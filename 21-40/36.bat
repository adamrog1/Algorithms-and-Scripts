@echo off
set /p var1=wybierz katalog z ktorego chcesz skopiowac
set /p var=wybierz katalog do ktorego mam skopiowac
for  %%x in (%var1%*.txt) do (copy *.txt %var%)
pause