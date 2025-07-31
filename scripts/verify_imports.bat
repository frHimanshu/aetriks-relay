@echo off
echo ========================================
echo Aetriks Import Verification Script
echo ========================================

echo [INFO] Checking Java files for import issues...

cd relay-server

echo [INFO] Checking KeyLogController.java...
findstr /n "import" src\main\java\com\aetriks\relay\controller\KeyLogController.java
echo.

echo [INFO] Checking KeyLogPayload.java...
findstr /n "package" src\main\java\com\aetriks\relay\model\KeyLogPayload.java
echo.

echo [INFO] Checking AetriksRelayApplication.java...
findstr /n "import" src\main\java\com\aetriks\relay\AetriksRelayApplication.java
echo.

echo [INFO] Import verification completed
echo [INFO] If you see any errors above, they need to be fixed
echo [INFO] Otherwise, the imports should be working correctly
pause 