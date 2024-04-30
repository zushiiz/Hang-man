import tkinter as tk

def reset_variable():
    global variable
    variable = "hello"
    print("Variable reset to:", variable)

num = 1
def sum():
    global num
    num+=1

print(num)
sum()
print(num)

def function():
    return "hello"

variable = function()

# Create the main application window
root = tk.Tk()
root.title("Reset Variable")

# Create a label to display the current value of the variable
label = tk.Label(root, text="Variable: " + variable)
label.pack()

# Create a button to reset the variable
button = tk.Button(root, text="Reset Variable", command=reset_variable)
button.pack()

# Run the Tkinter event loop
root.mainloop()