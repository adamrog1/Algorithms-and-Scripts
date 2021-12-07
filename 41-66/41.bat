@echo off
for /d %%x in (%cd%\*) do echo %%x >>%1
pause