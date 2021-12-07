@echo off
call "37.bat"

for /r %var1% %%x in (*.eps) do (echo %%x >> %var1%\listjpg.txt)
pause