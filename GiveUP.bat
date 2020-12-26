@echo off
color 3f
title Git版本强制同步工具
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
echo             ▇       ***正在等待确认***       ▇
echo             ▇                                ▇
echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
set Vbscript=Msgbox("你确定要放弃本地更改吗？所有本地修改都将丢失！！！",1,"数据安全确认")
for /f "Delims=" %%a in ('MsHta VBScript:Execute("CreateObject(""Scripting.Filesystemobject"").GetStandardStream(1).Write(%Vbscript:"=""%)"^)(Close^)') do Set "MsHtaReturnValue=%%a"
set ReturnValue1=确定
set ReturnValue2=取消或关闭窗口
if %MsHtaReturnValue% == 1 (
    echo.
    echo.
    echo -------------------丢弃本地数据，强制同步-------------------
    timeout /t 1 >nul
    cls
    color cf
    echo.
    echo.
    echo.
    echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
    echo             ▇                                ▇
    echo             ▇       ***用户丢弃数据***       ▇
    echo             ▇                                ▇
    echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
    echo.
    echo.
    echo --------------十秒后自动开始，取消请右上角关闭--------------
    echo.
    echo.
    timeout /t 9
    echo.
    echo.
    cls
    git fetch --all
    git reset --hard origin/master
    git pull
    timeout /t 3 >nul
) else (
    cls
    color 4f
    echo.
    echo.
    echo.
    echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
    echo             ▇                                ▇
    echo             ▇       ***用户放弃同步***       ▇
    echo             ▇                                ▇
    echo             ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
    echo.
    echo.
    echo -------------------用户放弃同步，同步中止-------------------
    timeout /t 3  >nul
)
timeout /t 5

