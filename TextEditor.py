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
                       wrap=tk.WORD, 
                       maxundo=100, 
                       padx=10, 
                       pady=10,
                       )
        
        # Add vertical scroll bar (vsb) and tie text widget scroll to VSB
        # vertical scroll. 
        vsb = tk.Scrollbar(window, orient=tk.VERTICAL, command=text.yview)
        text['yscrollcommand'] = vsb.set

        # Create menu widget
        menubar = tk.Menu(window)
        window['menu'] = menubar
        menu_file = tk.Menu(menubar)
        menu_edit = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label="File")
        menubar.add_cascade(menu=menu_edit, label="Edit")

        # Add widgets to frame
        vsb.grid(row=0, column=1, sticky=tk.NS)
        text.grid(row=0, column=0, sticky=tk.NSEW)

        window.mainloop()

    def run(self):
        """Loop and respond to keyboard and mouse events"""

    def create_menu(self):
        """Create drop down menu for text editor"""
        pass

    def create_scrollbar(self, window):
        """Create scrollbar that appears when text exceeds window. """
        pass

    def save(self):
        """Save text file"""
        pass

    def save_as(self):
        """Save file as into directory of user's choice"""
        pass

    def open(self):
        """Open saved text file"""
        pass


if __name__ == "__main__":
    te = TextEditor()
    te.run()