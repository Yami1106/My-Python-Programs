import tkinter as tk

# create a Tkinter window
window = tk.Tk()

# set the background color of the window to blue
window.configure(bg="blue")

# set the cursor to be a hand cursor
window.configure(cursor="hand2")

# set the border width of the window to 10 pixels
window.configure(bd=10)

# set the highlight color of the window to yellow
window.configure(highlightcolor="yellow")

# set the width and height of the window to 300 pixels each
window.geometry("300x300")

# start the Tkinter event loop
window.mainloop()
