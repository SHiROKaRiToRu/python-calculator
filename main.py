import tkinter as tk

window = tk.Tk()
window.geometry("350x450")
window.title("Python Calculator")

# allow window to expand
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

values = tk.Entry(window, font=("Arial", 16), justify="right")
values.grid(row=0, column=0, padx=20, pady=20, sticky="ew")


buttonframe = tk.Frame(window)
buttonframe.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# make grid uniform and expandable
for i in range(3):
    buttonframe.grid_columnconfigure(i, weight=1, uniform="x")
    buttonframe.grid_rowconfigure(i, weight=1)

btn_font = ("Arial", 18)


current_op = None
first_value = None

def get_number():
    try:
        return float(values.get())
    except ValueError:
        values.delete(0, tk.END)
        values.insert(0, "Error")
        return None

def clear_entry():
    values.delete(0, tk.END)

def set_operation(op):
    global first_value, current_op
    first_value = get_number()
    if first_value is None:
        return
    current_op = op
    clear_entry()

def calculate():
    global first_value, current_op
    second_value = get_number()
    if second_value is None or current_op is None:
        return

    try:
        if current_op == "+":
            result = first_value + second_value
        elif current_op == "-":
            result = first_value - second_value
        elif current_op == "*":
            result = first_value * second_value
        elif current_op == "/":
            result = first_value / second_value
        elif current_op == "%":          # percentage
            result = (first_value * second_value) / 100
        elif current_op == "^":
            result = first_value ** second_value
        elif current_op == "mod":       # modulus
            result = first_value % second_value

        clear_entry()
        values.insert(0, int(result) if result.is_integer() else result)

    except ZeroDivisionError:
        clear_entry()
        values.insert(0, "Error")

    first_value = None
    current_op = None



# row 0
tk.Button(buttonframe, text="+", font=btn_font,
          command=lambda: set_operation("+")).grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Button(buttonframe, text="-", font=btn_font,
          command=lambda: set_operation("-")).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
tk.Button(buttonframe, text="*", font=btn_font,
          command=lambda: set_operation("*")).grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

# row 1
tk.Button(buttonframe, text="/", font=btn_font,
          command=lambda: set_operation("/")).grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Button(buttonframe, text="%", font=btn_font,
          command=lambda: set_operation("%")).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
tk.Button(buttonframe, text="^", font=btn_font,
          command=lambda: set_operation("^")).grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

# row 2
tk.Button(buttonframe, text="mod", font=btn_font,
          command=lambda: set_operation("mod")).grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Button(buttonframe, text="=", font=btn_font,
          command=calculate).grid(row=2, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)

window.mainloop()
