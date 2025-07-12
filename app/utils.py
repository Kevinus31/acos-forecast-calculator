from typing import Dict, Any, Optional

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
    impressions: int
) -> Dict[str, Any]:
    """
    Oblicza prognozę kampanii na podstawie zaawansowanych metryk.
    
    Args:
        gross_margin (float): Marża brutto w procentach
        target_aov (float): Docelowa wartość średniego zamówienia
        target_ctr (float): Docelowy CTR w procentach
        target_cpc (float): Docelowy koszt za kliknięcie
        target_cvr (float): Docelowy współczynnik konwersji w procentach
        impressions (int): Liczba wyświetleń
    
    Returns:
        Dict[str, Any]: Słownik z prognozami i wskaźnikami
    """
    
    # Obliczenia podstawowe
    clicks = impressions * (target_ctr / 100)
    conversions = clicks * (target_cvr / 100)
    spend = clicks * target_cpc
    sales = conversions * target_aov
    
    # Obliczenie wskaźników
    acos = (spend / sales) * 100 if sales > 0 else 0
    roi = ((sales - spend) / spend) * 100 if spend > 0 else 0
    
    # Obliczenie zysku
    profit_per_sale = (sales * gross_margin / 100) - spend
    total_profit = profit_per_sale
    
    # Break-even ACOS
    break_even_acos = gross_margin
    
    # Sprawdzenie rentowności
    is_profitable = acos <= gross_margin if gross_margin > 0 else False
    
    # Przygotowanie komunikatów
    profitability_message = ""
    if not is_profitable and acos > 0:
        profitability_message = f"⚠️ UWAGA: Kampania jest nierentowna! ACOS ({acos:.2f}%) przekracza marżę ({gross_margin:.2f}%)"
    elif is_profitable and acos > 0:
        profitability_message = f"✅ Kampania jest rentowna! ACOS ({acos:.2f}%) mieści się w marży ({gross_margin:.2f}%)"
    
    # Określenie statusu rentowności
    profitability_status = "profitable" if is_profitable else "unprofitable"
    
    return {
        # Wskaźniki podstawowe
        "acos": round(acos, 2),
        "roi": round(roi, 2),
        "profit": round(total_profit, 2),
        "break_even_acos": round(break_even_acos, 2),
        "is_profitable": is_profitable,
        "profitability_message": profitability_message,
        "profitability_status": profitability_status,
        
        # Prognozowane wyniki
        "impressions": impressions,
        "clicks": round(clicks, 0),
        "conversions": round(conversions, 0),
        "sales": round(sales, 2),
        "spend": round(spend, 2),
        
        # Parametry wejściowe
        "gross_margin": gross_margin,
        "target_aov": target_aov,
        "target_ctr": target_ctr,
        "target_cpc": target_cpc,
        "target_cvr": target_cvr,
        
        # Dodatkowe wskaźniki
        "cpm": round((spend / impressions) * 1000, 2) if impressions > 0 else 0,
        "cost_per_conversion": round(spend / conversions, 2) if conversions > 0 else 0,
        "roas": round(sales / spend, 2) if spend > 0 else 0
    }

def format_currency(amount: float) -> str:
    """
    Formatuje kwotę w walucie polskiej (PLN).
    
    Args:
        amount (float): Kwota do sformatowania
    
    Returns:
        str: Sformatowana kwota
    """
    return f"{amount:,.2f} PLN".replace(',', ' ')

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