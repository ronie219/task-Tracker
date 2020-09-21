@echo off
if "%1" equ "Restarted" goto %1

:again
echo N|start "" /WAIT cmd.exe /C "%~F0" Restarted > NUL
goto :again

:Restarted
cd D:\task\task
:loop
echo Runnng the server...
py manage.py runserver abiswas:8080
timeout /T 1 > NUL
goto loop