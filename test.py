import random
import tkinter as tk


root = tk.Tk()
root.geometry('905x700')
img = tk.PhotoImage(file="h1.png")
label = tk.Label(root, image=img)
label.pack() 
root.mainloop()
    