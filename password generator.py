import tkinter as tk
import random
import string

global password
def generate_password():
    l = int(length.get())
    chars = string.ascii_letters + string.digits + string.punctuation  
    password=''.join(random.choice(chars) for _ in range(l))
    result_label.config(text=password)

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)
length = tk.Entry(root)
length.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("aerial", 14))
result_label.pack(pady=10)

root.mainloop()
