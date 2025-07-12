# 🚀 Instrukcja wdrożenia ACOS Forecast Calculator

## ✅ Status przygotowania

Aplikacja jest **gotowa do wdrożenia**:
- ✅ Testowana lokalnie na http://localhost:8000
- ✅ Dockerfile skonfigurowany z obsługą Railway PORT
- ✅ Pliki Git gotowe do push na GitHub
- ✅ Railway.json przygotowany do automatycznego deployment

## 📋 Krok 1: Wrzucenie na GitHub

### 1.1 Stwórz repozytorium na GitHub
1. Idź na https://github.com
2. Kliknij "New repository"
3. Nazwa: `acos-forecast-calculator`
4. Opis: `ACOS Forecast Calculator - Aplikacja do analizy rentowności kampanii reklamowych`
5. Zaznacz: **Public** (lub Private jeśli chcesz)
6. **NIE** zaznaczaj: Add a README file, .gitignore, license
7. Kliknij "Create repository"

### 1.2 Połącz z lokalnym repozytorium
```bash
# W katalogu "Acos Appka"
git remote add origin https://github.com/TWOJ-USERNAME/acos-forecast-calculator.git
git branch -M main
git push -u origin main
```

**Zamień `TWOJ-USERNAME` na swoją nazwę użytkownika GitHub!**

### 1.3 Weryfikacja
Po push sprawdź na GitHub czy wszystkie pliki są widoczne:
- `app/` (main.py, utils.py, templates/, static/)
- `Dockerfile`
- `requirements.txt`
- `railway.json`
- `README.md`
- `.gitignore`

## 🚂 Krok 2: Wdrożenie na Railway

### 2.1 Logowanie do Railway
1. Idź na https://railway.app
2. Zaloguj się przez GitHub
3. Kliknij "New Project"

### 2.2 Połączenie z GitHub
1. Wybierz "Deploy from GitHub repo"
2. Znajdź repozytorium `acos-forecast-calculator`
3. Kliknij "Deploy Now"

### 2.3 Automatyczna konfiguracja
Railway automatycznie:
- Wykryje `Dockerfile`
- Użyje `railway.json` do konfiguracji
- Zbuduje obraz Docker
- Uruchomi aplikację

### 2.4 Monitorowanie deployment
W panelu Railway zobaczysz:
- **Build logs** - proces budowania
- **Deploy logs** - proces wdrażania
- **Application logs** - logi aplikacji

### 2.5 Dostęp do aplikacji
Po udanym deployment:
1. Railway wygeneruje URL (np. `https://acos-forecast-calculator-production.up.railway.app`)
2. Aplikacja będzie dostępna pod tym adresem
3. Możesz również ustawić custom domain

## 🔧 Krok 3: Konfiguracja (opcjonalnie)

### 3.1 Zmienne środowiskowe
W panelu Railway -> Variables możesz dodać:
```
PORT=8000
PYTHONPATH=/code/app
```

### 3.2 Custom domain
1. W panelu Railway kliknij "Settings"
2. Przejdź do "Domains"
3. Dodaj swój domain

## 🧪 Krok 4: Testowanie

### 4.1 Sprawdź funkcjonalność
1. Otwórz URL aplikacji
2. Sprawdź formularz obliczeń
3. Przetestuj z przykładowymi danymi:
   - Sprzedaż: 10000 PLN
   - Wydatki: 2000 PLN
   - Marża: 25%

### 4.2 Spodziewane wyniki
- ACOS: 20.00%
- ROI: 400.00%
- Zysk: 500.00 PLN
- Status: ✅ Kampania jest rentowna!

## 🔄 Krok 5: Aktualizacje

### 5.1 Zmiany w kodzie
```bash
# Edytuj pliki
# Potem:
git add .
git commit -m "Opis zmian"
git push origin main
```

### 5.2 Automatyczne wdrożenie
Railway automatycznie:
- Wykryje zmiany na GitHub
- Zbuduje nową wersję
- Wdroży bez przestojów

## 📊 Monitoring i debugowanie

### 6.1 Logi aplikacji
W panelu Railway:
- **Deploy** tab -> logi wdrożenia
- **Metrics** tab -> wydajność
- **Variables** tab -> zmienne

### 6.2 Problemy?
**Typowe problemy:**
1. **Import Error** - sprawdź czy wszystkie pliki są w repo
2. **Port Error** - Railway automatycznie ustawia PORT
3. **Build Error** - sprawdź Dockerfile i requirements.txt

**Rozwiązania:**
```bash
# Sprawdź logi locally
python3 -m uvicorn app.main:app --reload

# Sprawdź Docker locally (jeśli masz Docker)
docker build -t test-app .
docker run -p 8000:8000 test-app
```

## 🎯 Gotowe do użycia!

Po wykonaniu tych kroków Twoja aplikacja będzie:
- ✅ Dostępna online 24/7
- ✅ Automatycznie aktualizowana przy zmianach
- ✅ Skalowalna w Railway
- ✅ Zabezpieczona HTTPS
- ✅ Gotowa do dalszego rozwoju

## 📞 Wsparcie

Jeśli masz problemy:
1. Sprawdź logi w Railway
2. Zweryfikuj GitHub repo
3. Przetestuj lokalnie
4. Sprawdź dokumentację Railway

---
**Powodzenia z wdrożeniem! 🚀** 