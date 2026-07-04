@echo off
cd /d %~dp0
echo ==============================================
echo   ollama-lite 启动中...
echo   如果报错，请确保已安装依赖：pip install requests
echo ==============================================
echo.

start /b py simple_chat.py

pause