@echo off 
:poczatek
cls
echo ===============
echo Menu
echo ===============
echo.
echo 1) Zrob obiad
echo 2) Zaparz se kawke
echo 3) Pisz skrypty
echo 4) Wyjdz
echo.
set /p opcja=wybierz:
if %opcja%==1 goto opcja1
if %opcja%==2 goto opcja2
if %opcja%==3 goto opcja3
if %opcja%==4 exit
goto zly_wybor
:opcja1
cls
echo wybrano zrobienie obiadku
pause
goto poczatek
:opcja2
cls
echo wybrano parzenie kawki
pause
goto poczatek
:opcja3
cls
echo wybrano Pisanie skryptow
pause
goto poczatek
:zly_wybor
echo Opcja nie zostala wprowadzona do programu wybierz inna albo poczekaj na update :)
pause
goto poczatek