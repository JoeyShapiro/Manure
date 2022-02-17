@echo off

set max=1000000000
set min=1000000

dir /s/b *.exe > out.txt

for /f %%i in (out.txt) do (
    if %%~zi LSS %max% if %%~zi GTR %min% (
        echo %%i %%~zi
    )
)

DEL out.txt