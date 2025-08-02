@echo off
chcp 65001 > nul

call conda activate photobooth
pip install -r requirements.txt
echo Done install requirements
pyinstaller --onefile --icon=statics\photobooth.ico --windowed launcher.py

set CURR_DIR=%~dp0
set TARGET=%CURR_DIR%\photobooth.exe
set SHORTCUT=%USERPROFILE%\Desktop\photobooth.lnk

powershell ^
  "$s=(New-Object -COM WScript.Shell).CreateShortcut('%SHORTCUT%');" ^
  "$s.TargetPath='%TARGET%';" ^
  "$s.WorkingDirectory='%CURR_DIR%';" ^
  "$s.Save()"

echo ✅ CreateShortcut = %CURR_DIR%


echo ALL Done.
pause
