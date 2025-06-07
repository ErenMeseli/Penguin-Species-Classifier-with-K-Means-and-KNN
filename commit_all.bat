@echo off
cd /d %~dp0
echo Starting commit process...

for /r %%f in (*) do (
    git add "%%f"
    git commit -m "Add files via upload" >nul 2>&1
)

git push origin main

echo.
echo ✅ All files committed and pushed!
pause
