@echo off 
set /p lok1=lokalizacja 1
set /p str1=<%lok1%
set /p lok2=lokalizacja 2
set /p str2=<%lok2%
echo tekst numer 1: %str1%
echo tekst numer 2: %str2%
set str3=%str1% %str2%
echo %str3%
pause