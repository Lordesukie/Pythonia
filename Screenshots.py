import tkinter as tk
from tkinter import messagebox
import pyscreenshot as ImageGrab

def take_screenshot():
    # Capture the screen
    image = ImageGrab.grab()
    
    # Show the screenshot
    image.show()
    
    # Save the screenshot
    image.save("GeeksforGeeks.png")
    
    # Optional: Notify user
    messagebox.showinfo("Success", "Screenshot saved as Pyscreenshot.png")

# Create the main window
root = tk.Tk()
root.title("Screenshot App")
root.geometry("300x150")

# Create a button to take a screenshot
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot, font=("Arial", 14))
screenshot_button.pack(expand=True)

# Run the application
root.mainloop()


#the program uses Pythom image library, PIL or pillow and pyscreenshot to take screenshots.
# The pyscreenshot module is a cross-platform Python module for taking screenshots.
# It works on Windows, Linux, and Mac OS X.
# It is a pure Python module and does not require any external dependencies.
# The module is compatible with Python 2 and 3.
# The module is also compatible with PyPy.
# The module is available on PyPI and can be installed using pip.
# The module is also available on Anaconda and can be installed using conda.
# The module is also available on GitHub and can be installed using git.
#


