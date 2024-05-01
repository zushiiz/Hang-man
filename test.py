from tkinter import *

def update_image():
    # Update the image here
    pass  # Placeholder for image update logic

root = Tk()
root.geometry('400x400')  # Adjust dimensions as needed
root.title('Image Display')

image = PhotoImage(file='h1.png')  # Replace 'your_image.png' with the path to your image file

label = Label(root, image=image)
label.pack()  # Adjust positioning as needed

button = Button(root, text='Update Image', command=update_image)
button.pack()  # Adjust positioning as needed

root.mainloop()