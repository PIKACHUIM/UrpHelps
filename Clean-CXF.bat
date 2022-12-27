rd /s /q Release\0.4.0
mkdir Release\0.4.0
xcopy /s /e /y  "Configs\" "Release\0.4.0\Configs\"
xcopy /s /e /y build\exe.win-amd64-3.9\ Release\0.4.0\
rd /s /q build