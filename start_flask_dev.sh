#!/bin/bash
# Development script to run Flask backend

echo "🐍 Starting Flask backend server..."
echo "📍 Working directory: $(pwd)"
echo "🔧 Python version: $(python --version)"

# Check if required packages are installed
python -c "import flask, flask_cors, psycopg2" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Required packages are installed"
else
    echo "❌ Missing packages. Installing..."
    pip install flask flask-cors psycopg2-binary python-dotenv
fi

# Set environment variables
export FLASK_ENV=development
export FLASK_DEBUG=1
export PORT=5001

# Start Flask server
echo "🚀 Starting Flask server on port 5001..."
python app.py