@echo off
color 3f
title Git信息设置工具
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
git config --global user.email "pikachuim@qq.com"
git config --global user.name "皮卡丘"
timeout /t 5