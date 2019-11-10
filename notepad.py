from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#file menu functions 
def new_file():
    global file
    window.title("Untitled - Notepad")
    text_area.delete(1.0,END)

#for opening file
def open_file():
    global file
    file = askopenfilename(defaultextension = ".txt",filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
    	file = None
    else: 
        window.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0,END)
        f = open(file,'r')
        text_area.insert(1.0,f.read())
        f.close()

#to save the file
def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt',defaultextension = ".txt",filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,'w')
            f.write(text_area.get(1.0,END))
            f.close()

            window.title(os.path.basename(file) + " -Notepad")
            print("File Saved")
    else:
        f = open(file,'w')
        f.write(text_area.get(1.0,END))
        f.close()
#to quit app    
def quit_app():
    window.destroy()
    

#edit menu functions

def about():
    showinfo("Notepad","\n Developed by : Sajid Shaikh")
if __name__ == "__main__":
    window = Tk()                   #window 
    window.title("Untitled Notepad*")       #title
    window.wm_iconbitmap("notepad.ico")
    window.geometry("644x788")

    #add text area
    text_area = Text(window,font = "lucida 13")
    file = None
    text_area.pack(expand = True,fill = BOTH)

    menu_bar = Menu(window)                             #create a menubar

    file_menu = Menu(menu_bar, tearoff = 0)                 #file_menu inside menu_bar
    file_menu.add_command(label = "New",command = new_file)         #add command of 'New'
    file_menu.add_command(label = "Open",command = open_file)           #open files
    file_menu.add_command(label = "Save",command = save_file)           #save files
    file_menu.add_separator()                                           #separator
    file_menu.add_command(label = "Exit",command = quit_app)                #to quite the app
    
    menu_bar.add_cascade(label = "File",menu = file_menu)                   #cascading file_menu in menu_bar
    
    #edit menu
    edit_menu = Menu(menu_bar,tearoff = 0)
    edit_menu.add_command(label = "Copy", accelerator = "Ctrl-C", command = lambda : window.focus_get().event_generate('<<Copy>>'))
    
    edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: window.focus_get().event_generate('<<Cut>>'))

    edit_menu.add_command(label = "Paste", accelerator = "Ctrl + V", command = lambda : window.focus_get().event_generate("<<Paste>>"))

    menu_bar.add_cascade(label = "Edit",menu = edit_menu)                      #cascading edit_menu in menu_bar

    # Help Menu Starts
    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label = "About Notepad", command=about)

    menu_bar.add_cascade(label="Help", menu = help_menu)                        #cascading help_menu in menu_bar

    window.config(menu = menu_bar)
    
    window.protocol('WM_DELETE_WINDOW',quit_app)
    window.mainloop()                   #loop that keeps it open
