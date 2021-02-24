from tkinter import *
from tkinter import messagebox
import user_data
from weather_data import WeatherData
from price_tracker import PriceTracker
import os


class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Personal Assistant")
        self.config(padx=50, pady=50)
        self.main_page()
        self.selected_site = IntVar()
        self.send_sms = IntVar()

        # Objects

        # to give padding to all widgets in window
        self.padding_adder(self)

        self.mainloop()

    def main_page(self):
        msg = Label(text="Welcome")
        msg.grid(column=0, row=0)

        # For weather btn
        weather_btn = Button(text="Weather Info",
                                command=self.weather_page,
                                bg='brown',fg='white')
        weather_btn.grid(row=1, column=0)
        # For price tracker
        price_tracker_btn = Button(self,
                                    text="Price Tracker",
                                    command=self.price_track_page,
                                    bg='brown',fg='white')

    def weather_page(self):
        print(self.weather_data_obj.get_data())

    def price_track_page(self):
        """This methiod creates the window for price tracker for amazon or flipkart"""
        def destroy_win():
            track_win.destroy()

        def store_data():
            url = url_entry.get()
            price = price_entry.get()
            price_tracker.save_url(url, price)
            track_win.destroy()
            self.price_track_page()

        def confirm_msg():
            msg = messagebox.askquestion('Warning', 
                    'Are you sure you want to chenge url ?', icon='warning')
            if msg == 'yes':
                track_win.destroy()
                change_url()

        def change_url():
            os.system('rm url.txt')
            self.price_track_page()

        price_tracker = PriceTracker()
        track_win = Tk()
        track_win.title("Price Tracker")
        track_win.config(padx=50, pady=50)

        # if url does not exist already
        if not price_tracker.status:
            Label(track_win, text="Welcome").grid(row=0, column=0, columnspan=2)
            Label(track_win, text="Enter url bellow : ").grid(row=1, column=0, columnspan=2)
            url_entry = Entry(track_win, width=30)
            url_entry.grid(row=2, column=0, columnspan=2)
            Label(track_win, text="Desired Price").grid(row=3, column=0, columnspan=2)
            price_entry = Entry(track_win, width=10)
            price_entry.grid(row=4, column=0, columnspan=2)
            #Label(track_win, text="Which website is this url from:").grid(row=4, column=0, columnspan=2)
            #flipkart = Radiobutton(track_win,
            #                        text="Flipkart ",
            #                        variable=self.selected_site,
            #                        value=0)
            #flipkart.grid(row=5, column=0)
            #amazon = Radiobutton(track_win,
            #                        text="Amazon ", 
            #                        variable=self.selected_site, 
            #                        value=1)
            #amazon.grid(row=5, column=1)
            #Label(track_win, text="Should we notify you through sms ?").grid(row=6, column=0, columnspan=2)
            #sel_yes = Radiobutton(track_win, text="Yes", variable=self.send_sms, value=1)
            #sel_yes.grid(row=7, column=0)
            #sel_no = Radiobutton(track_win, text="No", variable=self.send_sms, value=0)
            #sel_no.grid(row=7, column=1)
            Button(track_win, text="Done", command=store_data).grid(row=8, column=0, columnspan=2)

        # if url exist already
        else:
            data = price_tracker.check_price()
            Label(track_win, text="Product Name ").grid(row=0, column=0, columnspan=2)
            product_name_label = Label(track_win, text=f"{data['product name']}")
            product_name_label.grid(row=1, column=0, columnspan=2)
            cur_price = Label(track_win,
                                text=f"Current Price : Rs. {data['current price']}")
            cur_price.grid(row=2, column=0)
            des_price = Label(track_win,
                                text=f"Desired Price : Rs. {data['desired price']}")
            des_price.grid(row=3, column=0)
            is_low = Label(track_win,
                                text=f"Is price low   : {data['price low']}          ")
            is_low.grid(row=4, column=0)
            Button(track_win,
                    text="Ok",
                    command=destroy_win,
                    bg='brown',
                    fg='white').grid(row=5, column=0)
            Button(track_win,
                    text="Change url",
                    bg='brown',fg='white',
                    command=confirm_msg).grid(row=5, column=1)

        #self.padding_adder(track_win)


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
        Label(entry_window,
                text="Enter Your api keys and urls here").grid(row=0, column=0, columnspan=3)
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

    def padding_adder(self, obj):
        for child in obj.winfo_children():
            child.grid_configure(padx=10, pady=10)


