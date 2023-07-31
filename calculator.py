import tkinter as tk

def on_click(btext):
    if btext == "=":
        try:
            result = eval(enter.get())
            enter.delete(0, tk.END)
            enter.insert(tk.END, str(result))
        except Exception as e:
            enter.delete(0, tk.END)
            enter.insert(tk.END, "Error")
    elif btext == "C":
        enter.delete(0, tk.END)
    else:
        enter.insert(tk.END, btext)


root = tk.Tk()
root.title(" Calculator")


enter = tk.Entry(root, font=("arial", 16))
enter.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for btext, row, col in buttons:
    button = tk.Button(root, text=btext, font=("arial", 16), command=lambda text=btext: on_click(text))
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
