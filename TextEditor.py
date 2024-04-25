import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog as fd
from tkinter import messagebox
import time


"""Imitation program of the text editor for windows."""

class TextEditor(tk.Tk):
    def __init__(self) -> None:
        """Initialize Text Editor"""
        self.file_path = ""
        self.window = tk.Tk()
        self.window.title("Untitled")
        self.window.option_add('*tearOFF', False)
        self.window.grid_propagate(False)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.geometry("1280x720")
        self.window.iconbitmap('notepad_icon.ico')

        # Create text widget to contain user keyboard input. Create font
        # object to hold text size. 
        self.font = Font(family="Helvetica", size=11)
        self.text = tk.Text(self.window, 
                       wrap=tk.CHAR,
                       undo=True, 
                       maxundo=100, 
                       padx=10, 
                       pady=10,
                       font=self.font
                       )
        
        # Add vertical scroll bar (vsb) and tie text widget scroll to VSB
        # vertical scroll. 
        vsb = tk.Scrollbar(self.window, orient=tk.VERTICAL, 
                           command=self.text.yview)
        self.text['yscrollcommand'] = vsb.set

        # Add horizontal scroll bar (hsb) and tie widget horizontal
        # scroll to HSB
        hsb = tk.Scrollbar(self.window, orient=tk.HORIZONTAL, 
                           command=self.text.xview)
        self.text['xscrollcommand'] = hsb.set

        # Create menu widget
        menubar = tk.Menu(self.window, tearoff=0)
        self.window['menu'] = menubar

        # Create menu items and add to menubar
        menu_file = tk.Menu(menubar, tearoff=0)
        menu_edit = tk.Menu(menubar, tearoff=0)
        menu_format = tk.Menu(menubar, tearoff=0)
        menu_view = tk.Menu(menubar, tearoff=0)
        menu_help = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(menu=menu_file, label="File")
        menubar.add_cascade(menu=menu_edit, label="Edit")
        menubar.add_cascade(menu=menu_format, label="Format")
        menubar.add_cascade(menu=menu_view, label="View")
        menubar.add_cascade(menu=menu_help, label="Help")

        # Add File menu items
        menu_file.add_command(label="New", command=self.new)
        menu_file.add_command(label="New Window", command=self.new_window)
        menu_file.add_command(label="Open", command=self.open)
        menu_file.add_command(label="Save", command=self.save)
        menu_file.add_command(label="Save As...", command=self.save_as)
        menu_file.add_separator()
        menu_file.add_command(label="Page Setup (WIP)", command=self.page_setup)
        menu_file.add_command(label="Print (WIP)", command=self.print)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.exit)

        # Add edit menu items
        menu_edit.add_command(label="Undo", command=self.text.edit_undo)
        menu_edit.add_command(label="Redo", command=self.text.edit_redo)
        menu_edit.add_separator()
        menu_edit.add_command(label="Cut", command=self.cut)
        menu_edit.add_command(label="Copy", command=self.copy)
        menu_edit.add_command(label="Paste", command=self.paste)
        menu_edit.add_separator()
        menu_edit.add_command(label="Select All", command=self.select_all)
        menu_edit.add_command(label="Time/Date", command=self.time_date)

        # Add format menu items
        self.checked = tk.IntVar()
        menu_format.add_checkbutton(label="Word Wrap", 
                                    onvalue=1, 
                                    offvalue=0, 
                                    variable=self.checked, 
                                    command=self.word_wrap)
        menu_format.add_command(label="Font...")

        # Add view menu items
        menu_zoom = tk.Menu(menu_view, tearoff=0)
        menu_zoom.add_command(label="Zoom In", command=self.zoom_in)
        menu_zoom.add_command(label="Zoom Out", command=self.zoom_out)
        menu_zoom.add_command(label="Restore Default Zoom", 
                              command=self.restore_default_zoom)
        menu_view.add_cascade(menu=menu_zoom, label="Zoom")
        menu_view.add_checkbutton(label="Status Bar")
        
        # Add help menu item
        menu_help.add_command(label="About Text Editor", command=self.about_me)

        # Add widgets to frame
        vsb.grid(row=0, column=1, sticky=tk.NS)
        hsb.grid(row=1, column=0, sticky=tk.EW)
        self.text.grid(row=0, column=0, sticky=tk.NSEW)

        # Add keybind


        self.window.mainloop()

    def run(self):
        """Loop and respond to keyboard and mouse events"""
        
    def new(self):
        """Start new text editor state"""
        self.file_path = ""
        self.window.title("Untitled")
        self.text.delete('1.0', tk.END)

    def new_window(self):
        """Create new text window"""
        te = TextEditor()
    
    def open(self):
        """Open saved text file"""
        file = fd.askopenfile(mode="r", title="Open a file")

        # Read contents and replace text within text window
        contents = file.read()
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', contents)
        self.window.title(file.name)
        self.file_path = file.name

    def save(self):
        """Save text file"""
        if self.file_path:
            try: 
                with open(self.file_path, 'w') as file:
                    text_content = self.text.get("1.0", tk.END)
                    file.write(text_content)
            except Exception as e:
                print("Could not open file. ")
        else:
            self.save_as()
            

    def save_as(self):
        """Save file as into directory of user's choice"""
        self.file_path = fd.asksaveasfilename(defaultextension=".txt", 
                                         filetypes=[("Text files", "*.txt"), 
                                                    ("All files", "*.*")])
        if self.file_path:
            try:
                with open(self.file_path, 'w') as file:
                    text_content = self.text.get("1.0", tk.END)
                    file.write(text_content)

                # Rename window title
                self.window.title(f"{self.file_path}")
            except Exception as e:
                print("Could not open file. ")

    def page_setup(self):
        """Go through windows print page dialog and configure print"""
        pass

    def print(self):
        """Send text to printer"""
        pass

    def exit(self):
        """Exit text editor"""
        self.window.destroy()

    def cut(self):
        """Cut text"""
        self.text.event_generate("<<Cut>>")
    
    def copy(self):
        """Copy text"""
        self.text.event_generate("<<Copy>>")
    
    def paste(self):
        """Paste text"""
        self.text.event_generate("<<Paste>>")

    def select_all(self):
        """Select all text"""
        self.text.tag_add(tk.SEL, "1.0", tk.END)

    def time_date(self):
        """Print time/date to text window"""
        self.text.insert(tk.INSERT, time.ctime())
    
    def word_wrap(self):
        """Enable/disable word wrap"""
        checked = self.checked.get()
        print(checked)

        if checked:
            self.text.config(wrap=tk.WORD)
        else:
            self.text.config(wrap=tk.CHAR)

    def zoom_in(self):
        """Zoom in, or increase word font"""
        size = self.font.cget('size')
        if size < 32:
            self.font.config(size=size+2)

    def zoom_out(self):
        """Zoom out, or decrease word font"""
        size = self.font.cget('size')
        if size > 8:
            self.font.config(size=size-2)

    def restore_default_zoom(self):
        """Reset zoom. or set font to 11"""
        self.font.config(size=11)

    def about_me(self):
        messagebox.showinfo("About Me", "Made using tkinter and for fun. :)\n"
                            "Many things are WIP. Will improve this further "
                            "when I get the chance. ")


if __name__ == "__main__":
    te = TextEditor()
    te.run()