@ECHO OFF

:menuLOOP

for /f "tokens=1,2,* delims=_ " %%A in ('"findstr /b /c:":menu_" "%~f0""') do echo.  %%B  %%C
set choice=
echo.&set /p choice=Wybierz opcje lub enter aby wyjsc: ||GOTO:EOF
echo.&call:menu_%choice%
GOTO:menuLOOP

:menu_1   Opcja 1
echo.Wybrales opcje 1
GOTO:EOF

:menu_2   Opcja 2
echo.Wybrales opcje 2
GOTO:EOF
