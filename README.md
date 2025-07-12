# ACOS Forecast Calculator

Aplikacja webowa do obliczania wskaźników ACOS, ROI i analizy rentowności kampanii reklamowych.

## Funkcjonalności

- ✅ Obliczanie wskaźników ACOS (Advertising Cost of Sales)
- ✅ Kalkulacja ROI (Return on Investment)
- ✅ Analiza rentowności kampanii
- ✅ Określanie break-even ACOS
- ✅ Ostrzeżenia o nierentownych kampaniach
- ✅ Responsywny interfejs użytkownika
- ✅ Szablon uploadu plików CSV
- ✅ Wszystkie komunikaty w języku polskim

## Technologie

- **Backend**: FastAPI (Python 3.11+)
- **Frontend**: Jinja2 + HTML + CSS
- **Deployment**: Docker + Railway
- **Styling**: CSS Grid + Flexbox (responsywny)

## Struktura projektu

```
/
├── app/
│   ├── main.py              # Główna aplikacja FastAPI
│   ├── utils.py             # Logika obliczeń ACOS
│   ├── templates/
│   │   └── index.html       # Szablon HTML
│   └── static/
│       └── style.css        # Style CSS
├── Dockerfile               # Kontener Docker
├── requirements.txt         # Zależności Python
└── README.md               # Dokumentacja
```

## Uruchomienie lokalne

### Wymagania
- Python 3.11+
- pip

### Instalacja

1. **Sklonuj repozytorium**:
```bash
git clone <repository-url>
cd acos-forecast-calculator
```

2. **Utwórz wirtualne środowisko**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# lub
venv\Scripts\activate     # Windows
```

3. **Zainstaluj zależności**:
```bash
pip install -r requirements.txt
```

4. **Uruchom aplikację**:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

5. **Otwórz w przeglądarce**:
```
http://localhost:8000
```

## Uruchomienie z Docker

### Wymagania
- Docker
- Docker Compose (opcjonalnie)

### Instrukcje

1. **Zbuduj obraz Docker**:
```bash
docker build -t acos-calculator .
```

2. **Uruchom kontener**:
```bash
docker run -p 8000:8000 acos-calculator
```

3. **Otwórz w przeglądarce**:
```
http://localhost:8000
```

## Deployment na Railway

### Wymagania
- Konto Railway (https://railway.app)
- Repozytorium GitHub z kodem

### Instrukcje

1. **Przygotuj repozytorium**:
   - Wrzuć kod do repozytorium GitHub
   - Upewnij się, że wszystkie pliki są commitowane

2. **Połącz z Railway**:
   - Zaloguj się na Railway
   - Kliknij "New Project"
   - Wybierz "Deploy from GitHub repo"
   - Wybierz swoje repozytorium

3. **Konfiguracja**:
   - Railway automatycznie wykryje Dockerfile
   - Ustawi port 8000
   - Zbuduje i wdroży aplikację

4. **Dostęp**:
   - Po udanym deployment otrzymasz URL
   - Aplikacja będzie dostępna pod adresem: `https://twoja-aplikacja.railway.app`

### Konfiguracja zmiennych środowiskowych (opcjonalnie)

Jeśli chcesz dodać dodatkowe konfiguracje:

```bash
# W panelu Railway -> Variables
PORT=8000
PYTHONPATH=/code/app
```

## Użytkowanie

### Formularz obliczeń

1. **Wprowadź dane**:
   - Prognozowana sprzedaż (PLN)
   - Prognozowane wydatki na reklamę (PLN)
   - Marża brutto (%)

2. **Kliknij "Oblicz ACOS"**

3. **Analizuj wyniki**:
   - **ACOS**: Koszt reklamy do sprzedaży
   - **ROI**: Zwrot z inwestycji
   - **Zysk**: Przewidywany zysk
   - **Break-even ACOS**: Punkt rentowności

### Interpretacja wyników

- **🟢 Rentowna kampania**: ACOS ≤ Marża brutto
- **🔴 Nierentowna kampania**: ACOS > Marża brutto
- **Break-even ACOS**: Maksymalny ACOS dla rentowności

### Upload plików

Funkcja w trakcie rozwoju. Szablon przygotowany do:
- Uploadu plików CSV
- Przetwarzania danych z pliku
- Automatycznego obliczania wskaźników

## Rozwój aplikacji

### Dodanie nowych funkcji

1. **Edytuj logikę**: `app/utils.py`
2. **Dodaj endpointy**: `app/main.py`
3. **Zaktualizuj UI**: `app/templates/index.html`
4. **Dodaj style**: `app/static/style.css`

### Przykłady rozbudowy

- Wykresy i wizualizacje
- Analiza wielokanałowa
- Eksport wyników do PDF
- Integracja z API reklamowymi
- Baza danych historii obliczeń

## API Endpoints

- `GET /` - Strona główna
- `POST /calculate` - Obliczanie ACOS
- `POST /upload` - Upload pliku CSV
- `GET /health` - Status aplikacji

## Wsparcie

W przypadku problemów:
1. Sprawdź logi aplikacji
2. Zweryfikuj format danych wejściowych
3. Upewnij się, że wszystkie zależności są zainstalowane

## Licencja

Projekt stworzony na potrzeby analizy kampanii reklamowych.

---

**Autor**: ACOS Forecast Calculator Team  
**Wersja**: 1.0.0  
**Data**: 2024 