from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
import os
from .utils import calculate_acos

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

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(
    request: Request,
    file: UploadFile = File(...)
):
    """Szablon funkcji do uploadu pliku CSV z metrykami"""
    
    if not file.filename.endswith('.csv'):
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

@app.get("/health")
async def health_check():
    """Endpoint do sprawdzenia stanu aplikacji"""
    return {"status": "healthy", "message": "Aplikacja działa prawidłowo"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 