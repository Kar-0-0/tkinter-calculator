import tkinter as tk
from tkinter import messagebox

count = 0


def digit_check1(*args):
    global set_str
    current_str = num1.get()

    if current_str == "" or current_str.isdigit():
        set_str = current_str
    else:
        num1.set(set_str)


def digit_check2(*args):
    global curr_str
    current_str = num2.get()

    if current_str == "" or current_str.isdigit() and current_str != "0":
        curr_str = current_str
    else:
        num2.set(curr_str)


def remove():
    global answer
    if answer:
        answer.destroy()


def show_res(res):
    global answer
    global count

    count += 1
    answer = tk.Label(
        window, text=f"The Answer is... {res}", font=("Arial", 40, "bold")
    )
    answer.place(x=50, y=700)


def Evaluate():
    global count

    if radioint.get() == 0:
        if count > 0:
            remove()
        res = str(int(num1.get()) + int(num2.get()))
        show_res(res)

    if radioint.get() == 1:
        if count > 0:
            remove()
        res = str(int(num1.get()) - int(num2.get()))
        show_res(res)

    if radioint.get() == 2:
        if count > 0:
            remove()
        res = str(int(num1.get()) * int(num2.get()))
        show_res(res)

    if radioint.get() == 3:
        if count > 0:
            remove()
        res = str(int(num1.get()) / int(num2.get()))
        show_res(res)


window = tk.Tk()

window.geometry("800x800")
window.title("Calculator")

set_str = ""
num1 = tk.StringVar()
text1 = tk.Entry(window, textvariable=num1, bg="Beige")
num1.trace("w", digit_check1)
text1.place(x=100, y=300)

radioint = tk.IntVar()
radioint.set(0)

addition = tk.Radiobutton(window, text="+", variable=radioint, value=0)
addition.place(x=300, y=300)

subtraction = tk.Radiobutton(window, text="-", variable=radioint, value=1)
subtraction.place(x=300, y=325)

multiplication = tk.Radiobutton(window, text="*", variable=radioint, value=2)
multiplication.place(x=300, y=350)

division = tk.Radiobutton(window, text="/", variable=radioint, value=3)
division.place(x=300, y=375)

curr_str = ""
num2 = tk.StringVar()
text2 = tk.Entry(window, textvariable=num2, bg="Beige")
num2.trace("w", digit_check2)
text2.place(x=400, y=300)

# Not working
# equal_canvas = tk.Canvas(window, height=25, width=40, bg="Beige")
# equal_canvas.create_text(600, 300, text="=", font=("Arial", 40, "bold"), fill="Black")
# equal_canvas.place(x=600, y=300)

eval_button = tk.Button(window, text="Calculate", command=Evaluate)
eval_button.place(x=285, y=600)
window.mainloop()
