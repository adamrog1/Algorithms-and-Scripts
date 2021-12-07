@echo off

set /p month=<tekst.txt
set nbr=0
for %%x in (Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec) do (
set /a nbr+=1
if %%x == %month% goto :finish
)
:finish
echo The %month% is month number %nbr%
pause