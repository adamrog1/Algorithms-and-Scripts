@echo off
call "30.bat" 
echo Wywowal program zmiany tytulu okna
set /p var=podaj sciezke katalogu:
set /p var2=podaj sciezke katalogu do zapisu:

dir %var% > %var2%.txt
pause