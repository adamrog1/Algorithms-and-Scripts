@echo off
set /p var1=Podaj sciezke
for /d %%x in (%cd%\*) do del *.tmp
pause