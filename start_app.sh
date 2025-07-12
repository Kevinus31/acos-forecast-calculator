#!/bin/bash

# ACOS Calculator - Easy Start Script
# Press F5 in your terminal to restart the application

echo "🚀 Starting ACOS Calculator..."
echo "📍 Location: http://localhost:8000"
echo "⚡ Press Ctrl+C to stop the application"
echo "🔄 To restart, press F5 in your terminal"
echo "----------------------------------------"

# Kill any existing FastAPI/uvicorn processes
pkill -f "uvicorn app.main:app" 2>/dev/null

# Wait a moment for cleanup
sleep 1

# Start the application with auto-reload
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 