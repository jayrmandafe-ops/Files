#!/usr/bin/env python3
"""
Development script to run both React frontend and Flask backend
"""
import subprocess
import os
import sys
import time
import signal
from threading import Thread

def run_flask():
    """Run Flask backend server"""
    print("🐍 Starting Flask backend server...")
    try:
        subprocess.run([sys.executable, "run_flask.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Flask server stopped")
    except Exception as e:
        print(f"❌ Flask server error: {e}")

def run_vite():
    """Run Vite frontend server"""
    print("⚛️ Starting Vite frontend server...")
    try:
        subprocess.run(["npm", "run", "dev"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Vite server stopped")
    except Exception as e:
        print(f"❌ Vite server error: {e}")

def main():
    """Run both servers concurrently"""
    print("🚀 Starting Kutur ni Jean Admin Dashboard Development Servers")
    print("=" * 60)
    
    # Create threads for both servers
    flask_thread = Thread(target=run_flask, daemon=True)
    vite_thread = Thread(target=run_vite, daemon=True)
    
    try:
        # Start Flask backend
        flask_thread.start()
        time.sleep(2)  # Give Flask time to start
        
        # Start Vite frontend
        vite_thread.start()
        
        print("\n🌐 Servers running:")
        print("   Frontend: http://localhost:3000 (React)")
        print("   Backend:  http://localhost:5001 (Flask)")
        print("\n💡 Press Ctrl+C to stop both servers")
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping development servers...")
        print("👋 Development session ended")

if __name__ == "__main__":
    main()