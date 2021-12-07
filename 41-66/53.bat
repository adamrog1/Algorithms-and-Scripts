@echo off
set "HEX="
set /p liczba=Podaj liczbe
set /A DEC=0x%liczba%
echo Forma dziesietna  %liczba% to %DEC%.
pause