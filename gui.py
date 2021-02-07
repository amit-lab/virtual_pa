from tkinter import Tk, Label


class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Personal Assistant")
        self.config(padx=50, pady=50)
        self.main_page()

        self.mainloop()

    def main_page(self):
        msg = Label(text="Welcome")
        msg.grid(column=0, row=0)
