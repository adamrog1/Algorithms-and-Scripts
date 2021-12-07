@echo off
set /p var1=podaj liczbe do ktorej chcesz wypiszac
for /l %%x in (1,1,%var1%) do (echo %%x >> %1)
pause