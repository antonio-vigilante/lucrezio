@echo off
S
echo @echo off > compila.bat
echo python -m sphinx.cmd.build -b html source build >> compila.bat
echo echo. >> compila.bat
echo echo --- Compilazione completata! --- >> compila.bat
echo pause >> compila.bat
type compila.bat
