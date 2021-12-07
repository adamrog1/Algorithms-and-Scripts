@echo off
set /p var1=Podaj sciezke
for /d %%x in (%var1%\*) do del *.tmp
pause