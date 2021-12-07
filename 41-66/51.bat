@echo off
setlocal
set /p var3=wprowadz liczbe pierwsza
set /p var4=wprowadz liczbe druga
set /a var1=%var3%
set /a var2=%var4%
set /A a=%var1%+%var2%
set /A b=%var1%-%var2%
set /A c=%var1%*%var2%
set /A d=%var1%/%var2%
echo %a%
echo %b%
echo %c%
echo %d%
pause