#!/usr/bin/env python3
"""
Flask backend server for Kutur ni Jean Admin Dashboard
"""
import os
from app import app

if __name__ == '__main__':
    # Set environment variables for development
    os.environ.setdefault('FLASK_ENV', 'development')
    os.environ.setdefault('FLASK_DEBUG', '1')
    
    # Run the Flask app
    port = int(os.environ.get('PORT', 5001))  # Use different port to avoid conflict
    print(f"🐍 Starting Flask server on port {port}")
    print(f"🌐 API will be available at: http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)