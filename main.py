import tkinter
from tkinter import END, StringVar, font, scrolledtext
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# def window
window = tkinter.Tk()
window.title('TextWrite.py')
#window.iconbitmap('./w.ico')
window.geometry('600x500+500+200')
window.resizable(True,True)

# def functions
def change_font(event):
    # change font
    if font_opt.get() == 'none':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_opt.get())
        
    # change font style
    input_text.config(font=my_font)

    # change font size
    new_size = font_size.get()
    try:
        new_size = float(new_size)
        print(f"Changed font size to {new_size}")
    except ValueError:
        print('Invalid number')

def new_note():
    # create new note
    saveqs=messagebox.askyesno("Alert","Do you want to save your note?")
    if saveqs==0:
        input_text.delete('1.0', END)
    else:
        save_note()

def close_note():
    # create new note
    saveqs=messagebox.askyesno("Alert","Do you want to save your note?")
    if saveqs==0:
        window.destroy()
    else:
        save_note()

def save_note():
    # use filled dialog to get location and name of where to save
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Note",filetypes=(("Text Files",".txt"),("All Files",".")))
    with open(save_name, 'w') as f:
        f.write(font_family.get() + "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(font_opt.get() + "\n")
        f.write(input_text.get("1.0",END))

def open_note():
    # Use filedialog to get locaionn and directory of nnote file
    open_name = filedialog.askopenfilename(initialdir="./", title="Open Note", filetypes=(("Text Files",".txt"),("All Files",".")))
    with open(open_name,'r') as f:
        # clear the current text
        input_text.delete("1.0",END)
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_opt.set(f.readline().strip())
        # call change font for these
        change_font(1)
        # write remaining text
        text = f.read()
        input_text.insert("1.0",text)

# file menu
# Start menu
menu = tkinter.Menu(window)
window.config(menu = menu)
# Add File menu
file_menu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "File", menu = file_menu)
# File menu
file_menu.add_command(label = "New", accelerator="Ctrl+N", command=new_note)
file_menu.add_command(label = "Open...", accelerator="Ctrl+O", command=open_note)
file_menu.add_command(label = "Save", accelerator="Ctrl+S", command=save_note)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command=close_note)


# def font/colour
text_colour = "#fffacd"
menu_colour = "#dbd9db"
window_colour = "#6c809a"
window.configure(bg=window_colour)

# def layout
# def frames
menu_frame = tkinter.Frame(window, background=menu_colour)
text_frame = tkinter.Frame(window, background=text_colour)
menu_frame.pack(padx=5,pady=5)
text_frame.pack(padx=5,pady=5)

# menu frame layout
# create menu
# create font list
families = [f for f in font.families()]
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('Calibri')
# set width for long-ass font names
font_family_drop.config(width=16)
font_family_drop.grid(row=0,column=4,padx=5,pady=5)

size = [8,10,12,14,16,20,24,28,32,64,69,96,420]
font_size = StringVar()
font_size_combo = ttk.Combobox(menu_frame, textvariable=font_size,values=size,width=4)
font_size.set(12)
font_size_combo.bind('<<ComboboxSelected>>', change_font)
font_size_combo.bind('<FocusOut>',change_font)
font_size_combo.bind('<Return>',change_font)
font_size_combo.grid(row=0,column=5,padx=5,pady=5)

opt = ['none','bold','italic']
font_opt = StringVar()
opt_drop = tkinter.OptionMenu(menu_frame, font_opt, *opt, command=change_font)
font_opt.set('none')
# set width constant
opt_drop.config(width=5)
opt_drop.grid(row=0,column=6,padx=5,pady=5)

# text frame layout
my_font = (font_family.get(), font_size.get())

# c
# s
input_text = tkinter.scrolledtext.ScrolledText(text_frame, width=1000, height=100, bg=text_colour, font=my_font)
input_text.pack()


window.bind('<Control-n>', lambda event: new_note())
window.bind('<Control-o>', lambda event: open_note())
window.bind('<Control-s>', lambda event: save_note())

window.mainloop()