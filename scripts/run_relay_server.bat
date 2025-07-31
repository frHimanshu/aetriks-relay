@echo off
echo ========================================
echo Aetriks Relay Server Runner
echo ========================================

REM Check if JAR exists
if not exist "relay-server\target\aetriks-relay-1.0.0.jar" (
    echo [ERROR] JAR file not found. Please build the project first.
    echo [INFO] Run: scripts\build_relay_server.bat
    pause
    exit /b 1
)

echo [INFO] Starting Aetriks Relay Server...
echo [INFO] Server will be available at: http://localhost:8080
echo [INFO] Press Ctrl+C to stop the server
echo.

cd relay-server
java -jar target/aetriks-relay-1.0.0.jar

pause 