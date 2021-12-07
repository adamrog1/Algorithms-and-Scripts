@echo off 
set sciezka=%1
set /p roz=na jakie rozszerzenie zamienic
echo %sciezka%
cd %sciezka%
ren *.txt *%roz%
set /p wybor= czy chcesz skopiowac wszyskie zamienione pliki (jesli tak to wprowadz "t")
if not %wybor%==t (goto :etykieta2) ELSE goto :etykieta
:etykieta
set /p data=Podaj date plikow
set /p miejsce=Podaj do jakiego katalogu skopiowac te pliki
copy %sciezka% %miejsce% /d%data%
echo koniec
goto :eof
pause
:etykieta2
echo koniec
pause