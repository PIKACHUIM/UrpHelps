@echo off
color 3f
title Git�汾ǿ��ͬ������
mode con lines=20 cols=60
echo.
echo.
echo.
echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo             �~                                �~
echo             �~       ***��������Ȩ��***       �~
echo             �~                                �~
echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
echo          ***�����ʾ��Ȩ���������ǡ�***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
cls
echo.
echo.
echo.
echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo             �~                                �~
echo             �~       ***���ڵȴ�ȷ��***       �~
echo             �~                                �~
echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
set Vbscript=Msgbox("��ȷ��Ҫ�������ظ��������б����޸Ķ�����ʧ������",1,"���ݰ�ȫȷ��")
for /f "Delims=" %%a in ('MsHta VBScript:Execute("CreateObject(""Scripting.Filesystemobject"").GetStandardStream(1).Write(%Vbscript:"=""%)"^)(Close^)') do Set "MsHtaReturnValue=%%a"
set ReturnValue1=ȷ��
set ReturnValue2=ȡ����رմ���
if %MsHtaReturnValue% == 1 (
    echo.
    echo.
    echo -------------------�����������ݣ�ǿ��ͬ��-------------------
    timeout /t 1 >nul
    cls
    color cf
    echo.
    echo.
    echo.
    echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
    echo             �~                                �~
    echo             �~       ***�û���������***       �~
    echo             �~                                �~
    echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
    echo.
    echo.
    echo --------------ʮ����Զ���ʼ��ȡ�������Ͻǹر�--------------
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
    echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
    echo             �~                                �~
    echo             �~       ***�û�����ͬ��***       �~
    echo             �~                                �~
    echo             �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
    echo.
    echo.
    echo -------------------�û�����ͬ����ͬ����ֹ-------------------
    timeout /t 3  >nul
)
timeout /t 5

