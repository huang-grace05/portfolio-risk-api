# Portfolio Risk Analytics API

A Python project for analyzing historical portfolio performance and risk.

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Git

## Project Structure

- `app/main.py` — application setup and API endpoints
- `app/__init__.py` — marks the app folder as a Python package
- `requirements.txt` — Python dependencies
- `.gitignore` — files excluded from Git
- `README.md` — project documentation

## Setup

Run these commands from the `portfolio-risk-api` folder.

### 1. Create and activate a virtual environment

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the development server

```bash
fastapi dev app/main.py
```

Leave the terminal running. Press `Ctrl+C` to stop the server.

## API Endpoints

### GET /health

Checks whether the application responds.

Open: http://127.0.0.1:8000/health

### Interactive Documentation

Open http://127.0.0.1:8000/docs to explore and try the API.

## Planned Features

- Import historical stock prices from CSV files
- Store prices and holdings in PostgreSQL
- Calculate portfolio returns, volatility, Sharpe ratio, and maximum drawdown
- Test calculations and API behavior with pytest
- Build a Streamlit dashboard
- Package the application with Docker Compose

## Learning Resources

- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Python: Virtual Environments](https://docs.python.org/3.12/tutorial/venv.html)
- [Git: Getting Started](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)