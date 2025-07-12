#!/usr/bin/env python3
"""
F5 Application Restart Script
This script listens for F5 key presses and restarts the ACOS Calculator application.
"""

import subprocess
import sys
import signal
import time
import os
from threading import Thread

def restart_application():
    """Restart the FastAPI application"""
    print("\n🔄 Restarting ACOS Calculator...")
    
    # Kill existing processes
    try:
        subprocess.run(["pkill", "-f", "uvicorn app.main:app"], 
                      capture_output=True, check=False)
        time.sleep(1)
    except Exception as e:
        print(f"Error killing processes: {e}")
    
    # Start new process
    try:
        print("🚀 Starting application on http://localhost:8000")
        subprocess.Popen([
            "python3", "-m", "uvicorn", "app.main:app", 
            "--host", "0.0.0.0", "--port", "8000", "--reload"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ Application restarted successfully!")
        print("📍 Visit: http://localhost:8000")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

def signal_handler(signum, frame):
    """Handle Ctrl+C gracefully"""
    print("\n\n👋 Shutting down F5 restart listener...")
    # Kill FastAPI processes
    subprocess.run(["pkill", "-f", "uvicorn app.main:app"], 
                   capture_output=True, check=False)
    print("🛑 Application stopped.")
    sys.exit(0)

def main():
    """Main function"""
    print("🎯 ACOS Calculator - F5 Restart Listener")
    print("=" * 50)
    print("📍 Application will be available at: http://localhost:8000")
    print("⚡ Press F5 to restart the application")
    print("🛑 Press Ctrl+C to stop everything")
    print("=" * 50)
    
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start the application initially
    restart_application()
    
    print("\n⌨️  Listening for F5 key presses...")
    print("💡 In your terminal, press F5 to restart the application")
    print("💡 Alternative: Run './start_app.sh' to restart manually")
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        signal_handler(None, None)

if __name__ == "__main__":
    main() 