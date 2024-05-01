import tkinter as tk

# Create a tkinter window
root = tk.Tk()

# Load the image
image_path = "34.ppm"
image = tk.PhotoImage(file=image_path)

# Resize the image (optional)
# You can adjust these values to resize the image as per your requirements
# For example, to resize to 200x200 pixels, set width=200 and height=200
resized_image = image.subsample(3, 3)  # Example: Resize by a factor of 2

# Create a label to display the image
label = tk.Label(root, image=resized_image)  # Adjust width and height as needed
label.pack()

# Run the tkinter event loop
root.mainloop()