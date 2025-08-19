from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime, timedelta
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('PGHOST'),
            database=os.environ.get('PGDATABASE'),
            user=os.environ.get('PGUSER'),
            password=os.environ.get('PGPASSWORD'),
            port=os.environ.get('PGPORT', 5432)
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

# Dashboard API
@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Get dashboard metrics (mock data for now - replace with real queries)
        dashboard_data = {
            'dailySales': 0,
            'dailyCustomers': 0,
            'pendingOrders': 0,
            'completedOrders': 0,
            'salesData': [
                {'date': '2024-01-01', 'sales': 1200, 'orders': 8},
                {'date': '2024-01-02', 'sales': 1800, 'orders': 12},
                {'date': '2024-01-03', 'sales': 1600, 'orders': 10},
                {'date': '2024-01-04', 'sales': 2200, 'orders': 15},
                {'date': '2024-01-05', 'sales': 1900, 'orders': 13},
                {'date': '2024-01-06', 'sales': 2400, 'orders': 18},
                {'date': '2024-01-07', 'sales': 2100, 'orders': 16}
            ],
            'topGarments': [
                {'name': 'Barong Tagalog Premium', 'sales': 45, 'revenue': 67500},
                {'name': 'Filipiniana Gown Classic', 'sales': 32, 'revenue': 96000},
                {'name': 'Modern Terno', 'sales': 28, 'revenue': 84000},
                {'name': 'Traditional Maria Clara', 'sales': 25, 'revenue': 62500}
            ],
            'recentOrders': [
                {
                    'id': 'ORD-001',
                    'customer': 'Maria Santos',
                    'garment': 'Filipiniana Gown',
                    'status': 'In Progress',
                    'amount': 3500,
                    'date': '2024-01-15'
                },
                {
                    'id': 'ORD-002',
                    'customer': 'Juan Dela Cruz',
                    'garment': 'Barong Tagalog',
                    'status': 'Completed',
                    'amount': 1500,
                    'date': '2024-01-14'
                }
            ],
            'upcomingSchedule': [
                {
                    'id': 'SCH-001',
                    'type': 'Fitting',
                    'customer': 'Ana Rodriguez',
                    'garment': 'Wedding Gown',
                    'time': '10:00 AM',
                    'date': '2024-01-16'
                },
                {
                    'id': 'SCH-002',
                    'type': 'Pickup',
                    'customer': 'Carlos Lopez',
                    'garment': 'Barong Set',
                    'time': '2:00 PM',
                    'date': '2024-01-16'
                }
            ]
        }
        
        cursor.close()
        conn.close()
        
        return jsonify(dashboard_data)
    except Exception as e:
        print(f"Dashboard API error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Orders API
@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify([])

# Customers API
@app.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify([])

# Schedule API
@app.route('/api/schedules', methods=['GET'])
def get_schedules():
    return jsonify([])

# Sales API
@app.route('/api/sales', methods=['GET'])
def get_sales():
    return jsonify([])

# Feedback API
@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    return jsonify([])

# Fittings API
@app.route('/api/fittings', methods=['GET'])
def get_fittings():
    return jsonify([])

# Couture API
@app.route('/api/couture', methods=['GET'])
def get_couture():
    return jsonify([])

# Health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)