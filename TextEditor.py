import tkinter as tk
import tkinter.scrolledtext as scrolledtext

"""Imitation program of the text editor for windows."""

class TextEditor():
    def __init__(self) -> None:
        """Initialize Text Editor"""
        window = tk.Tk()
        window.title("Text Editor")
        window.grid_propagate(False)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.geometry("1200x720")

        # Create ScrolledText within window
        st = scrolledtext.ScrolledText(window)

        # Create text widget to contain user keyboard input
        text = tk.Text(window, 
                       wrap=tk.WORD, 
                       maxundo=100, 
                       padx=10, 
                       pady=10,
                       )
        
        # Add vertical scroll bar (vsb)
        vsb = tk.Scrollbar(window, orient=tk.VERTICAL, command=text.yview)
        text['yscrollcommand'] = vsb.set

        vsb.grid(row=0, column=1, sticky=tk.E)
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