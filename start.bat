@echo off
chcp 65001 >nul
title Random Tux

echo ================================
echo   Random Tux Launcher
echo ================================
echo.

REM Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python не найден.
    echo.
    echo Скачай и установи Python с https://python.org
    echo При установке поставь галочку "Add Python to PATH".
    echo.
    pause
    exit /b 1
)

REM Проверка pip
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [*] pip не найден, устанавливаю...
    python -m ensurepip --upgrade
)

echo [*] Запускаю Random Tux...
echo.
python "%~dp0tux_app.py"

if errorlevel 1 (
    echo.
    echo [!] Что-то пошло не так.
    pause
)
