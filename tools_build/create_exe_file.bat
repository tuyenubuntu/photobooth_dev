@echo off
chcp 65001 > nul

call conda activate train
pyinstaller --onefile --icon=..\statics\photobooth.ico launcher.py



set SOURCE_EXE=dist\launcher.exe
set DEST_FOLDER=..
set DEST_EXE=%DEST_FOLDER%\photobooth.exe
echo Done 1
copy "%SOURCE_EXE%" "%DEST_EXE%" /Y


set CURR_DIR=%~dp0..
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


 pause