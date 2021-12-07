@echo off
setlocal enabledelayedexpansion

:main
set inputFile=dane.txt
set outputFile=wyjscie.html
cls
call :tytul
call :opcje
set /p input=wybierz opcje:
if !input!==1 call :info
if !input!==2 call :compute
if !input!==3 call :backup
if !input!==4 call exit


:tytul
echo Adam Rogalski - projekt "Drapieznik-Ofiara"
exit /b
	
:opcje
echo	1. Informacje ogolne
echo	2. Wykonaj program
echo	3. Wykonaj kopie danych
echo	4. Wyjdz
exit /b
	
:info
cls
echo Program rozwiazuje nastepujacy problem:
echo	Na plaszczyznie, w punkcie Pd znajduje sie drapieznik, ktory w chwili t0 (mozemy
echo przyjac, że 𝑡0 = 0) dostrzegl ofiare znajdującą się w punkcie P0 i w tej samej chwili rozpoczal
echo jej poscig z predkoscia vd. Ofiara, rowniez w tej samej chwili, rozpoczyna ucieczkę po
echo pewnej prostej l0 z prędkością v0. Co pewien staly krok czasu delta t, drapieżnik spoglada,
echo w ktorym miejscu znajduje sie ofiara i koryguje swa trase poscigu (drapieżnik również
echo biegnie wzdluz prostej, jednak po kazdej korekcie, prosta ta może ulec zmianie).
echo Napisz program, ktory po zadaniu wspołrzednych punktow Pd i P0, prędkości Vd i V0,
echo parametrow prostej l0 oraz delta t, zwróci krzywe, po ktorych biegna drapieznik i ofiara (trasa
echo ucieczki ofiary jest prosta, a trasa pogoni – lamana). Warunkiem zakończenia poscigu jest
echo spelnienie jednego z warunkow: dogonienie ofiary lub zmeczenie sie drapieznika, co dzieje
echo sie po upływie pewnego zadanego czasu t (kolejny argument programu).
echo W drugiej częsci rozbuduj program w taki sposob, aby ofiara, równiez co delta t,
echo korygowała trase ucieczki, tak aby biec w kierunku najkorzystniejszym dla uciekającej ofiary
echo (wowczas obydwie trasy beda lamanymi i nie trzeba zadawac parametrow prostej l0).
echo .
echo Nacisnij ENTER aby wrocic do menu
pause > NUL
goto :main
:compute
cd "C:\Users\Adam\anaconda3\envs\pythonProject3"
kod.py

pause > NUL
goto :main
:backup
set imie=backup
if exist backup(
echo Backup już istnieje, przenieś lub usuń go aby kontynuowac
echo Wciśnij ENTER, ay wrócić do menu
pause > NUL
goto main
)
mkdir !name!
if exist !inputFile! copy !inputFile! !name!
if exist !outputFile! copy !outputFile! !name!
if exist style.css copy style.css !name!
echo.
echo Kopia zapasowa znajduje sie w folderze !name!
echo Wciśnij ENTER, aby wrócić do menu
pause > NUL
goto main
:exit
exit 0