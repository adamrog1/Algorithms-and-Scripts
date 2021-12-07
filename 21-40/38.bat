@echo off
set /p var1=podaj scierze plku w ktorym chcesz zapisac liczby
for  %%x in (1,1,%1) do (echo %%x >> %var1%)
pause