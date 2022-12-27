rd /s /q Release\0.3.3
mkdir Release\0.3.3
xcopy /s /e /y  "Configs\" "Release\0.3.3\Configs\"
xcopy /s /e /y build\exe.win-amd64-3.9\ Release\0.3.3\
rd /s /q build