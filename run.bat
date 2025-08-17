@echo off
echo ========================================
echo    Daggerheart Tracker - Modern Edition
echo ========================================
echo.
echo Iniciando aplicacion...
echo.

cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    echo Usando entorno virtual...
    .venv\Scripts\python.exe main.py
) else (
    echo Usando Python del sistema...
    python main.py
)

echo.
echo Aplicacion cerrada.
pause
