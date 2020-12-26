@echo off
color 3f
title Git版本提交工具
mode con lines=20 cols=60
echo.
echo.
echo.
echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo             ▇                                ▇
echo             ▇       ***正在申请权限***       ▇
echo             ▇                                ▇
echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo.
echo.
echo          ***如果提示授权，请点击【是】***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
cls
echo.
echo.
echo.
echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo             ▇                                ▇
echo             ▇       ***正在准备程序***       ▇
echo             ▇                                ▇
echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
git add .
git commit -m "Updated"%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
git push
timeout /t 5