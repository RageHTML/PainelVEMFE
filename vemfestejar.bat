@echo off

cd /d "%~dp0"

start "" /B cmd /c "timeout /t 3 /nobreak >nul && start chrome http://127.0.0.1:8000/clientes"

uv run fastapi run main.py --port 8000

pause