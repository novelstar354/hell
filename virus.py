import tkinter as tk
import random

MAX_REOPEN = 2
reopen_count = 0

# 使用文字
chars = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "あいうえおかきくけこさしすせそ"
    "たちつてとなにぬねのはひふへほ"
    "まみむめもやゆよらりるれろわをん"
    "アイウエオカキクケコサシスセソ"
    "タチツテトナニヌネノハヒフヘホ"
    "マミムメモヤユヨラリルレロワヲン"
)

# ランダム文字列生成
def generate_random_line(length=120):
    return "".join(random.choice(chars) for _ in range(length))


def create_window():
    global reopen_count

    root = tk.Tk()
    root.title("STAR")

    # フルスクリーン
    root.attributes("-fullscreen", True)

    # 背景
    root.configure(bg="red")

    # 一番上だけSTAR
    lines = ["STAR CAUTION!!" * 20]

    # 残りをランダム生成
    for _ in range(9):
        lines.append(generate_random_line())

    # テキスト化
    random_text = "\n".join(lines)

    label = tk.Label(
        root,
        text=random_text,
        font=("Arial", 42, "bold"),
        fg="yellow",
        bg="red",
        justify="center"
    )

    label.place(relx=0.5, rely=0.5, anchor="center")

    # 閉じる処理
    def reopen():
        global reopen_count

        root.destroy()

        reopen_count += 1

        # 5回まで復活
        if reopen_count <= MAX_REOPEN:
            create_window()

    # ESCキー
    root.bind("<Escape>", lambda e: reopen())

    # ×ボタン
    root.protocol("WM_DELETE_WINDOW", reopen)

    root.mainloop()


create_window()
