import tkinter as tk
import random

WINDOW_WIDTH = 220
WINDOW_HEIGHT = 120
INTERVAL = 500  # 0.5秒

root = tk.Tk()
root.title("Parent Window")

# 親ウィンドウを透明にする
root.attributes("-alpha", 0.0)

# 画面サイズ
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 親ウィンドウを画面全体にする
root.geometry(
    f"{screen_width}x{screen_height}+0+0"
)


def parent_closed():
    # 親ウィンドウを閉じても終了しない
    root.deiconify()


root.protocol("WM_DELETE_WINDOW", parent_closed)


def create_window():
    # ランダムな位置
    x = random.randint(
        0,
        screen_width - WINDOW_WIDTH
    )

    y = random.randint(
        0,
        screen_height - WINDOW_HEIGHT
    )

    # 小さいウィンドウ風パネル
    frame = tk.Frame(
        root,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        bg="white",
        bd=2,
        relief="raised"
    )

    frame.place(x=x, y=y)

    # タイトルバー
    title = tk.Label(
        frame,
        text="Staaaaaaaaaaaaaaaaaaaaaaaaaarrrrrrrrrrrrrrrrrrrrrrrr",
        bg="#dddddd",
        anchor="w"
    )

    title.place(
        x=0,
        y=0,
        width=WINDOW_WIDTH - 30,
        height=25
    )

    # 閉じるボタン
    close = tk.Button(
        frame,
        text="×",
        command=frame.destroy,
        bd=0
    )

    close.place(
        x=WINDOW_WIDTH - 30,
        y=0,
        width=30,
        height=25
    )

    # 内容
    label = tk.Label(
        frame,
        text="Staaaaaaaaaaaaaaaaaaaaaar",
        font=("Arial", 14),
        bg="white"
    )

    label.place(
        x=0,
        y=25,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT - 25
    )

    # 0.5秒後に次を生成
    root.after(INTERVAL, create_window)


# 0.5秒後に最初のウィンドウ
root.after(INTERVAL, create_window)

root.mainloop()
