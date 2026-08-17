import tkinter as tk
import random
import subprocess

WINDOW_WIDTH = 220
WINDOW_HEIGHT = 120
INTERVAL = 500  # 0.5秒

root = tk.Tk()
root.withdraw()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

windows = []
window_count = 0


def move_window(window, title, x, y):
    """
    wmctrlを使ってX11/XWaylandウィンドウを
    指定した位置へ移動する
    """

    # Tkinter側でも位置を指定
    window.geometry(
        f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}"
    )

    # ウィンドウを表示
    window.update_idletasks()

    # wmctrlで強制移動
    try:
        subprocess.run(
            [
                "wmctrl",
                "-r",
                title,
                "-e",
                f"0,{x},{y},-1,-1"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except FileNotFoundError:
        print("wmctrl がインストールされていません")


def create_window():
    global window_count

    window_count += 1

    # ランダムな位置
    x = random.randint(
        0,
        max(0, screen_width - WINDOW_WIDTH)
    )

    y = random.randint(
        0,
        max(0, screen_height - WINDOW_HEIGHT)
    )

    # ウィンドウごとに固有のタイトル
    title = f"StarWindow_{window_count}"

    window = tk.Toplevel(root)

    window.title(title)

    window.resizable(False, False)

    # 最前面
    window.attributes("-topmost", True)

    # サイズだけ指定
    window.geometry(
        f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
    )

    # 内容
    frame = tk.Frame(
        window,
        bg="white",
        bd=2,
        relief="raised"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    # タイトルバー風
    title_label = tk.Label(
        frame,
        text="Star",
        bg="#dddddd",
        anchor="w"
    )

    title_label.place(
        x=0,
        y=0,
        width=WINDOW_WIDTH - 30,
        height=25
    )

    # 閉じるボタン
    close = tk.Button(
        frame,
        text="×",
        command=window.destroy,
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
        text="Star",
        font=("Arial", 14),
        bg="white"
    )

    label.place(
        x=0,
        y=25,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT - 25
    )

    windows.append(window)

    # ウィンドウを実際に表示してから移動
    window.update()

    # wmctrlでランダム位置へ移動
    move_window(
        window,
        title,
        x,
        y
    )

    # 少し遅れてもう一度移動
    # ウィンドウマネージャーに位置を
    # 上書きされた場合への対策
    root.after(
        100,
        lambda: move_window(
            window,
            title,
            x,
            y
        )
    )

    # 次のウィンドウ
    root.after(
        INTERVAL,
        create_window
    )


# 最初のウィンドウ
root.after(
    INTERVAL,
    create_window
)

root.mainloop()
