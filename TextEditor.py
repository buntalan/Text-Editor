import tkinter as tk
import tkinter.scrolledtext as scrolledtext

"""Imitation program of the text editor for windows."""

class TextEditor():
    def __init__(self) -> None:
        """Initialize Text Editor"""
        window = tk.Tk()
        window.title("Text Editor")
        window.option_add('*tearOFF', False)
        window.grid_propagate(False)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.geometry("1200x720")

        # Create text widget to contain user keyboard input
        text = tk.Text(window, 
                       wrap=tk.CHAR, 
                       maxundo=100, 
                       padx=10, 
                       pady=10,
                       )
        
        # Add vertical scroll bar (vsb) and tie text widget scroll to VSB
        # vertical scroll. 
        vsb = tk.Scrollbar(window, orient=tk.VERTICAL, command=text.yview)
        text['yscrollcommand'] = vsb.set

        # Add horizontal scroll bar (hsb) and tie widget horizontal
        # scroll to HSB
        hsb = tk.Scrollbar(window, orient=tk.HORIZONTAL, command=text.xview)
        text['xscrollcommand'] = hsb.set

        # Create menu widget
        menubar = tk.Menu(window, tearoff=0)
        window['menu'] = menubar

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
        menu_file.add_command(label="Page Setup", command=self.page_setup)
        menu_file.add_command(label="Print", command=self.print)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.exit)

        # Add edit menu items
        menu_edit.add_command(label="Undo", command=self.undo)
        menu_edit.add_separator()
        menu_edit.add_command(label="Cut")
        menu_edit.add_command(label="Copy")
        menu_edit.add_command(label="Paste")
        menu_edit.add_command(label="Delete")
        menu_edit.add_separator()
        menu_edit.add_command(label="Select All")
        menu_edit.add_command(label="Time/Date")

        # Add format menu items
        menu_format.add_checkbutton(label="Word Wrap")
        menu_format.add_command(label="Font...")

        # Add view menu items
        menu_zoom = tk.Menu(menu_view, tearoff=0)
        menu_zoom.add_command(label="Zoom In")
        menu_zoom.add_command(label="Zoom Out")
        menu_zoom.add_command(label="Restore Default Zoom")
        menu_view.add_cascade(menu=menu_zoom, label="Zoom")
        menu_view.add_checkbutton(label="Status Bar")
        
        # Add help menu item
        menu_help.add_command(label="About Text Editor")

        # Add widgets to frame
        vsb.grid(row=0, column=1, sticky=tk.NS)
        hsb.grid(row=1, column=0, sticky=tk.EW)
        text.grid(row=0, column=0, sticky=tk.NSEW)

        window.mainloop()

    def run(self):
        """Loop and respond to keyboard and mouse events"""
        
    def new(self):
        """Save text file"""
        pass

    def new_window(self):
        """Save text file"""
        pass
    
    def open(self):
        """Open saved text file"""
        pass

    def save(self):
        """Save text file"""
        pass

    def save_as(self):
        """Save file as into directory of user's choice"""
        pass

    def page_setup(self):
        """Go through windows print page dialog and configure print"""
        pass

    def print(self):
        """Send text to printer"""
        pass

    def exit(self):
        """Exit text editor"""
        pass

    def undo(self):
        """Undo last edit"""
        pass

if __name__ == "__main__":
    te = TextEditor()
    te.run()