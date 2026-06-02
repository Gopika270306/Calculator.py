import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, height=2,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, height=2,
                  command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Clear", width=22, command=clear).grid(row=6, column=0, columnspan=4)

root.mainloop()