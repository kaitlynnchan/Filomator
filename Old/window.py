from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import sys, os

window = Tk()
global text
text = tk.StringVar()

path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)


def select_path(event):
    global output_path

    output_path = filedialog.askdirectory()
    entry0.delete(0, END)
    entry0.insert(0, output_path)


def btn_clicked():
    Value = entry0.get()
    print(Value)


def clear_func():
    text.set("")


window.geometry("1440x1024")
window.configure(bg="#009bff")
canvas = Canvas(
    window,
    bg="#009bff",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

canvas.create_rectangle(
    0, 229, 0 + 1440, 229 + 795,
    fill="#ffffff",
    outline="")

canvas.create_text(
    720.5, 104.0,
    text="Filomator GUI",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(96.0)))

canvas.create_text(
    227.5, 298.0,
    text="This is is an example file",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    227.5, 326.0,
    text="where we will be testing out our GUI",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    227.5, 354.0,
    text="Feel free to play around!",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=688, y=407,
    width=163,
    height=66)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_func,
    relief="flat")

b1.place(
    x=872, y=407,
    width=163,
    height=66)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    359.0, 451.5,
    image=entry0_img)

entry0 = tk.Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=text)

entry0.place(
    x=61.0, y=423,
    width=596.0,
    height=85)

entry0.bind("<1>", select_path)

canvas.create_text(
    150.0, 410.0,
    text="Choose File Path",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(24.0)))

window.mainloop()
