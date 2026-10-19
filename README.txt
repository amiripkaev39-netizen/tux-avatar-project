========================================
  Random Tux — случайные пингвины Tux
========================================

Программа показывает случайного пингвина Tux.
Нажми кнопку "Другой Tux!" или клавишу Пробел,
чтобы получить нового пингвина.


--- WINDOWS ---

1. Установи Python с https://python.org
   ВАЖНО: при установке поставь галочку
   "Add Python to PATH".

2. Двойной клик по start.bat

Готово! Программа сама установит Pillow.


--- LINUX / macOS ---

1. Установи Python и Tkinter:

   Arch:     sudo pacman -S python python-pip tk
   Debian:   sudo apt install python3 python3-pip python3-tk
   Fedora:   sudo dnf install python3 python3-pip python3-tkinter
   macOS:    brew install python-tk

2. Запусти:

   ./start.sh

   (если не запускается, сначала: chmod +x start.sh)


--- ЧТО ДЕЛАЕТ ПРОГРАММА ---

- Автоматически ставит библиотеку Pillow (нужна для картинок).
- Читает картинки из папки images/.
- Показывает их в случайном порядке.


--- ЕСЛИ ЧТО-ТО НЕ РАБОТАЕТ ---

- "Python не найден"  → переустанови Python с галочкой "Add to PATH"
- Пустое окно          → проверь, что в папке images/ есть картинки
- Ошибка Pillow       → установи вручную:  pip install Pillow

