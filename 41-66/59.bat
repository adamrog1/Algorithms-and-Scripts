@echo off 
set /p str=<tekst.txt
echo %str%
set str= %str:a=%
echo %str%
pause