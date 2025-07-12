# 🎯 ACOS Forecast Calculator

Professional calculator for analyzing the profitability of advertising campaigns with NBP API integration and real-time currency conversion.

## 🚀 Features

- **ACOS Calculator**: Calculate profitability indicators of advertising campaigns
- **Campaign Forecasting**: Advanced prediction of campaign results based on metrics
- **Excel Export**: Generate detailed reports in Excel format
- **NBP Integration**: Automatic EUR/PLN currency conversion using National Bank of Poland API
- **Real-time Calculations**: Interactive sliders with instant results
- **Responsive Design**: Modern UI optimized for all devices

## 📊 Key Metrics

- **ACOS** (Advertising Cost of Sales): Campaign profitability indicator
- **ROI** (Return on Investment): Investment return calculation
- **Projected Sales**: Forecasted revenue based on campaign metrics
- **Projected Spend**: Estimated advertising costs
- **Break-even Analysis**: Profitability threshold calculation

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python 3.9+)
- **Frontend**: HTML5, CSS3, JavaScript
- **Templating**: Jinja2
- **Excel Export**: OpenPyXL
- **Currency API**: NBP (National Bank of Poland)
- **Deployment**: Railway.app, Docker

## 🚀 Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Kevinus31/acos-forecast-calculator.git
cd acos-forecast-calculator
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run the application:
```bash
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

4. Open in browser: `http://localhost:8000`

### Quick Start Scripts

- **Basic start**: `./start_app.sh`
- **F5 restart**: `python3 f5_restart.py`

## 🌐 Live Demo

The application is deployed on Railway.app: [Live Demo](https://acos-forecast-calculator-production.up.railway.app)

## 📖 Usage

### Basic ACOS Calculation
1. Enter projected sales (PLN)
2. Enter advertising spend (PLN)
3. Set gross margin (%)
4. Click "Calculate ACOS"

### Advanced Forecasting
1. Choose "Manual Inputs" method
2. Set campaign parameters using sliders:
   - Gross Margin (%)
   - Target AOV (EUR)
   - Target CTR (%)
   - Target CPC (EUR)
   - Target CVR (%)
   - Impressions
3. Results update in real-time

### Excel Export
- Fill in the forecast parameters
- Click "Export Results"
- Download generated Excel report

## 🔧 Configuration

### Environment Variables
```bash
PORT=8000                    # Application port
PYTHONPATH=/code/app        # Python path for imports
```

### Railway Deployment
The application is configured for Railway deployment with:
- `Dockerfile` for containerization
- `railway.json` for deployment configuration
- Automatic HTTPS and custom domain support

## 📁 Project Structure

```
acos-forecast-calculator/
├── app/
│   ├── main.py              # FastAPI application
│   ├── utils.py             # Calculation utilities
│   ├── static/              # CSS, JS, images
│   └── templates/           # HTML templates
├── Dockerfile               # Docker configuration
├── railway.json             # Railway deployment config
├── requirements.txt         # Python dependencies
├── start_app.sh            # Local start script
├── f5_restart.py           # F5 restart utility
└── README.md               # This file
```

## 🧮 Calculation Formulas

### ACOS Formula
```
ACOS = (Ad Spend / Ad Sales) × 100%
```

### ROI Formula
```
ROI = ((Revenue - Cost) / Cost) × 100%
```

### Forecast Calculations
```
Clicks = Impressions × CTR%
Orders = Clicks × CVR%
Ad Spend = Clicks × CPC
Ad Sales = Orders × AOV
```

## 🔄 Currency Conversion

The application uses NBP (National Bank of Poland) API for real-time EUR/PLN conversion:
- Automatic rate fetching with 24-hour cache
- Fallback rate: 4.30 PLN/EUR
- All calculations support both EUR and PLN display

## 🚀 Deployment

### Railway.app (Recommended)
1. Fork this repository
2. Connect to Railway.app
3. Deploy automatically with `railway.json`

### Docker
```bash
docker build -t acos-calculator .
docker run -p 8000:8000 acos-calculator
```

### Manual
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🛡️ Security

- Input validation for all user data
- HTTPS enforcement in production
- Environment variable protection
- No sensitive data in logs

## 📈 Performance

- Async FastAPI for high performance
- Efficient currency rate caching
- Optimized database-free architecture
- CDN-ready static files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Issues

If you encounter any issues:
1. Check the [Issues](https://github.com/Kevinus31/acos-forecast-calculator/issues) page
2. Review the deployment logs
3. Test locally first
4. Submit a detailed bug report

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the deployment guide

---

**Built with ❤️ for marketing professionals and campaign managers**
