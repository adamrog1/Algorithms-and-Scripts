@echo off 
set /p scierzka=podaj scierzke pliku tekstowego
set /p str=<%scierzka%
echo tekst przed zmiana: %str%
set /p co=co zmienic
set /p naco=na co zmienic
call set strkoniec=%%str:%co%=%naco%%%
echo %strkoniec%
set /p gdzie=gdzie zapisac zmiane ?:
echo strkoniec>>%gdzie%
pause