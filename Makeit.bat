@echo off
title Ƥ????Python?????ű?
mode con cols=80 lines=30
color 4f
F:\Venvs\URP-Helper\Scripts\pyinstaller.exe -i icon.ico -F urps_main.PY
TIMEOUT /T 3
EXIT