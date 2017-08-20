# encoding: utf-8


import os
import sys

from Tkinter import *
from PIL import Image, ImageTk


class GoblinButton:
    def __init__(self, name, y_pos, x_pos, root):
        self.frame = Frame(root, bd = 0, bg = "black")
        self.frame.place( y = y_pos, x = x_pos )
        self.image = ImageTk.PhotoImage( Image.open( "./temp/{0}.png".format(name) ) )
        self.button = Button(
            self.frame,
            image = self.image,
            command = self.new_window,
            bd = 0,
            bg = 'black' )
        self.button.pack( )
        self.window = GoblinWindow(name, root)
    def new_window(self):
        self.window.win_state = self.window.win.state( )
        if self.window.win_state == 'withdrawn':
            self.window.win.deiconify( )
        elif self.window.win_state == 'normal':
            self.window.win.withdraw( )
        else:
            print(self.win_state)


class GoblinWindow:
    def __init__(self, name, root):
        self.win = Toplevel( )
        self.win.resizable(False, False)
        self.background = Label(self.win , image = bg2, bd = 0 )
        self.background.place( x = 0, y = 0 )
        self.win.geometry( get_left_of(root) )
        self.win.withdraw( )
        #TODO:
        #self.win.overrideredirect( True )
        self.win.title( name )
        self.win.tkraise( )
        self.labels = {
            'lvl'   : Label(self.win),
            'gold'  : Label(self.win),
            'item1' : Label(self.win),
            'item2' : Label(self.win),
            'item3' : Label(self.win),
            'item4' : Label(self.win),
            'item5' : Label(self.win),
            'item6' : Label(self.win)
        }
        self.buttons = {
            're'    :  Button(
                                self.win,
                                image = images['re'],
                                command = self.hide_all,
                                bd = 0,
                                bg = 'black'  ),
            'up'    :  Button(
                                self.win,
                                image = images['up'],
                                #command = ,
                                bd = 0,
                                bg = 'black'  ),
            'down'  : Button(
                                self.win,
                                image = images['down'],
                                #command = ,
                                bd = 0,
                                bg = 'black'  ),
            'copy' : Button(
                                self.win,
                                image = images['copy'],
                                command = self.write,
                                bd = 0,
                                bg = 'black'  ),
        }
        self.buttons['re'].place(x=645, y=165)
        self.buttons['up'].place(x=575, y=65)
        self.buttons['down'].place(x=575, y=165)
        self.buttons['copy'].place(x=575, y=115)

    def hide_all(self):
        for goblin in goblin_arr:
            goblin.window.win.withdraw( )
    def write(self):
        root.clipboard_clear()
        root.clipboard_append('txt to write')

def module_path():
    if hasattr(sys, "frozen"):
        return os.path.dirname(
            unicode(sys.executable, sys.getfilesystemencoding( ))
            )
    return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))

def get_right_down(scr, app_width=330, app_height=210):
    width = scr.winfo_screenwidth( )
    height = scr.winfo_screenheight( )
    #print "{0}x{1}".format(width, height)
    return '{0}x{1}+{2}+{3}'.format(
        app_width,
        app_height,
        int( width - app_width),
        int( height - app_height)
        #int( ( width / 2.0 ) - ( app_width / 2.0 ) ),
        #int( ( height / 2.0 ) - ( app_height / 2.0 ) ),
        )

def get_center(scr, app_width=330, app_height=210):
    width = scr.winfo_screenwidth( )
    height = scr.winfo_screenheight( )
    return '{0}x{1}+{2}+{3}'.format(
        app_width,
        app_height,
        int( ( width / 2.0 ) - ( app_width / 2.0 ) ),
        int( ( height / 2.0 ) - ( app_height / 2.0 ) ),
        )

def get_left_of(scr, app_width=733 , app_height=210 ):
    main_win = get_right_down(scr)
    main_win = main_win.split('+')

    return '{0}x{1}+{2}+{3}'.format(
        app_width,
        app_height,
        int(main_win[1]) - app_width,
        main_win[2]
    )

work_dir = module_path( )
print
print work_dir
print len( work_dir )

root = Tk( )
root.resizable(False, False)
root.config( bg="black" )
root.grid_columnconfigure( 0, pad=0 )
root.grid_rowconfigure( 0, pad=0 )
root.title( ' < GSSaveReader > ' )
#TODO:
#root.overrideredirect( True )
root.tkraise( )
root.geometry( get_right_down( root ) )


bg1_img = Image.open( "./temp/bg1.png" )
bg1 = ImageTk.PhotoImage( bg1_img )
label_background = Label( root, image = bg1, bd = 0 )
label_background.place( x = 0, y = 0 )


bg2_img = Image.open( "./temp/bg2.png" )
bg2 = ImageTk.PhotoImage( bg2_img )


stop_btm_frame = Frame( root, bd=0, bg="black" )
stop_btm_frame.place( x=238, y=153 )

#TODO: criate copy.png
images = { name : ImageTk.PhotoImage(
                Image.open( "./temp/{0}.png".format(name) )
                ) for name in ('up', 'down', 'copy', 're', 'stop') }

button_stop = Button( stop_btm_frame, image=images['stop'], command=root.quit, bd=0, bg="black" )
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

goblin_arr = []
for goblin in gobins:
    goblin_arr.append(
        GoblinButton(goblin['name'], goblin['y'], goblin['x'], root)
    )



root.mainloop( )
