from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from data_storage import *

def select_path(event):
    global output_path

    output_path = filedialog.askdirectory()
    entry0.delete(0, END)
    entry0.insert(0, output_path)


def select_path_destination(event):
    global output_path2

    output_path2 = filedialog.askdirectory()
    entry3.delete(0, END)
    entry3.insert(0, output_path2)


def btn_clicked():
    Value = entry0.get()
    file = open('path.txt', 'a')
    file.seek(0)
    file.write(str(Value) + '\n')
    print(Value)


def btn_clicked2():
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

def create_task():
    print(entry_name.get())

    hour = entry1.get()
    hour = convert_to_24_hr_clock(hour, time_set_pm)
    write_to_json(entry_name.get(), hour, entry2.get(), None, entry0.get(), entry3.get(), None, None)
    extract_data_fr_json()

window = Tk()

global output_path, output_path2, text, text2, hour, minute, time_set_am, time_set_pm, text_name, text_desired_files
text = tk.StringVar()
text2 = tk.StringVar()
hour = tk.IntVar()
minute = tk.IntVar()
time_set_am = tk.BooleanVar()
time_set_pm = tk.BooleanVar()
text_name = tk.StringVar()
text_desired_files = tk.StringVar()

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

# source select button
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

# source clear button
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

# hour up button
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

# hour down button
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

# min up button
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

# min down button
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

# am button
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

# pm button
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

# source entry
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

# hour entry
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

# min entry box
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

# source input path text
canvas.create_text(
    107.0, 395.0,
    text="Input Path",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(24.0)))

# storage select button
img8 = PhotoImage(file=f"img8.png")
b8 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked2,
    relief="flat")

b8.place(
    x=714, y=484,
    width=160,
    height=30)

# storage clear button
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

# time select button
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

# time clear button
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

# storage entry
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

# storage input path text
canvas.create_text(
    107.0, 499.0,
    text="Input Path",
    fill="#ffffff",
    font=("RobotoCondensed-Regular", int(24.0)))


# Name
entry_name_img = PhotoImage(file=f"img_textBox4.png")
entry_name_bg = canvas.create_image(
    371.0, 394.5,
    image=entry_name_img)

entry_name = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=text_name)

entry_name.place(
    x=243, y=650,
    width=443,
    height=37)

#entry_name.bind("<1>", select_name)

# select_name_img = PhotoImage(file=f"img0.png")
# select_name_btn = Button(
#     image=select_name_img,
#     borderwidth=0,
#     highlightthickness=0,
#     command=select_name,
#     relief="flat")

# select_name_btn.place(
#     x=714, y=650,
#     width=160,
#     height=30)

canvas.create_text(
    130.0, 670.0,
    text="Input Name",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

# File type and name
entry_desired_files_img = PhotoImage(file=f"img_textBox4.png")
entry_desired_files_bg = canvas.create_image(
    431.0, 394.5,
    image=entry_desired_files_img)

entry_desired_files = Entry(
    bd=0,
    bg="#425b6b",
    highlightthickness=0,
    textvariable=text_desired_files)

entry_desired_files.place(
    x=353, y=700,
    width=443,
    height=37)

#entry_desired_files.bind("<1>", select_desired_files)

# select_desired_files_img = PhotoImage(file=f"img0.png")
# select_desired_files_btn = Button(
#     image=select_desired_files_img,
#     borderwidth=0,
#     highlightthickness=0,
#     command=btn_clicked,
#     relief="flat")

# select_desired_files_btn.place(
#     x=824, y=700,
#     width=160,
#     height=30)

canvas.create_text(
    160.0, 720.0,
    text="File Types and Names",
    fill="#000000",
    font=("RobotoCondensed-Regular", int(24.0)))

# new task button
new_task_img = PhotoImage(file=f"new_task.png")
new_task_btn = Button(
    image=new_task_img,
    borderwidth=0,
    highlightthickness=0,
    command=create_task,
    relief="flat")

new_task_btn.place(
    x=1280, y=720,
    width=160,
    height=59)

# window.resizable(False, False)
window.mainloop()
