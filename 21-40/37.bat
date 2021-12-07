@echo off
set /p var1=wybierz katalog w ktorym chcesz konwertowac
for /r %var1% %%x in (*.jpg) do (ren %%x *.eps)
for /r %var1% %%x in (*.png) do (ren %%x *.eps)
pause