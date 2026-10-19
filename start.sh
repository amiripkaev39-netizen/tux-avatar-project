#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

echo "================================"
echo "  Random Tux Launcher"
echo "================================"
echo

# Ищем Python
if command -v python3 >/dev/null 2>&1; then
    PY=python3
elif command -v python >/dev/null 2>&1; then
    PY=python
else
    echo "[!] Python не найден."
    echo "Arch:    sudo pacman -S python python-pip tk"
    echo "Debian:  sudo apt install python3 python3-pip python3-tk"
    exit 1
fi

echo "[*] Использую: $PY"
echo "[*] Запускаю Random Tux..."
echo

exec "$PY" tux_app.py
