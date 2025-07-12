# 🔧 GitHub Setup i Railway Deployment

## 📋 Krok 1: Stworzenie repozytorium GitHub

### 1.1 Utwórz nowe repozytorium
1. Idź na https://github.com
2. Kliknij **"New repository"**
3. Wypełnij dane:
   - **Repository name**: `acos-forecast-calculator`
   - **Description**: `ACOS Forecast Calculator - Professional advertising campaign profitability analyzer`
   - **Visibility**: Public (lub Private)
   - **⚠️ NIE zaznaczaj**: "Add a README file", "Add .gitignore", "Choose a license"
4. Kliknij **"Create repository"**

### 1.2 Skopiuj URL repozytorium
Po utworzeniu repozytorium skopiuj URL w formacie:
```
https://github.com/TWOJA-NAZWA-UŻYTKOWNIKA/acos-forecast-calculator.git
```

## 🔗 Krok 2: Połączenie z GitHub

### 2.1 Dodaj remote repository
```bash
git remote add origin https://github.com/TWOJA-NAZWA-UŻYTKOWNIKA/acos-forecast-calculator.git
```

**⚠️ Zamień `TWOJA-NAZWA-UŻYTKOWNIKA` na swoją nazwę użytkownika GitHub!**

### 2.2 Wypchnij kod na GitHub
```bash
git branch -M main
git push -u origin main
```

### 2.3 Weryfikacja
Po wykonaniu powyższych kroków sprawdź na GitHub czy wszystkie pliki są widoczne:
- ✅ `app/` (main.py, utils.py, templates/, static/)
- ✅ `Dockerfile`
- ✅ `requirements.txt`
- ✅ `railway.json`
- ✅ `README.md`
- ✅ `.gitignore`
- ✅ `DEPLOYMENT.md`

## 🚂 Krok 3: Deploy na Railway

### 3.1 Przygotowanie Railway
1. Idź na https://railway.app
2. Kliknij **"Login"**
3. Zaloguj się przez **GitHub**
4. Kliknij **"New Project"**

### 3.2 Deployment
1. Wybierz **"Deploy from GitHub repo"**
2. Znajdź repozytorium `acos-forecast-calculator`
3. Kliknij **"Deploy Now"**

### 3.3 Automatyczna konfiguracja
Railway automatycznie:
- ✅ Wykryje `Dockerfile`
- ✅ Użyje `railway.json` do konfiguracji
- ✅ Zbuduje obraz Docker
- ✅ Uruchomi aplikację na porcie dynamicznym

### 3.4 Monitoring
W panelu Railway będziesz mógł zobaczyć:
- **Build logs** - proces budowania
- **Deploy logs** - proces wdrażania
- **Application logs** - logi aplikacji w czasie rzeczywistym

## 🌐 Krok 4: Dostęp do aplikacji

### 4.1 URL aplikacji
Po udanym deployment Railway wygeneruje unikalny URL:
```
https://acos-forecast-calculator-production.up.railway.app
```

### 4.2 Custom Domain (opcjonalnie)
1. W panelu Railway kliknij **"Settings"**
2. Przejdź do **"Domains"**
3. Dodaj swój własny domain

## 🔧 Krok 5: Konfiguracja zmiennych (opcjonalnie)

### 5.1 Environment Variables
W panelu Railway -> **Variables** możesz dodać:
```bash
PORT=8000
PYTHONPATH=/code/app
```

**💡 Uwaga**: Railway automatycznie ustawia zmienną `PORT`, więc nie musisz jej konfigurować ręcznie.

## 🧪 Krok 6: Testowanie

### 6.1 Sprawdź funkcjonalność
1. Otwórz URL aplikacji
2. Sprawdź formularz obliczeń
3. Przetestuj z przykładowymi danymi:
   - **Gross Margin**: 30%
   - **Target AOV**: 25 EUR
   - **Target CTR**: 3%
   - **Target CPC**: 1 EUR
   - **Target CVR**: 3%
   - **Impressions**: 1000

### 6.2 Spodziewane wyniki
- **ACOS**: około 48%
- **ROI**: dodatni wynik
- **Projected Sales**: obliczone na podstawie metryk
- **Status**: zależny od marży vs ACOS

## 🔄 Krok 7: Aktualizacje

### 7.1 Zmiany w kodzie
Po wprowadzeniu zmian w kodzie:
```bash
git add .
git commit -m "Opis zmian"
git push origin main
```

### 7.2 Automatyczne wdrożenie
Railway automatycznie:
- ✅ Wykryje zmiany na GitHub
- ✅ Zbuduje nową wersję
- ✅ Wdroży bez przestojów (zero-downtime deployment)

## 🛠️ Troubleshooting

### Problem: Git push błąd
```bash
# Jeśli masz problemy z push:
git pull origin main --rebase
git push origin main
```

### Problem: Railway build błąd
1. Sprawdź logi w Railway dashboard
2. Zweryfikuj `requirements.txt`
3. Sprawdź `Dockerfile`

### Problem: Aplikacja nie odpowiada
1. Sprawdź **Deploy logs** w Railway
2. Sprawdź **Application logs**
3. Zweryfikuj czy port jest poprawnie skonfigurowany

## 📞 Wsparcie

Jeśli masz problemy:
1. 📖 Sprawdź dokumentację Railway: https://docs.railway.app
2. 💬 GitHub Issues w repozytorium
3. 🔍 Sprawdź logi w Railway dashboard

---

## 🎯 Gotowy do uruchomienia!

Po wykonaniu tych kroków Twoja aplikacja będzie:
- ✅ Dostępna online 24/7
- ✅ Automatycznie aktualizowana
- ✅ Zabezpieczona HTTPS
- ✅ Skalowalna
- ✅ Profesjonalnie wdrożona

**Powodzenia! 🚀** 