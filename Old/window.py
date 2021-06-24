from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox

# import sys, os
# path = getattr(sys, '_MEIPASS', os.getcwd())
# os.chdir(path)


def select_path(event):
    global output_path

    output_path = filedialog.askdirectory()
    entry0.delete(0, END)
    entry0.insert(0, output_path)


def btn_clicked():
    Value = entry0.get()
    file = open('path.txt', 'a')
    file.seek(0)
    file.write(str(Value) + '\n')
    print(Value)


def hour_increment():
    current = entry1.get()
    current = int(current)
    if 12 > current >= 0:
        hour.set(current + 1)
    else:
        print("Out of bounds")


def hour_decrement():
    current = entry1.get()
    current = int(current)
    if 12 >= current > 0:
        hour.set(current - 1)
    else:
        print("Out of bounds")


def minute_increment():
    current = entry2.get()
    current = int(current)
    if 59 > current >= 0:
        minute.set(current + 1)
    else:
        print("Out of bounds")


def minute_decrement():
    current = entry2.get()
    current = int(current)
    if 59 >= current > 0:
        minute.set(current - 1)
    else:
        print("Out of bounds")


def time_am():
    file = open('time.txt', 'a')
    file.seek(0)
    print_hour = entry1.get()
    print_minute = entry2.get()
    if int(print_hour) == 0 and int(print_minute) == 0:
        print_time = "00:00 AM"
        messagebox.showinfo('Time', str(print_time))
        print(print_time)
        file.write(str(print_hour) + ":" + str(print_minute) + "AM" + "\n")
        file.close()
    elif int(print_hour) < 10 and int(print_minute) < 10:
        print_time = "0" + str(print_hour) + ":0" + str(print_minute) + " AM"
        messagebox.showinfo('Time', str(print_time))
        print(print_time)
        file.write(str(print_hour) + ":" + str(print_minute) + "AM" + "\n")
        file.close()
    else:
        print_time = str(print_hour) + ":" + str(print_minute) + " AM"
        messagebox.showinfo('Time', str(print_time))
        print(print_time)
        file.write(str(print_hour) + ":" + str(print_minute) + "AM" + "\n")
        file.close()


def time_pm():
    file = open('time.txt', 'a')
    file.seek(0)
    print_hour = int(entry1.get())
    print_minute = entry2.get()
    if int(print_hour) == 0 and int(print_minute) == 0:
        print_time = "00:00 PM"
        messagebox.showinfo('Time', str(print_time))
        print(print_time)
        file.write(str(print_hour) + ":" + str(print_minute) + "PM" + "\n")
        file.close()
    elif int(print_hour) < 10 and int(print_minute) < 10:
        print_time = "0" + str(print_hour) + ":0" + str(print_minute) + " PM"
        messagebox.showinfo('Time', str(print_time))
        print(print_time)
        file.write(str(print_hour) + ":" + str(print_minute) + "PM" + "\n")
        file.close()
    else:
        print_time = str(print_hour) + ":" + str(print_minute) + " PM"
        messagebox.showinfo('Time', str(print_time))
        print(print_time)
        file.write(str(print_hour) + ":" + str(print_minute) + "PM" + "\n")
        file.close()


def clear_func():
    text.set("")


window = Tk()

global output_path, text, hour, minute
text = tk.StringVar()
hour = tk.IntVar()
minute = tk.IntVar()

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
    0, 185, 0 + 1440, 185 + 839,
    fill="#ffffff",
    outline="")

canvas.create_text(
    720.5, 104.0,
    text="Filomator GUI",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(96.0)))

canvas.create_text(
    233.5, 248.0,
    text="This is is an example file",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    233.5, 276.0,
    text="where we will be testing out our GUI",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    233.5, 304.0,
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
    x=720, y=349,
    width=160,
    height=30)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_func,
    relief="flat")

b1.place(
    x=891, y=349,
    width=160,
    height=30)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=hour_increment,
    relief="flat")

b2.place(
    x=155, y=396,
    width=74,
    height=18)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=hour_decrement,
    relief="flat")

b3.place(
    x=155, y=416,
    width=74,
    height=18)

img4 = PhotoImage(file=f"img4.png")
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=minute_increment,
    relief="flat")

b4.place(
    x=338, y=396,
    width=74,
    height=18)

img5 = PhotoImage(file=f"img5.png")
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=minute_decrement,
    relief="flat")

b5.place(
    x=338, y=416,
    width=74,
    height=18)

img6 = PhotoImage(file=f"img6.png")
b6 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=time_am,
    relief="flat")

b6.place(
    x=421, y=396,
    width=74,
    height=18)

img7 = PhotoImage(file=f"img7.png")
b7 = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=time_pm,
    relief="flat")

b7.place(
    x=421, y=416,
    width=74,
    height=18)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    377.0, 363.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=text)

entry0.place(
    x=180.0, y=346,
    width=510.0,
    height=37)

entry0.bind("<1>", select_path)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    102.0, 415.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=hour)

entry1.place(
    x=67.0, y=396,
    width=70.0,
    height=37)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(
    284.0, 415.5,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=minute)

entry2.place(
    x=249.0, y=396,
    width=70.0,
    height=37)

canvas.create_text(
    113.0, 364.0,
    text="Input Path",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(24.0)))

window.mainloop()
