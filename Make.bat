@echo off
title 皮卡丘Python编译脚本
mode con cols=80 lines=30
color 4f
%~dp0venv\Scripts\pyinstaller.exe -i icon.ico -F urps_main.PY
TIMEOUT /T 3
EXIT