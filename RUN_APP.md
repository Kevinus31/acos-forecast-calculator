# 🚀 ACOS Calculator - Instrukcja uruchomienia

## Szybki start

### Metoda 1: Uruchomienie podstawowe
```bash
./start_app.sh
```

### Metoda 2: Z F5 restart (zalecana)
```bash
python3 f5_restart.py
```

## 🎯 Dostęp do aplikacji

Po uruchomieniu aplikacja będzie dostępna pod adresem:
**http://localhost:8000**

## ⚡ Restart aplikacji

### Opcja 1: Restart manualny
- Naciśnij `Ctrl+C` aby zatrzymać aplikację
- Uruchom ponownie `./start_app.sh`

### Opcja 2: Restart z F5 (w terminalu)
1. Uruchom: `python3 f5_restart.py`
2. W terminalu naciśnij `F5` aby zrestartować aplikację
3. Aplikacja automatycznie się zrestartuje

### Opcja 3: Konfiguracja F5 w terminalu macOS

#### Dla Terminal.app:
1. Otwórz Terminal > Preferencje > Profiles > Keyboard
2. Dodaj nowe powiązanie klawisza:
   - Klawisz: `F5`
   - Akcja: `send text`
   - Tekst: `./start_app.sh\n`

#### Dla iTerm2:
1. Otwórz iTerm2 > Preferences > Profiles > Keys
2. Dodaj nowy Key Mapping:
   - Klawisz: `F5`
   - Akcja: `Send Text`
   - Tekst: `./start_app.sh\n`

## 📋 Funkcje aplikacji

- **Kalkulator ACOS**: Obliczanie wskaźników rentowności kampanii
- **Prognoza kampanii**: Zaawansowane przewidywanie wyników
- **Eksport do Excel**: Generowanie raportów
- **Integracja z NBP**: Automatyczne przeliczanie walut EUR/PLN

## 🛠️ Rozwiązywanie problemów

### Port już zajęty?
```bash
# Zabij wszystkie procesy uvicorn
pkill -f uvicorn

# Sprawdź co używa portu 8000
lsof -i :8000
```

### Problemy z zależnościami?
```bash
# Zaktualizuj pip
python3 -m pip install --upgrade pip

# Zainstaluj ponownie zależności
python3 -m pip install -r requirements.txt
```

## 📝 Pliki konfiguracyjne

- `start_app.sh` - Skrypt uruchamiający
- `f5_restart.py` - Skrypt F5 restart
- `app/main.py` - Główna aplikacja FastAPI
- `requirements.txt` - Zależności Python

## 🔧 Rozwój

Aplikacja korzysta z `--reload` więc zmiany w kodzie są automatycznie ładowane bez potrzeby restartu. 