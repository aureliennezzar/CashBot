@echo off
:ins_modules
mode 75,12
cls
echo Voulez-vous installer les modules Python pour Cash Bot ? (o/n)
echo Cela va prendre quelques minutes...
batbox /k
if %errorlevel%==111 (goto :ins_modules2)
if %errorlevel%==110 (goto :sett)
goto :ins_modules
:ins_modules2
cls
echo Installation. (requests) 10 %%%
echo.
pip install requests
cls
echo Installation.. (PyQt5) 20 %%%
echo.
pip install PyQt5
cls
echo Installation... (Pillow) 40 %%%
echo.
pip install Pillow
cls
echo Installation. (numpy) 50 %%%
echo.
pip install numpy
cls
echo Installation.. (beautifulsoup4) 60 %%%
echo.
pip install beautifulsoup4
cls
echo Installation... (opencv-python) 80 %%%
echo.
pip install opencv-python
cls
echo Installation. (regex) 90 %%%
echo.
pip install regex
cls
echo Installation.. (pytesseract) 100 %%%
echo.
pip install pytesseract
:ins_m_fin
cls
echo Il ne manque plus que le module Tkinter qui se télécharge sur le site Activestate.com
echo ActiveTcl 8.5 instellera toute les fonctionnalités requises pour CashBot (sous windows)
echo.
echo Lancer le telechargement sur Google Chrome ? (o/n)
batbox /k
if %errorlevel%==111 (goto :ins_m_fin2)
if %errorlevel%==110 (exit)
goto :ins_m_fin
:ins_m_fin2
start chrome.exe https://www.activestate.com/activetcl/downloads/thank-you?dl=http://downloads.activestate.com/ActiveTcl/releases/8.5.18.0/ActiveTcl8.5.18.0.298892-win32-x86_64-threaded.exe
cls
echo A vous de finir l'installation Ciao !
batbox /w 500
exit