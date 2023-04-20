import os
import random
import sys
from PIL import Image
from tkinter import Tk, Label, Button, filedialog

folder_path = ""  # Global variable to store folder path


def choose_random_image():
    global folder_path  # can be accessed and modified from any part of this function
    try:
        # Get a list of image files in the chosen folder
        # os.listdir returns a list of all files and directories in a directory
        image_files = [f for f in os.listdir(folder_path) if f.endswith(
            ".jpg") or f.endswith(".jpeg") or f.endswith(".png") or f.endswith(".gif")]

        if not image_files:
            raise ValueError("No image files found in the folder.")

        # Choose a random image file from the list
        random_image = random.choice(image_files)

        # Get the full path of the randomly chosen image file by concantenating
        # Open and display the image using Pillow
        image_path = os.path.join(folder_path, random_image)

        image = Image.open(image_path)  # opens the image path
        # used to display an image using the default image viewer associated with the operating system.
        image.show()
    except Exception as e:
        print(f"Error: {e}")


def browse_folder():
    global folder_path
    # Open a folder dialog to choose a folder and store the chosen path in the global variable
    folder_path = filedialog.askdirectory()
    folder_label.config(text=f"Folder: {folder_path}")


root = Tk()
root.title("Image Viewer")

folder_label = Label(root, text="Choose a folder containing images.")
folder_label.pack(pady=100, padx=100)

browse_button = Button(root, text="Browse", command=browse_folder, font=(
    "Helvetica", 14),  fg="white",  bg="blue",  width=10, height=1)
browse_button.pack()

view_button = Button(root, text="View Random Image", command=choose_random_image, font=(
    "Helvetica", 14),  fg="white",  bg="#34A2FE",  width=20, height=1)
view_button.pack(pady=10)

root.mainloop()
