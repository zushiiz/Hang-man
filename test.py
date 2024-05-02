import tkinter as tk

var = 0

def update_image(ig):
    image_list = ["h0", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10"]
    new_image = tk.PhotoImage(file=image_list[ig]+".ppm")
    dimage.config(image=new_image)
    dimage.image = new_image

# Create the Tkinter window
root = tk.Tk()
root.title("Image Update Example")

# Load the initial image
iimage = tk.PhotoImage(file="h0.ppm")

# Create a Label to display the image
dimage = tk.Label(root, image=iimage)
dimage.pack()

# Button to trigger image update
update_button = tk.Button(root, text="Update Image", command=lambda:update_image(var))
update_button.pack()

# Keep the Tkinter event loop running
root.mainloop()