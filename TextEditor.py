import tkinter as tk

"""Imitation program of the text editor for windows."""

class TextEditor():
    def __init__(self) -> None:
        """Initialize Text Editor"""
        window = tk.Tk()
        window.title("Text Editor")

        text_widget = tk.Text(window, 
                              wrap=tk.WORD, 
                              maxundo=100, 
                              padx=10, 
                              pady=10
                              )

        text_widget.grid(row=0, column=0, sticky=tk.NSEW)
        

        window.mainloop()

    def run(self):
        """Loop and respond to keyboard and mouse events"""

    def create_menu(self):
        """Create drop down menu for text editor"""
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