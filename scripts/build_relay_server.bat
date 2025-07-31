@echo off
echo ========================================
echo Aetriks Relay Server Build Script
echo ========================================

REM Check if Java is installed
java -version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Java is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if Maven is available
mvn --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Maven is not available
    pause
    exit /b 1
)

echo [INFO] Building relay server...
cd relay-server
mvn clean install

if errorlevel 1 (
    echo [ERROR] Build failed
    pause
    exit /b 1
)

echo [SUCCESS] Build completed!
echo [INFO] JAR location: relay-server/target/aetriks-relay-1.0.0.jar
echo [INFO] To run: java -jar relay-server/target/aetriks-relay-1.0.0.jar
pause 