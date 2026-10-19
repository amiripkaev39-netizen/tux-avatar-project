#!/usr/bin/env python3
"""Random Tux — показывает случайных пингвинов Tux."""

import os
import sys
import subprocess
import random
import tkinter as tk

# --- Автоустановка Pillow ---
def ensure_pillow():
    try:
        import PIL  # noqa
    except ImportError:
        print("Pillow не найден, устанавливаю...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        except Exception as e:
            print(f"Не удалось установить Pillow автоматически: {e}")
            print("Установи вручную:  pip install Pillow")
            sys.exit(1)

ensure_pillow()

from PIL import Image, ImageTk

# Папка images рядом со скриптом
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join(BASE_DIR, "images")


class TuxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Tux")
        self.root.geometry("420x500")
        self.root.configure(bg="#2b2b2b")

        self.image_files = self.load_images()

        if not self.image_files:
            tk.Label(
                root,
                text=f"Не найдено картинок в папке:\n{IMAGE_FOLDER}",
                font=("Arial", 11),
                bg="#2b2b2b", fg="white", justify="center"
            ).pack(expand=True)
            return

        print(f"Загружено картинок: {len(self.image_files)}")

        self.image_label = tk.Label(root, bg="#2b2b2b")
        self.image_label.pack(expand=True, pady=15)

        self.name_label = tk.Label(
            root, text="", font=("Arial", 11, "bold"),
            bg="#2b2b2b", fg="#8bd450"
        )
        self.name_label.pack()

        tk.Button(
            root, text="Другой Tux!",
            command=self.show_random,
            font=("Arial", 12),
            bg="#8bd450", fg="black",
            activebackground="#6fae3f",
            relief="flat", padx=20, pady=8
        ).pack(pady=15)

        root.bind("<space>", lambda e: self.show_random())
        root.bind("<Return>", lambda e: self.show_random())

        self.show_random()

    def load_images(self):
        if not os.path.isdir(IMAGE_FOLDER):
            return []
        exts = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
        return [
            os.path.join(IMAGE_FOLDER, f)
            for f in os.listdir(IMAGE_FOLDER)
            if f.lower().endswith(exts)
        ]

    def show_random(self):
        if not self.image_files:
            return
        path = random.choice(self.image_files)
        try:
            img = Image.open(path).convert("RGBA")
            img.thumbnail((380, 380), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
            self.name_label.configure(text=os.path.basename(path))
        except Exception as e:
            print(f"Ошибка загрузки {path}: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TuxApp(root)
    root.mainloop()
