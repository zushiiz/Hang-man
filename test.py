import tkinter as tk

def update_image():
    # Update the PhotoImage object with a new image
    new_image = tk.PhotoImage(file="h2.ppm")
    label.config(image=new_image)
    # Keep a reference to the image to prevent it from being garbage collected
    label.image = new_image

# Create the Tkinter window
root = tk.Tk()
root.title("Image Update Example")

# Load the initial image
image = tk.PhotoImage(file="h0.ppm")

# Create a Label to display the image
label = tk.Label(root, image=image)
label.pack()

# Button to trigger image update
update_button = tk.Button(root, text="Update Image", command=update_image)
update_button.pack()

# Keep the Tkinter event loop running
root.mainloop()