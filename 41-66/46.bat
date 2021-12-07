@echo off
set /p var1=podaj liczbe do ktorej chcesz wypiszac
set var2=licznik
:liczba
set /a licznik=%licznik%+1
if %licznik%==%var1% goto :eof 
else echo %licznik%>>%1
pause