cd /d "C:\Users\w\spyder_workspace_W"
"C:\Program Files\Git\bin\git.exe" fetch
"C:\Program Files\Git\bin\git.exe" diff HEAD origin/master --exit-code > nul 2>&1
if errorlevel 1 (
    echo 有未合併的更改，請先處理。
    pause
    exit /b
)
"C:\Program Files\Git\bin\git.exe" add .
"C:\Program Files\Git\bin\git.exe" commit -m "Regularly Updated"
"C:\Program Files\Git\bin\git.exe" push