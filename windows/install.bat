@echo off
:: Set script to global windows startup
:: set startupdir="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
:: Set script to current user's windows startup
set startupdir="%appdata%\Microsoft\Windows\Start Menu\Programs\Startup"

winget install Python -s msstore
::winget import .\winget.json

python -m pip install --upgrade pip
python -m pip install watchdog
python .\install.py %startupdir%
COPY .\onboot.bat %startupdir%