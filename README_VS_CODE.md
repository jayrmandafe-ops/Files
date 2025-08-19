# Running Kutur ni Jean Admin Dashboard in VS Code

## Prerequisites

### Required Software
1. **Node.js** (v18 or higher)
   - Download from: https://nodejs.org/
   - Check version: `node --version`

2. **Python** (v3.11 or higher)
   - Download from: https://python.org/
   - Check version: `python --version`

3. **PostgreSQL** (v14 or higher)
   - Download from: https://postgresql.org/
   - Or use a cloud service like Neon Database

### VS Code Extensions
Install these VS Code extensions:
- **Python** (Microsoft)
- **TypeScript and JavaScript Language Features** (built-in)
- **ES7+ React/Redux/React-Native snippets**
- **Tailwind CSS IntelliSense**
- **PostgreSQL** (Chris Kolkman)

## Setup Instructions

### 1. Clone and Install Dependencies

```bash
# Clone the project (if from Git)
git clone <repository-url>
cd kutur-ni-jean-dashboard

# Install Node.js dependencies
npm install

# Install Python dependencies
pip install flask flask-cors psycopg2-binary python-dotenv
```

### 2. Database Setup

#### Option A: Local PostgreSQL
```bash
# Create database
createdb kutur_ni_jean

# Set environment variables in .env file:
DATABASE_URL=postgresql://username:password@localhost:5432/kutur_ni_jean
PGHOST=localhost
PGPORT=5432
PGUSER=your_username
PGPASSWORD=your_password
PGDATABASE=kutur_ni_jean
```

#### Option B: Neon Database (Recommended)
1. Sign up at https://neon.tech/
2. Create a new project
3. Copy the connection string to your `.env` file

### 3. Environment Configuration

Create a `.env` file in the root directory:
```env
# Database Configuration
DATABASE_URL=your_postgresql_connection_string
PGHOST=your_host
PGPORT=5432
PGUSER=your_username
PGPASSWORD=your_password
PGDATABASE=your_database_name

# Development Mode
NODE_ENV=development
```

### 4. Initialize Database Schema

Run the database migrations to create tables:
```bash
# This will create all necessary tables
python -c "
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Add your table creation SQL here
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# Create tables (you'll need to add the SQL schema)
# cur.execute('CREATE TABLE IF NOT EXISTS ...')

conn.commit()
conn.close()
"
```

## Running the Application

### Development Mode (Recommended)

#### Terminal 1 - Start Python Flask Backend:
```bash
cd server
python app.py
# Backend will run on http://localhost:5000
```

#### Terminal 2 - Start React Frontend:
```bash
npm run dev
# Frontend will run on http://localhost:5173
```

### VS Code Integration

#### 1. Python Debugging
Create `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/server/app.py",
            "env": {
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "1"
            },
            "console": "integratedTerminal"
        }
    ]
}
```

#### 2. TypeScript Configuration
The project includes `tsconfig.json` for proper TypeScript support.

#### 3. Recommended VS Code Settings
Create `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "typescript.preferences.importModuleSpecifier": "relative",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

## Project Structure

```
├── client/src/          # React TypeScript frontend
│   ├── components/      # Reusable UI components
│   ├── pages/          # Page components
│   └── lib/            # Utilities and helpers
├── server/             # Python Flask backend
│   ├── app.py         # Main Flask application
│   ├── routes.py      # API routes
│   └── db.py          # Database connections
├── shared/            # Shared TypeScript schemas
└── package.json       # Node.js dependencies
```

## Common Issues and Solutions

### 1. Database Connection Errors
- Verify PostgreSQL is running
- Check DATABASE_URL format
- Ensure database exists

### 2. Port Conflicts
- Backend uses port 5000
- Frontend uses port 5173
- Change ports in configuration if needed

### 3. Missing Dependencies
```bash
# Reinstall Node.js dependencies
rm -rf node_modules package-lock.json
npm install

# Reinstall Python dependencies
pip install -r requirements.txt
```

### 4. TypeScript Errors
- Ensure VS Code TypeScript version is up to date
- Restart TypeScript language server: Ctrl+Shift+P → "TypeScript: Restart TS Server"

## Development Workflow

1. Start both servers (Flask + React)
2. Make changes to frontend in `client/src/`
3. Make changes to backend in `server/`
4. Hot reload works for both frontend and backend
5. Access application at `http://localhost:5173`

## Production Deployment

For production, you'll need to:
1. Build the React frontend: `npm run build`
2. Configure Flask to serve static files
3. Set up proper environment variables
4. Use a production WSGI server like Gunicorn

## Need Help?

- Check the console logs in VS Code terminal
- Use VS Code debugger for both Python and TypeScript
- Verify environment variables are loaded correctly