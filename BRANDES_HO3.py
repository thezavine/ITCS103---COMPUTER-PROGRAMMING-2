import tkinter as calculator

solve = calculator.Tk()
solve.title("Simple Calculator")
solve.geometry("250x250")
solve.configure(bg="lightgreen")

# First is, I use def for the Arithmetic functions
def add():
    a = int(entry1.get())
    b = int(entry2.get())
    result_label.config(text=f"The sum of {a} + {b} is {a+b}.")

def subtract():
    a = int(entry1.get())
    b = int(entry2.get())
    result_label.config(text=f"The subtraction of {a} - {b} is {a-b}.")

def multiply():
    a = int(entry1.get())
    b = int(entry2.get())
    result_label.config(text=f"The multiplication of {a} * {b} is {a*b}.")

def divide():
    a = int(entry1.get())
    b = int(entry2.get())
    result_label.config(text=f"The division of {a} / {b} is {a/b}.")

# Frame for the title on top of it
top_frame = calculator.Frame(solve, bg="lightgreen")
top_frame.pack(fill="x")

result_label = calculator.Label(top_frame, text="Hello User, Let's Solve!!", bg="white", font=("Arial", 12))
result_label.pack(fill="x")

# Frame for inputs where the user will enter the numbers
input_frame = calculator.Frame(solve, bg="lightgreen")
input_frame.pack(pady=5)

label1 = calculator.Label(input_frame, text="Enter 1st Number:", bg="white")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = calculator.Entry(input_frame, width=12)
entry1.grid(row=0, column=1)

label2 = calculator.Label(input_frame, text="Enter 2nd Number:", bg="white")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = calculator.Entry(input_frame, width=12)
entry2.grid(row=1, column=1)

# Frame for buttons, so they can choose which arithmetic or what should they use to solve
button_frame = calculator.Frame(solve, bg="lightgreen")
button_frame.pack(pady=10)

btn_add = calculator.Button(button_frame, text="Add", bg="lightpink", width=5, command=add)
btn_add.grid(row=0, column=0, padx=7, pady=7)

btn_sub = calculator.Button(button_frame, text="Subtract", bg="lightpink", width=8, command=subtract)
btn_sub.grid(row=0, column=1, padx=7, pady=7)

btn_mul = calculator.Button(button_frame, text="Multiply", bg="lightpink", width=7, command=multiply)
btn_mul.grid(row=1, column=0, padx=5, pady=7)

btn_div = calculator.Button(button_frame, text="Division", bg="lightpink", width=8, command=divide)
btn_div.grid(row=1, column=1, padx=5, pady=7)

# lastly, the mainloop() that is always in the last part
solve.mainloop()