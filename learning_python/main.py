from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("720x540")
window.title("Jeremiah's first window")

icon = PhotoImage(file="clock.png")
window.iconphoto(True, icon)
window.config(background="#5cfcff")

window.mainloop()  # replace window on computer screen

