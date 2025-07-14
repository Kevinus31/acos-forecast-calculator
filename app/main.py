from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
import os
from .utils import calculate_acos, calculate_forecast_from_metrics, calculate_budget_from_tacos, generate_export_data, get_eur_rate_from_nbp, create_excel_report
import json
from datetime import datetime

# Inicjalizacja aplikacji FastAPI
app = FastAPI(title="ACOS Forecast Calculator", description="Kalkulator prognoz ACOS")

# Konfiguracja statycznych plików i szablonów
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Strona główna z formularzem do obliczeń ACOS"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    sales: float = Form(..., description="Prognozowana sprzedaż"),
    spend: float = Form(..., description="Prognozowane wydatki na reklamę"),
    margin: float = Form(..., description="Marża brutto w procentach")
):
    """Obliczanie wskaźników ACOS na podstawie danych z formularza"""
    
    # Walidacja danych wejściowych
    if sales < 0 or spend < 0 or margin < 0:
        error_message = "Wszystkie wartości muszą być dodatnie!"
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": error_message,
            "sales": sales,
            "spend": spend,
            "margin": margin
        })
    
    # Obliczenie wskaźników
    results = calculate_acos(sales, spend, margin)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "results": results,
        "sales": sales,
        "spend": spend,
        "margin": margin
    })

@app.post("/calculate-forecast", response_class=HTMLResponse)
async def calculate_forecast(
    request: Request,
    gross_margin: float = Form(..., description="Marża brutto w procentach"),
    target_aov: float = Form(..., description="Docelowa wartość średniego zamówienia"),
    target_ctr: float = Form(..., description="Docelowy CTR w procentach"),
    target_cpc: float = Form(..., description="Docelowy koszt za kliknięcie"),
    target_cvr: float = Form(..., description="Docelowy współczynnik konwersji w procentach"),
    impressions: int = Form(..., description="Liczba wyświetleń")
):
    """Obliczanie prognoz na podstawie zaawansowanych metryk kampanii"""
    
    # Walidacja danych wejściowych
    if any(val < 0 for val in [gross_margin, target_aov, target_ctr, target_cpc, target_cvr, impressions]):
        error_message = "Wszystkie wartości muszą być dodatnie!"
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": error_message,
            "gross_margin": gross_margin,
            "target_aov": target_aov,
            "target_ctr": target_ctr,
            "target_cpc": target_cpc,
            "target_cvr": target_cvr,
            "impressions": impressions
        })
    
    # Obliczenie prognoz
    results = calculate_forecast_from_metrics(
        gross_margin, target_aov, target_ctr, target_cpc, target_cvr, impressions
    )
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "results": results,
        "forecast_mode": True,
        "gross_margin": gross_margin,
        "target_aov": target_aov,
        "target_ctr": target_ctr,
        "target_cpc": target_cpc,
        "target_cvr": target_cvr,
        "impressions": impressions
    })

@app.get("/budget", response_class=HTMLResponse)
async def budget_form(request: Request):
    """Wyświetla osobny kalkulator budżetu w nowym oknie"""
    return templates.TemplateResponse("budget.html", {"request": request})

@app.post("/calculate-budget", response_class=HTMLResponse)
async def calculate_budget(
    request: Request,
    target_sales: float = Form(..., description="Docelowa wartość sprzedaży w EUR"),
    target_tacos: float = Form(..., description="Zakładany TACOS w procentach"),
    gross_margin: float = Form(..., description="Marża brutto w procentach")
):
    """Obliczanie budżetu marketingowego na podstawie zakładanego TACOS"""
    if any(val < 0 for val in [target_sales, target_tacos, gross_margin]):
        error_message = "Wszystkie wartości muszą być dodatnie!"
        return templates.TemplateResponse("budget.html", {
            "request": request,
            "error": error_message,
            "target_sales": target_sales,
            "target_tacos": target_tacos,
            "gross_margin": gross_margin
        })
    results = calculate_budget_from_tacos(target_sales, target_tacos, gross_margin)
    return templates.TemplateResponse("budget.html", {
        "request": request,
        "results": results,
        "target_sales": target_sales,
        "target_tacos": target_tacos,
        "gross_margin": gross_margin
    })

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(
    request: Request,
    file: UploadFile = File(...)
):
    """Szablon funkcji do uploadu pliku CSV z metrykami"""
    
    if not file.filename or not file.filename.endswith('.csv'):
        error_message = "Proszę przesłać plik CSV!"
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": error_message
        })
    
    # Tutaj można dodać logikę przetwarzania pliku CSV
    # Na razie zwracamy komunikat o pomyślnym przesłaniu
    success_message = f"Plik {file.filename} został pomyślnie przesłany. Funkcja w trakcie rozwoju."
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "success": success_message
    })

@app.post("/export-results")
async def export_results(
    request: Request,
    gross_margin: float = Form(...),
    target_aov: float = Form(...),
    target_ctr: float = Form(...),
    target_cpc: float = Form(...),
    target_cvr: float = Form(...),
    impressions: int = Form(...)
):
    """Endpoint do eksportu wyników obliczeń w formacie Excel"""
    
    # Oblicz wyniki
    results = calculate_forecast_from_metrics(
        gross_margin, target_aov, target_ctr, target_cpc, target_cvr, impressions
    )
    
    # Wygeneruj raport Excel
    excel_buffer = create_excel_report(results)
    
    # Generuj nazwę pliku z datą
    filename = f"prognoza_acos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    
    # Zwróć plik Excel do pobrania
    return StreamingResponse(
        iter([excel_buffer.getvalue()]),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )

@app.get("/currency-info")
async def get_currency_info():
    """Endpoint do pobierania informacji o kursie EUR/PLN"""
    eur_rate = get_eur_rate_from_nbp()
    return {
        "currency": "EUR",
        "eur_pln_rate": eur_rate,
        "source": "NBP API",
        "last_updated": "cache"
    }

@app.get("/health")
async def health_check():
    """Endpoint do sprawdzenia stanu aplikacji"""
    return {"status": "healthy", "message": "Aplikacja działa prawidłowo"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 