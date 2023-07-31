import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
# Example: Drawing a line
canvas.create_oval(50, 50, 150, 150, fill="pink")
def on_button_click():
    # Your event handling code here

    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack()
root.mainloop()




