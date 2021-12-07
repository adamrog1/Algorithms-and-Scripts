@echo off
if %1==/h goto :print_help
if %1==/a goto :del_reg
:print_help
po wpisaniu przełącznika "/a" program usunie wpisy w edytorze rejestru odpowiedzialne za automatyczne uruchamianie programow przy starcie systemu
goto :eof
set /s progra=wpisz nazwe proramu ktory chcesz usunac z autostartu
del C:\Users\Adam\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\%program%
goto :eof
:del_reg
reg del Komputer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
pause