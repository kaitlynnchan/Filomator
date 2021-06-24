from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox


def select_path(event):
    global output_path

    output_path = filedialog.askdirectory()
    entry0.delete(0, END)
    entry0.insert(0, output_path)


def select_path_destination(event):
    global output_path2

    output_path2 = filedialog.askdirectory()
    entry3.delete(0, END)
    entry3.insert(0, output_path)


def btn_clicked():
    Value = entry0.get()
    file = open('path.txt', 'a')
    file.seek(0)
    file.write(str(Value) + '\n')
    print(Value)


def btn_clicked():
    Value = entry3.get()
    file = open('path_destination.txt', 'a')
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
    global time_set_am
    time_set_am = True
    print(time_set_am)


def time_pm():
    global time_set_pm
    time_set_pm = True
    print(time_set_pm)


def time_select():
    if time_set_am:
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
    elif time_set_pm:
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


def clear_func2():
    text2.set("")


def time_clear():
    hour.set("")
    minute.set("")


window = Tk()

global output_path, output_path2, text, text2, hour, minute, time_set_am, time_set_pm
text = tk.StringVar()
text2 = tk.StringVar()
hour = tk.IntVar()
minute = tk.IntVar()
time_set_am = tk.BooleanVar()
time_set_pm = tk.BooleanVar()

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
    227.5, 239.0,
    text="This is is an example file",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    227.5, 267.0,
    text="where we will be testing out our GUI",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    227.5, 295.0,
    text="Feel free to play around!",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    227.5, 354.0,
    text="Source Folder",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    227.5, 455.0,
    text="Storage Folder",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

canvas.create_text(
    227.5, 560.0,
    text="Select Time",
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
    x=714, y=380,
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
    x=885, y=380,
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
    x=149, y=581,
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
    x=149, y=601,
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
    x=332, y=581,
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
    x=332, y=601,
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
    x=415, y=581,
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
    x=415, y=601,
    width=74,
    height=18)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    371.0, 394.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=text)

entry0.place(
    x=176.0, y=377,
    width=510.0,
    height=37)

entry0.bind("<1>", select_path)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    96.0, 600.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=hour)

entry1.place(
    x=61.0, y=581,
    width=70.0,
    height=37)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(
    278.0, 600.5,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=minute)

entry2.place(
    x=243.0, y=581,
    width=70.0,
    height=37)

canvas.create_text(
    107.0, 395.0,
    text="Input Path",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(24.0)))

img8 = PhotoImage(file=f"img8.png")
b8 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b8.place(
    x=714, y=484,
    width=160,
    height=30)

img9 = PhotoImage(file=f"img9.png")
b9 = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=clear_func2,
    relief="flat")

b9.place(
    x=885, y=484,
    width=160,
    height=30)

img10 = PhotoImage(file=f"img10.png")
b10 = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=time_select,
    relief="flat")

b10.place(
    x=514, y=587,
    width=160,
    height=30)

img11 = PhotoImage(file=f"img11.png")
b11 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    command=time_clear,
    relief="flat")

b11.place(
    x=685, y=587,
    width=160,
    height=30)

entry3_img = PhotoImage(file=f"img_textBox3.png")
entry3_bg = canvas.create_image(
    371.0, 498.5,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=text2)

entry3.place(
    x=176.0, y=481,
    width=510.0,
    height=37)

entry3.bind("<1>", select_path_destination)

canvas.create_text(
    107.0, 499.0,
    text="Input Path",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(24.0)))

# window.resizable(False, False)
window.mainloop()
