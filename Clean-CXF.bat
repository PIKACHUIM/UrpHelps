rd /s /q Release\0.3.2
mkdir Release\0.3.2
xcopy /s /e /y  "Configs\" "Release\0.3.2\Configs\"
xcopy /s /e /y build\exe.win-amd64-3.9\ Release\0.3.2\
rd /s /q build