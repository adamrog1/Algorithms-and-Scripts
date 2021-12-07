@echo off 
set /p str=tekst numer 1
set /p str2= tekst number 2
echo tekst numer 1: %str%
echo tekst numer 2: %str2%
set str3=%str% %str2%
echo %str3%
pause