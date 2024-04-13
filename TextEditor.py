import tkinter as tk
import time #TODO: Temporary library call for testing. 

"""Imitation program of the text editor for windows."""

class TextEditor():
    def __init__(self) -> None:
        """Initialize Text Editor"""
        window = tk.Tk()

        window.geometry("800x800")
        tk.Label(text="Text Editor").pack()
        tk.Entry().pack()
        window.mainloop()

    def run(self):
        """run Tkinter and create window"""
        # try:
        #     while True:
        #         print("hello!")
        #         time.sleep(3)
        # except KeyboardInterrupt:
        #     exit

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