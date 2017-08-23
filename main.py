# -*- coding: utf-8 -*-
print 'TODO: '
print '1) Добавить всплывющее сообение о том, что сейв скопирован при нажатии на кнопку "copy"'
print '2) Изменить цвет названия предмета на цвет предмета'
print '3) Исправить изображение temp/bg2.png'

import os
import sys

from Tkinter import *
from PIL import Image, ImageTk


class MyLabel(Label):
    def __init__(self, place, text, x = 0, y = 0, color = 'grey', font = 'comic-sans 10'):
        Label.__init__(self, place)
        self.widget = Label(place, bg = 'black', fg = color, font = font, text = text)
        self.widget.place(x = x, y = y)


class GoblinButton:
    def __init__(self, name, y_pos, x_pos, root):
        self.name = name
        self.frame = Frame(root, bd = 0, bg = 'black')
        self.frame.place( y = y_pos, x = x_pos )
        self.image = ImageTk.PhotoImage( Image.open( './temp/{0}.png'.format(self.name) ) )
        self.button = Button(
            self.frame,
            image = self.image,
            command = self.new_window,
            bd = 0,
            bg = 'black' )
        self.button.pack()
        self.window = GoblinWindow(self.name, root)
    def new_window(self):
        self.window.win_state = self.window.win.state()
        if self.window.win_state == 'withdrawn':
            self.window.win.deiconify()
        elif self.window.win_state == 'normal':
            self.window.win.withdraw()
        else:
            print(self.win_state)


class GoblinWindow:
    def __init__(self, name, root):
        self.name = name
        self.win = Toplevel()
        self.win.resizable(False, False)
        self.background = Label(self.win , image = bg2, bd = 0 )
        self.background.place( x = 0, y = 0 )
        self.win.geometry( get_left_of(root) )
        self.win.withdraw()
        #TODO:
        #self.win.overrideredirect( True )
        self.win.title( name )
        self.win.tkraise()
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
                                command = self.up_action,
                                bd = 0,
                                bg = 'black'  ),
            'down'  : Button(
                                self.win,
                                image = images['down'],
                                command = self.down_action,
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
        self.saves = os.listdir('../../{0}'.format(self.name))
        self.saves = [ x for x in self.saves if ( x[:5] == '-load' and x[-4:] == '.txt' ) ]
        self.saves_len = len(self.saves)
        self.i = 0
        self.activ_save_path = '../../{0}/{1}'.format(self.name, self.saves[self.i])
        self.lvl = '1'
        self.gold = '3000'
        self.date =  self.parser()
        self.labels = {
            'lvl'   : MyLabel(self.win, 'Уровень: {0}'.format(self.date['lvl']['val']), y = 84, x = 250, font = 'comic-sans 7' ),
            'gold'  : MyLabel(self.win, 'Золото: {0}'.format(self.date['gold']['val']), y = 84, x = 350, font = 'comic-sans 7' ),
            'item1' : MyLabel(self.win, self.date['item1']['val'], y = 101, x= 250, color = self.date['item1']['color'] ),
            'item2' : MyLabel(self.win, self.date['item2']['val'], y = 117, x= 250, color = self.date['item2']['color'] ),
            'item3' : MyLabel(self.win, self.date['item3']['val'], y = 133, x= 250, color = self.date['item3']['color'] ),
            'item4' : MyLabel(self.win, self.date['item4']['val'], y = 150, x= 250, color = self.date['item4']['color'] ),
            'item5' : MyLabel(self.win, self.date['item5']['val'], y = 167, x= 250, color = self.date['item5']['color'] ),
            'item6' : MyLabel(self.win, self.date['item6']['val'], y = 184, x= 250, color = self.date['item6']['color'] )
        }


    def refresh(self):
        self.activ_save_path = '../../{0}/{1}'.format(self.name, self.saves[self.i])
        self.date =  self.parser()
        for key in self.labels:
            if key == 'lvl':
                f_val = 'Уровень: {0}'.format(self.date['lvl']['val'])
                f_color = 'grey'
            elif key == 'gold':
                f_val = 'Золото: {0}'.format(self.date['gold']['val'])
                f_color = 'grey'
            else:
                f_val  =  self.date[key]['val']
                f_color = self.date[key]['color']
            self.labels[key].widget.configure(text = f_val, fg = f_color)


    def parser(self):
        arr = []
        with open(self.activ_save_path, 'r') as f:
            for line in f:
                arr.append(line)
        """for i in range(len(arr)):
            print i, ') type = ', type(arr[i]), ';  whits length = ', len(arr[i])
            print arr[i]
        print '################################################################################'
        for i in [8, 9, 10, 13, 14, 15]:
            print from_item_get_name(arr[i])
        print '################################################################################'"""
        return {
            'lvl'   :  {
                'val' : arr[4].strip().split(' ')[1], #arr[4].split(' ')[4][:-1:],
                'color' : 'grey'
                },
            'gold'  :  {
                'val' : arr[5].strip().split(' ')[1], #arr[5].split(' ')[4],
                'color' : 'grey'
                },
            'item1' :  {
                'val' : from_item_get_name(arr[8]),
                'color' : 'white' #TODO - color from date
                 },
            'item2' :  {
                'val' : from_item_get_name(arr[9]),
                'color' : 'white'
                },
            'item3' :  {
                'val' : from_item_get_name(arr[10]),
                'color' : 'white'
                },
            'item4' :  {
                'val' : from_item_get_name(arr[13]),
                'color' : 'white'
                },
            'item5' :  {
                'val' : from_item_get_name(arr[14]),
                'color' : 'white'
                },
            'item6' :  {
                'val' : from_item_get_name(arr[15]),
                'color' : 'white'
                }
            }


    def up_action(self):
            self.i = (self.i + 1) %  self.saves_len
            self.refresh()

    def down_action(self):
            if self.i == 0:
                self.i = self.saves_len - 1
            else:
                self.i -= 1
            self.refresh()

    def hide_all(self):
        for goblin in goblin_arr:
            goblin.window.win.withdraw()


    def write(self):
        root.clipboard_clear()
        root.clipboard_append(self.saves[self.i][:-4:])

def from_item_get_name(string):
    index = string.find('|')
    if index != -1:
        string = string.strip().split('|')[1][9:]
    else:
        string = string.strip().split(' ')
        string = ' '.join(string[2:])
    if string[0] in ['\'', "\""] and string[-1] in ['\'', "\""]:
        return string[1:-1]
    return string

def module_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(
            unicode(sys.executable, sys.getfilesystemencoding())
            )
    return os.path.dirname(unicode(__file__, sys.getfilesystemencoding()))

def get_right_down(scr, app_width=330, app_height=210):
    width = scr.winfo_screenwidth()
    height = scr.winfo_screenheight()
    #print '{0}x{1}'.format(width, height)
    return '{0}x{1}+{2}+{3}'.format(
        app_width,
        app_height,
        int( width - app_width),
        int( height - app_height)
        #int( ( width / 2.0 ) - ( app_width / 2.0 ) ),
        #int( ( height / 2.0 ) - ( app_height / 2.0 ) ),
        )

def get_center(scr, app_width=330, app_height=210):
    width = scr.winfo_screenwidth()
    height = scr.winfo_screenheight()
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

work_dir = module_path()
print work_dir#, __name__


root = Tk()
root.resizable(False, False)
root.config( bg='black' )
root.grid_columnconfigure( 0, pad=0 )
root.grid_rowconfigure( 0, pad=0 )
root.title( ' < GSSaveReader > ' )
#TODO:
#root.overrideredirect( True )
root.tkraise()
root.geometry( get_right_down( root ) )


bg1_img = Image.open( './temp/bg1.png' )
bg1 = ImageTk.PhotoImage( bg1_img )
label_background = Label( root, image = bg1, bd = 0 )
label_background.place( x = 0, y = 0 )


bg2_img = Image.open( './temp/bg2.png' )
bg2 = ImageTk.PhotoImage( bg2_img )


stop_btm_frame = Frame( root, bd=0, bg='black' )
stop_btm_frame.place( x=238, y=153 )

images = { name : ImageTk.PhotoImage(
                Image.open( './temp/{0}.png'.format(name) )
                ) for name in ('up', 'down', 'copy', 're', 'stop') }

button_stop = Button( stop_btm_frame, image=images['stop'], command=root.quit, bd=0, bg='black' )
button_stop.pack()


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
    if os.path.isdir('../../{0}'.format(goblin['name'])):
        goblin_arr.append(
            GoblinButton(goblin['name'], goblin['y'], goblin['x'], root)
                        )

if __name__ == '__main__':
    root.mainloop()
else:
    print '__name__ == ' + __name__
