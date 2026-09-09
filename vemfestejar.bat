@echo off
NET FILE >nul 2>&1
if '%errorlevel%' == '0' ( goto gotAdmin ) else ( goto getAdmin )
:getAdmin
if '%1'=='ELEV' (shift & goto gotAdmin)
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "ELEV", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B
:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
cd /d "%~dp0"
@echo off

cd /d "%~dp0"

start "" /B cmd /c "timeout /t 5 /nobreak >nul && start chrome http://127.0.0.1:8000/clientes"

uv run uvicorn main:app --reload --port 8000

pause
