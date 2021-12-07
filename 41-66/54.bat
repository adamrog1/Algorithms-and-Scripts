@echo off

set month=%1
set nbr=0
for %%x in (Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec) do (
set /a nbr+=1
if %%x == %1 goto :finis
)
:finis
echo The %1 is month number %nbr%
pause