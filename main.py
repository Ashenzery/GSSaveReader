import os
import sys

from Tkinter import *
from PIL import Image, ImageTk


class GoblinButton:
    def __init__(self, name, y_pos, x_pos, root):
        self.name = name
        self.frame = Frame(root, bd=0, bg="black")
        self.frame.place( y=y_pos, x=x_pos )
        self.img = Image.open( "./temp/{0}.png".format(self.name) )
        self.image = ImageTk.PhotoImage( self.img )
        self.button = Button(
         self.frame,
         image=self.image,
         command=self.new_window,
         bd=0,
         bg="black" )

        self.button.pack( )
    def new_window(self):
        print(self.name)
        #FIXME

def module_path():
    if hasattr(sys, "frozen"):
        return os.path.dirname(
            unicode(sys.executable, sys.getfilesystemencoding( ))
            )
    return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))

def getCenter(scr, app_width=600, app_height=400):
    width = scr.winfo_screenwidth( )
    height = scr.winfo_screenheight( )
    #print "{0}x{1}".format(width, height)
    return '{0}x{1}+{2}+{3}'.format(
        app_width,
        app_height,
        int( ( width / 2.0 ) - ( app_width / 2.0 ) ),
        int( ( height / 2.0 ) - ( app_height / 2.0 ) ),
        )


work_dir = module_path( )
print
print work_dir
print len( work_dir )

root = Tk( )
root.config( bg="black" )
root.grid_columnconfigure( 0, pad=0 )
root.grid_rowconfigure( 0, pad=0 )
root.title( "                <  GSSaveReader  >" )
root.overrideredirect( 1 )
root.geometry(
    getCenter(
        root,
        330,
        210
              )
    )


bg1_img = Image.open( "./temp/bg1.png" )
bg1 = ImageTk.PhotoImage( bg1_img )
label_background = Label( root, image=bg1, bd=0 )
label_background.place( x=0, y=0 )


stop_btm_frame = Frame( root, bd=0, bg="black" )
stop_btm_frame.place( x=240, y=153 )


stop_img = Image.open( "./temp/stop.png" )
stop = ImageTk.PhotoImage( stop_img )
button_stop = Button( stop_btm_frame, image=stop, command=root.quit, bd=0, bg="black" )
button_stop.pack( )


gobins = [
{
'name' : 'Stalker',
'x' : 19,
'y' : 39
}, {
'name' : 'Rocketeer',
'x' : 92,
'y' : 39
}, {
'name' : 'Piro',
'x' : 165,
'y' : 39
}, {
'name' : 'Medic',
'x' : 238,
'y' : 39
},  {
'name' : 'Gunner',
'x' : 19,
'y' : 96
},  {
'name' : 'Exploder',
'x' : 92,
'y' : 96
},  {
'name' : 'Sniper',
'x' : 165,
'y' : 96
},  {
'name' : 'Ingeneer',
'x' : 238,
'y' : 96
}
]

butt_arr = []
for goblin in gobins:
    butt_arr.append(
        GoblinButton(goblin['name'], goblin['y'], goblin['x'], root)
    )



root.mainloop( )
