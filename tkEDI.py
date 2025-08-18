###333###############################################################333###

#from tkinter import Tk, Menu, Text, tk.END, BOTH, Toplevel, Label
import tkinter as tk

from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess as su
import os

###################################################
# main window (wnd) & functons (code block 1)     
###################################################

wnd = tk.Tk()
wnd.title('tkIDE_pre_finish_version: 0.1.1 data:18.08.2026 20.05MSK add commands in "cmd" winow')

file_path = ''
tek_dir = ''
 

def set_file_path(path):
    global file_path
    file_path = path


def open_file(): ### function fo open .py file
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    print(path, 'path') ### print::: C:/Users/Azerty/Desktop/tkEDI/test.py path

    with open(path, 'r') as file: ### open file for read
        code = file.read() ### read
        edi.delete('1.0', tk.END) ### clear edi window (edi == editor)
        edi.insert('1.0', code) ### insert code from file to ede window
        set_file_path(path) ### set where our file is


def save_as(): ### s
    if file_path == '': ### if NO file's path ==>> set path
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')]) 
    else:
        path = file_path ### else use path 
    with open(path, 'w') as file: ### open file im write regime 
        code = edi.get('1.0', tk.END) ### berem data from begin to end in edi window
        file.write(code) ### write data to file
        set_file_path(path) 


def run(): ### 'run' function for py code
    co_res.delete("1.0", "end") ### clear 'co_res' window ('co_res' from 'code result')
    co_res.config(fg='white') ### set color text
    if file_path == '': ### if code NOT save to file!!! Need to save it first!!!
        save_prompt = tk.Toplevel() ### Toplevel window (vsplivaushee okno)
        text = tk.Label(save_prompt, text='Please save your code') ### show message in Toplevel window
        text.pack() ### pack Toplevel window with main window (wnd)
        return
    command = f'python {file_path}'  ###create command from file path
    
    process = su.Popen(command, stdout=su.PIPE, stderr=su.PIPE, shell=True)
    
    
    output, error = process.communicate()  #[0] ### poluchaem values from process (output, error)
    
    
    co_res.insert(tk.END, '>')
    co_res.insert(tk.END, '\n')
    co_res.insert(tk.END, 'output:')
    co_res.insert(tk.END, '\n')
    co_res.insert(tk.END, output)
    co_res.insert(tk.END, '\n')
    co_res.insert(tk.END, 'error:')
    co_res.insert(tk.END, '\n')
    if error == b'':
        co_res.config(fg='green') ### normal text color
        co_res.insert(tk.END, 'No errors') ### show that text if errors NO!!!
    else:
        co_res.config(fg='red') ### error text color
        co_res.insert(tk.END,  error) ### show error text

def run_cmd(insert):
    insert = co_res.get(pos, 'end -1c')
    
    try:
        result = su.check_output(["cmd", "/c", insert], encoding='cp866')
    except Exception as e:
        print(e, 'Exception')
    co_res.insert('end -1c', result)
    
def exit():
    wnd.quit()

###################################################
# menu (code block 2)
###################################################
menu_bar = tk.Menu(wnd) ### create menu bar

file_menu = tk.Menu(menu_bar, tearoff=0)
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

edi = tk.Text()
Font_tuple = ("Courier", 12, "normal")
edi.configure(font=Font_tuple)
edi.config(fg='white')
edi.config(bg='#060b24')
edi.pack(expand=1, fill=tk.BOTH)

###################################################
# co_res window (code block 4)
###################################################
co_res = tk.Text(height=12, fg='white')
Font_tuple = ("Courier", 12, "normal")
co_res.configure(font=Font_tuple)
co_res.config(bg='#060b24')
co_res.pack(expand=1, fill=tk.BOTH)
co_res.insert(tk.END, os.getcwd())
#print(os.getcwd(), 'os.getcwd()2')
co_res.insert(tk.END, '>')
pos = co_res.index("end-1c") #pos = get_last_line(co_res)
co_res.bind('<Return>', run_cmd)
###################################################
# co2_res window (code block 4)
###################################################

#os.system(
        #'start cmd /k "' +
        #'color 1f & ' +
        #'mode con: cols=140 lines=15000 &' +
        #'title cmd ' +
        #'"'
    #)

wnd.mainloop() #### Super Top Command!!!!
#####################2