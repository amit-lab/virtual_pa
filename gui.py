from tkinter import *
from user_data import UserData


class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Personal Assistant")
        self.config(padx=50, pady=50)
        self.main_page()
        self.user_data = UserData()

        # to give padding to all widgets in window
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)
        self.mainloop()

    def main_page(self):
        msg = Label(text="Welcome")
        msg.grid(column=0, row=0)
        btn = Button(text="Insert Data", command=self.data_entry)
        btn.grid(column=0, row=1)

    def data_entry(self):
        """This function creates the window where you can enter your api keys and urls"""

        def insert_data():
            """This function puts all data into database and destroy the window"""
            self.user_data.insert_data(
                url_id=open_weather_id,
                url=open_weather_url.get(),
                api_key=open_weather_api_key.get()
            )
            entry_window.destroy()

        # Heading of the window
        entry_window = Tk()
        entry_window.title("Entry Window")
        entry_window.config(padx=20, pady=20)
        Label(entry_window, text="Enter Your api keys and urls here").grid(row=0, column=0, columnspan=3)
        Label(entry_window, text="URL").grid(row=1, column=1)
        Label(entry_window, text="API key").grid(row=1, column=2)

        # Open weather
        open_weather_id = 0
        Label(entry_window, text="Open Weather").grid(row=2, column=0)
        open_weather_url = Entry(entry_window, width=20)
        open_weather_url.grid(row=2, column=1)
        open_weather_api_key = Entry(entry_window, width=20)
        open_weather_api_key.grid(row=2, column=2)

        submit_btn = Button(entry_window, text="Submit", bg='green', command=insert_data)
        submit_btn.grid(row=3, column=0, columnspan=3)
        # to give padding to all widgets in window
        for child in entry_window.winfo_children():
            child.grid_configure(padx=10, pady=10)


