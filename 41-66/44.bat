@echo off
set /p var1=Podaj typ pliku
if not exist *%var1% goto :linia
for /d %%x in (%cd%) do del *%var1%
:linia
echo nie ma takiego typu plikow
pause