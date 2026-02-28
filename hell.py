SCREEN_HEIGHT = 160
SCREEN_WIDTH = 160
print("破壊", SCREEN_HEIGHT)
import tkinter as tk
window = tk.Tk()
window.title("shine")
window.geometry("400x400")
def close_window(event):
    window.destroy()
window.bind("<Escape>",close_window)
window.mainloop()
print("destroy")
for i in range(9):
    print(i)
    print("なぜウィンドウを閉じた。")
    print("もう", i, "回目だぞ。")
    match i:
        case 1:
            print("1回目\n")
        case 2:
            print("2回目\n")
        case 3:
            print("3回目\n")
        case 4:
            print("4回目\n")
        case 5:
            print("5回目\n")
        case 6:
            print("6回目\n")
        case 7:
            print("7回目\n")
        case 8:
            print("8回目\n")
        case 9:
            print("9回目\n")
# -*- coding: utf-8 -*-
import tkinter
from tkinter import font

root = tkinter.Tk()
root.title("Label")
root.geometry("400x400")

#デフォルト
label1 = tkinter.Label(root, text="Hello, World!")  #文字ラベル設定
label1.pack(side="top") # 場所を指定　（top, bottom, left, or right）

#文字色、背景色、サイズ、フォントを指定。
font1 = font.Font(family='Helvetica', size=20, weight='bold')
label2 = tkinter.Label(root, text="case", fg="white", bg="black", font=font1)
label2.pack(side="top")

#座標入力
font2 = font.Font(family='Times', size=40)
label3 = tkinter.Label(root, text="お前はこれから地獄を見ることになる。\nn嫌だったら今すぐこのモジュールを閉じろ。地獄を見たくなかったらウィンドウだけは最初に閉じるなよ\n忠告はしたからな。", font=font2)
label3.place(x=10, y=60)

root.mainloop()

for i in range(900):
    import tkinter as tk
    window = tk.Tk()
    window.title("shine")
    window.geometry("400x400")
    def close_window(event):
        window.destroy()
    window.bind("<Escape>",close_window)
window.mainloop()


