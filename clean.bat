@echo off
title CASPER Dev Cleaner
echo [casper cleaner] Cleaning, please wait!
del /f framework\*.pyc >nul
echo [casper cleaner] Cleaning done
echo [casper cleaner] Press any key o exit...
pause >nul