@ echo off
echo Zmienna path z wartosciami systemowymi :
echo %path%
echo . . . . .
Setlocal
set path=”c:\Program_Files ”
echo Zmienna path po przyjeciu zadanej wartosci :
echo %path%
echo . . . . .
Endlocal
echo Zmienne systemowe poza sekcja setlocal endlocal :
echo %path%
echo . . . . .
pause