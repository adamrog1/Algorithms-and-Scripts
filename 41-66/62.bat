@echo off 
set  str1="%~dp0"
echo tekst: %str1%
set str1=%str1:~1,-1%
echo %str1%
pause