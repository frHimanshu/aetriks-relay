@echo off
echo ========================================
echo Aetriks Relay Server Compilation Script
echo ========================================

echo [INFO] Checking for Java installation...
java -version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Java is not installed or not in PATH
    echo [INFO] Please install Java 17 or higher
    pause
    exit /b 1
)

echo [INFO] Checking for Maven installation...
mvn -version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Maven is not installed or not in PATH
    echo [INFO] Attempting to use Maven wrapper if available...
    
    cd relay-server
    
    if exist "mvnw.cmd" (
        echo [INFO] Using Maven wrapper...
        call mvnw.cmd clean compile
    ) else (
        echo [ERROR] Maven wrapper not found
        echo [INFO] Please install Maven or use an IDE to compile the project
        echo [INFO] Required dependencies:
        echo   - Java 17+
        echo   - Maven 3.6+
        echo   - Spring Boot 3.2.0
        pause
        exit /b 1
    )
) else (
    echo [INFO] Using installed Maven...
    cd relay-server
    mvn clean compile
)

if errorlevel 1 (
    echo [ERROR] Compilation failed
    echo [INFO] Please check the error messages above
    pause
    exit /b 1
)

echo [SUCCESS] Compilation completed successfully!
echo [INFO] The relay server is ready to run
echo [INFO] To run: mvn spring-boot:run (or use the run script)
pause 