from typing import Dict, Any, Optional
import requests
import json
from datetime import datetime, timedelta

# Cache dla kursu EUR (ważny przez 1 dzień)
_eur_rate_cache: Dict[str, Any] = {"rate": None, "timestamp": None}

def get_eur_rate_from_nbp() -> float:
    """
    Pobiera aktualny kurs EUR/PLN z API Narodowego Banku Polskiego.
    Używa cache'u aby ograniczyć liczbę zapytań do API.
    
    Returns:
        float: Kurs EUR/PLN
    """
    global _eur_rate_cache
    
    # Sprawdź czy mamy świeży kurs w cache (max 1 dzień)
    if (_eur_rate_cache["rate"] is not None and 
        _eur_rate_cache["timestamp"] is not None):
        
        time_diff = datetime.now() - _eur_rate_cache["timestamp"]
        if time_diff.total_seconds() < 24 * 3600:  # 24 godziny
            return _eur_rate_cache["rate"]
    
    try:
        # Pobierz aktualny kurs EUR z NBP API
        response = requests.get(
            "https://api.nbp.pl/api/exchangerates/rates/a/eur/",
            headers={"Accept": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            rate = data["rates"][0]["mid"]
            
            # Zapisz w cache
            _eur_rate_cache["rate"] = rate
            _eur_rate_cache["timestamp"] = datetime.now()
            
            return rate
        else:
            # Fallback rate jeśli API nie działa
            return 4.30  # Przybliżony kurs EUR/PLN
            
    except Exception as e:
        print(f"Błąd przy pobieraniu kursu EUR: {e}")
        # Fallback rate
        return 4.30

def convert_pln_to_eur(amount_pln: float) -> float:
    """
    Przelicza kwotę z PLN na EUR używając kursu NBP.
    
    Args:
        amount_pln (float): Kwota w PLN
    
    Returns:
        float: Kwota w EUR
    """
    eur_rate = get_eur_rate_from_nbp()
    return round(amount_pln / eur_rate, 2)

def convert_eur_to_pln(amount_eur: float) -> float:
    """
    Przelicza kwotę z EUR na PLN używając kursu NBP.
    
    Args:
        amount_eur (float): Kwota w EUR
    
    Returns:
        float: Kwota w PLN
    """
    eur_rate = get_eur_rate_from_nbp()
    return round(amount_eur * eur_rate, 2)

def calculate_acos(sales: float, spend: float, margin: float) -> Dict[str, Any]:
    """
    Oblicza wskaźniki ACOS, ROI, zysk i sprawdza rentowność kampanii.
    
    Args:
        sales (float): Prognozowana sprzedaż
        spend (float): Prognozowane wydatki na reklamę
        margin (float): Marża brutto w procentach
    
    Returns:
        Dict[str, Any]: Słownik z obliczonymi wskaźnikami
    """
    
    # Obliczenie ACOS (Advertising Cost of Sales)
    acos = (spend / sales) * 100 if sales > 0 else 0
    
    # Obliczenie ROI (Return on Investment)
    roi = ((sales - spend) / spend) * 100 if spend > 0 else 0
    
    # Obliczenie zysku
    profit_per_sale = (sales * margin / 100) - spend
    total_profit = profit_per_sale
    
    # Break-even ACOS (punkt rentowności)
    break_even_acos = margin
    
    # Sprawdzenie rentowności
    is_profitable = acos <= margin if margin > 0 else False
    
    # Przygotowanie komunikatów
    profitability_message = ""
    if not is_profitable and acos > 0:
        profitability_message = f"⚠️ UWAGA: Kampania jest nierentowna! ACOS ({acos:.2f}%) przekracza marżę ({margin:.2f}%)"
    elif is_profitable and acos > 0:
        profitability_message = f"✅ Kampania jest rentowna! ACOS ({acos:.2f}%) mieści się w marży ({margin:.2f}%)"
    
    # Określenie statusu rentowności
    profitability_status = "profitable" if is_profitable else "unprofitable"
    
    return {
        "acos": round(acos, 2),
        "roi": round(roi, 2),
        "profit": round(total_profit, 2),
        "break_even_acos": round(break_even_acos, 2),
        "is_profitable": is_profitable,
        "profitability_message": profitability_message,
        "profitability_status": profitability_status,
        "sales": sales,
        "spend": spend,
        "margin": margin
    }

def calculate_forecast_from_metrics(
    gross_margin: float,
    target_aov: float,
    target_ctr: float,
    target_cpc: float,
    target_cvr: float,
    impressions: int,
    currency: str = "EUR"
) -> Dict[str, Any]:
    """
    Oblicza prognozę kampanii na podstawie zaawansowanych metryk w EUR.
    Używa poprawionej formuły ACOS: (Bid × Clicks) / [(Impressions × CTR%) × CVR% × AOV]
    
    Args:
        gross_margin (float): Marża brutto w procentach
        target_aov (float): Docelowa wartość średniego zamówienia w EUR
        target_ctr (float): Docelowy CTR w procentach
        target_cpc (float): Docelowy koszt za kliknięcie w EUR (Bid)
        target_cvr (float): Docelowy współczynnik konwersji w procentach
        impressions (int): Liczba wyświetleń
        currency (str): Waluta do wyświetlania (EUR)
    
    Returns:
        Dict[str, Any]: Słownik z prognozami i wskaźnikami
    """
    
    # Obliczenia podstawowe zgodnie z formułą ACOS
    clicks = impressions * (target_ctr / 100)
    orders = clicks * (target_cvr / 100)  # Zmiana nazwy z conversions na orders
    ad_spend = clicks * target_cpc  # Ad Spend = Bid × Clicks
    ad_sales = orders * target_aov  # Ad Sales = Orders × AOV
    
    # Obliczenie ACOS według wzoru: ACOS = Ad Spend / Ad Sales
    acos = (ad_spend / ad_sales) * 100 if ad_sales > 0 else 0
    
    # ROI = (Revenue - Cost) / Cost
    roi = ((ad_sales - ad_spend) / ad_spend) * 100 if ad_spend > 0 else 0
    
    # ROAS = Revenue / Ad Spend
    roas = ad_sales / ad_spend if ad_spend > 0 else 0
    
    # Obliczenie zysku - Profit per Sale uwzględnia marżę brutto
    gross_profit = ad_sales * (gross_margin / 100)  # Zysk brutto ze sprzedaży
    total_profit = gross_profit - ad_spend  # Zysk całkowity po odjęciu kosztów reklamy
    profit_per_sale = total_profit / orders if orders > 0 else 0
    
    # Break-even ACOS = marża brutto
    break_even_acos = gross_margin
    
    # Sprawdzenie rentowności
    is_profitable = acos <= gross_margin if gross_margin > 0 and acos > 0 else False
    
    # Przygotowanie komunikatów rentowności
    profitability_message = ""
    if acos > 0:
        if not is_profitable:
            profitability_message = (
                f"⚠️ Nierentowna kampania: ACOS {acos:.0f}% przekracza marżę {gross_margin:.0f}%. "
                f"Rozważ poprawę współczynnika konwersji, obniżenie CPC lub zwiększenie marży produktu."
            )
        else:
            profitability_message = f"✅ Rentowna kampania: ACOS {acos:.0f}% mieści się w marży {gross_margin:.0f}%"
    
    # Określenie statusu rentowności
    profitability_status = "profitable" if is_profitable else "unprofitable"
    
    # Pobierz aktualny kurs EUR/PLN dla informacji
    eur_rate = get_eur_rate_from_nbp()
    
    return {
        # Wskaźniki podstawowe
        "acos": round(acos, 0),  # Zaokrąglenie do całości jak na screenshocie
        "roi": round(roi, 0),
        "profit": round(total_profit, 0),
        "profit_per_sale": round(profit_per_sale, 0),
        "break_even_acos": round(break_even_acos, 0),
        "is_profitable": is_profitable,
        "profitability_message": profitability_message,
        "profitability_status": profitability_status,
        
        # Prognozowane wyniki (Forecast Results)
        "impressions": impressions,
        "clicks": round(clicks, 0),  # Projected Clicks
        "orders": round(orders, 0),  # Projected Orders (zamiast conversions)
        "projected_sales": round(ad_sales, 0),  # Projected Sales
        "projected_spend": round(ad_spend, 0),  # Projected Spend
        
        # Parametry wejściowe
        "gross_margin": gross_margin,
        "target_aov": target_aov,
        "target_ctr": target_ctr,
        "target_cpc": target_cpc,
        "target_cvr": target_cvr,
        
        # Dodatkowe wskaźniki
        "cpm": round((ad_spend / impressions) * 1000, 2) if impressions > 0 else 0,
        "cost_per_conversion": round(ad_spend / orders, 2) if orders > 0 else 0,
        "roas": round(roas, 2),
        
        # Informacje o walucie
        "currency": currency,
        "eur_rate": round(eur_rate, 4),
        "currency_info": f"Kurs EUR/PLN: {eur_rate:.4f} (NBP)"
    }

def format_currency(amount: float, currency: str = "EUR") -> str:
    """
    Formatuje kwotę w podanej walucie.
    
    Args:
        amount (float): Kwota do sformatowania
        currency (str): Kod waluty (EUR, PLN)
    
    Returns:
        str: Sformatowana kwota
    """
    if currency == "EUR":
        return f"€{amount:,.0f}".replace(',', ' ')
    elif currency == "PLN":
        return f"{amount:,.2f} PLN".replace(',', ' ')
    else:
        return f"{amount:,.2f} {currency}".replace(',', ' ')

def format_percentage(value: float) -> str:
    """
    Formatuje wartość procentową.
    
    Args:
        value (float): Wartość do sformatowania
    
    Returns:
        str: Sformatowana wartość procentowa
    """
    return f"{value:.2f}%"

def validate_input_data(sales: float, spend: float, margin: float) -> Dict[str, Any]:
    """
    Waliduje dane wejściowe do obliczeń.
    
    Args:
        sales (float): Prognozowana sprzedaż
        spend (float): Prognozowane wydatki na reklamę
        margin (float): Marża brutto w procentach
    
    Returns:
        Dict[str, Any]: Słownik z wynikiem walidacji
    """
    errors = []
    
    if sales < 0:
        errors.append("Prognozowana sprzedaż musi być dodatnia")
    
    if spend < 0:
        errors.append("Prognozowane wydatki muszą być dodatnie")
    
    if margin < 0:
        errors.append("Marża brutto musi być dodatnia")
    
    if margin > 100:
        errors.append("Marża brutto nie może przekraczać 100%")
    
    if sales > 0 and spend > sales:
        errors.append("Wydatki na reklamę nie mogą być większe niż prognozowana sprzedaż")
    
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

def generate_export_data(results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generuje dane do eksportu w formacie odpowiednim do pobrania.
    
    Args:
        results (Dict[str, Any]): Wyniki obliczeń ACOS
    
    Returns:
        Dict[str, Any]: Dane do eksportu
    """
    export_data = {
        "export_timestamp": datetime.now().isoformat(),
        "forecast_results": {
            "projected_sales_eur": results.get("projected_sales", 0),
            "projected_spend_eur": results.get("projected_spend", 0),
            "expected_acos_percent": results.get("acos", 0),
            "roi_percent": results.get("roi", 0),
            "profit_per_sale_eur": results.get("profit_per_sale", 0),
            "total_profit_eur": results.get("profit", 0),
            "break_even_acos_percent": results.get("break_even_acos", 0),
            "projected_clicks": results.get("clicks", 0),
            "projected_orders": results.get("orders", 0),
            "roas": results.get("roas", 0),
            "cpm_eur": results.get("cpm", 0),
            "cost_per_conversion_eur": results.get("cost_per_conversion", 0)
        },
        "input_parameters": {
            "gross_margin_percent": results.get("gross_margin", 0),
            "target_aov_eur": results.get("target_aov", 0),
            "target_ctr_percent": results.get("target_ctr", 0),
            "target_cpc_eur": results.get("target_cpc", 0),
            "target_cvr_percent": results.get("target_cvr", 0),
            "impressions": results.get("impressions", 0)
        },
        "profitability_analysis": {
            "is_profitable": results.get("is_profitable", False),
            "profitability_status": results.get("profitability_status", "unknown"),
            "profitability_message": results.get("profitability_message", "")
        },
        "currency_info": {
            "primary_currency": "EUR",
            "eur_pln_rate": results.get("eur_rate", 4.30),
            "currency_source": "NBP API"
        },
        "acos_formula": "ACOS = Ad Spend / Ad Sales = (Bid × Clicks) / (Orders × AOV)",
        "recommendations": {
            "target_acos_max": results.get("break_even_acos", 0),
            "current_performance": "profitable" if results.get("is_profitable", False) else "unprofitable"
        }
    }
    
    return export_data 