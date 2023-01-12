###333###############################################################333###
# autor: nasingfaund aka Serj Kado
# e-mail: nasingfaund@gmail.com
# e-mail2: nasingfaund@ya.ru
###333###############################################################333###

from tkinter import Tk, Menu, Text, END, BOTH, Toplevel, Label
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os

###################################################
# main window (wnd) & functons (code block 1)     
###################################################

wnd = Tk()
wnd.title('tkIDE_pre_finish_version: 0.1.0 data:11.01.2023 17.46MSK')

file_path = '' 

def set_file_path(path):
    global file_path
    file_path = path


def open_file(): ### function fo open .py file
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file: ### open file for read
        code = file.read() ### read
        edi.delete('1.0', END) ### clear edi window (edi == editor)
        edi.insert('1.0', code) ### insert code from file to ede window
        set_file_path(path) ### set where our file is


def save_as(): ### s
    if file_path == '': ### if NO file's path ==>> set path
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')]) 
    else:
        path = file_path ### else use path 
    with open(path, 'w') as file: ### open file im write regime 
        code = edi.get('1.0', END) ### berem data from begin to end in edi window
        file.write(code) ### write data to file
        set_file_path(path) 


def run(): ### 'run' function for py code
    co_res.delete("1.0", "end") ### clear 'co_res' window ('co_res' from 'code result')
    co_res.config(fg='white') ### set color text
    if file_path == '': ### if code NOT save to file!!! Need to save it first!!!
        save_prompt = Toplevel() ### Toplevel window (vsplivaushee okno)
        text = Label(save_prompt, text='Please save your code') ### show message in Toplevel window
        text.pack() ### pack Toplevel window with main window (wnd)
        return
    command = f'python {file_path}'  ###create command from file path
    ###command2 = 'py -3 command'
    process = subprocess.Popen(['cmd.exe', '/k', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) ### run cmd.exe 
    output = None
    error = None
    output, error = process.communicate() ### poluchaem values from process (output, error)
    co_res.insert(END, os.getcwd()) ### show in window our work directory
    co_res.insert(END, '\>')
    co_res.insert(END, '\n')
    co_res.insert(END, 'output:')
    co_res.insert(END, '\n')
    co_res.insert(END, output)
    co_res.insert(END, '\n')
    co_res.insert(END, 'error:')
    co_res.insert(END, '\n')
    if error == b'':
        co_res.config(fg='green') ### normal text color
        co_res.insert(END, 'No errors') ### show that text if errors NO!!!
    else:
        co_res.config(fg='red') ### error text color
        co_res.insert(END,  error) ### show error text
    
def exit():
    wnd.quit()

###################################################
# menu (code block 2)
###################################################
menu_bar = Menu(wnd) ### create menu bar

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Run', command=run)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

menu_bar.add_command(label='Run', command=run) 

wnd.config(menu=menu_bar)

###################################################
# edi window (code block 3)
###################################################

edi = Text()
Font_tuple = ("Courier", 12, "normal")
edi.configure(font=Font_tuple)
edi.config(fg='white')
edi.config(bg='#060b24')
edi.pack(expand=1, fill=BOTH)

###################################################
# co_res window (code block 4)
###################################################
co_res = Text(height=12, fg='white')
Font_tuple = ("Courier", 12, "normal")
co_res.configure(font=Font_tuple)
co_res.config(bg='#060b24')
co_res.pack(expand=1, fill=BOTH)


wnd.mainloop() #### Super Top Command!!!!
###EOOFFFoff_11.01.2023_17.46MSK_tkIDE_pre_finish_version: 0.1.0 Total: 118 lines of py code
