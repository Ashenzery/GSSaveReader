import os
import sys

from Tkinter import *
from PIL import Image, ImageTk

def module_path():
    if hasattr(sys, "frozen"):
        return os.path.dirname(
            unicode(sys.executable, sys.getfilesystemencoding( ))
            )
    return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))

def getCenter(scr, app_width=600, app_height=400):
    width = scr.winfo_screenwidth()
    height = scr.winfo_screenheight()
    print "{0}x{1}".format(width, height)
    return '{0}x{1}+{2}+{3}'.format(
        app_width,
        app_height,
        int( ( width / 2.0 ) - ( app_width / 2.0 ) ),
        int( ( height / 2.0 ) - ( app_height / 2.0 ) ),
        )
    

work_dir = module_path()
print work_dir


root = Tk()
root.config(bg="black")
root.grid_columnconfigure(0, pad=0)
root.grid_rowconfigure(0, pad=0) 
root.title("<  GSSaveReader  >")
root.overrideredirect(1)
root.geometry(
    getCenter(
        root,
        330,
        210
              )
    )


bg1_img = Image.open("./temp/bg1.png")
bg1 = ImageTk.PhotoImage(bg1_img)
label_background = Label(root, image=bg1, bd=0)
label_background.place(x=0, y=0)

'''
butt_arr = ['stop']
buttons = { butt_arr[i]: val for i in range(len(buttons_arr)) }
'''

frame1 = Frame(root, bd=0)
frame1.place(x=240, y=153)


stop_img = Image.open("./temp/stop.png")
stop = ImageTk.PhotoImage(stop_img)
button_stop = Button(frame1, image=stop, command=root.quit, bd=0, bg="black")
button_stop.pack()
root.mainloop()
