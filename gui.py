from tkinter import *
from tkinter import messagebox
from weather_data import WeatherData
from price_tracker import PriceTracker
from habit_tracker import HabitTracker
from nlp import Nlp
import os


class Gui(Tk):
    def __init__(self):
        super().__init__()

    def run(self):
        self.title("Virtual Personal Assistant")
        self.config(padx=50, pady=50)
        self.resizable(0, 0)
        self.main_page()
        self.selected_site = IntVar()
        self.send_sms = IntVar()

        # to give padding to all widgets in window
        self.padding_adder(self)

        self.mainloop()

    def main_page(self):

        def launch_gui_win():
            self.destroy()
            self.gui_page()

        def launch_nlp_win():
            self.destroy()
            self.nlp_page()

        def voice_cmd_mode():
            from voice_recognition import VoiceRecognition
            self.destroy()
            vr = VoiceRecognition(self)
            vr.run()

        gui_btn = Button(self,
                         text="GUI MODE",
                         padx=20, pady=20,
                         bg='brown', fg='white',
                         command=launch_gui_win
                         )
        nlp_btn = Button(self,
                         text="COMMAND MODE",
                         padx=20, pady=20,
                         bg='brown', fg='white',
                         command=launch_nlp_win
                         )
        voice_btn = Button(self,
                           text="VOICE COMMAND MODE",
                           padx=20, pady=20,
                           bg='brown', fg='white',
                           command=voice_cmd_mode
                           )
        gui_btn.grid(row=1, column=0)
        nlp_btn.grid(row=1, column=1)
        voice_btn.grid(row=2, column=0, columnspan=2)

    def nlp_page(self):

        def destroy_win():
            nlp_win.destroy()

        def launch():
            text = search_entry.get()
            nlp_obj.other_launcher(text)
            nlp_obj.gui_launcher(text, self)
            nlp_obj.query(text)

        def switch_to_gui():
            self.gui_page()
            nlp_win.destroy()

        def go_to_menu():
            self.__init__()
            self.main_page()
            nlp_win.destroy()

        nlp_obj = Nlp()
        nlp_win = Tk()
        nlp_win.title("VPA Command Window")
        nlp_win.config(padx=30, pady=30)
        info_label = Label(nlp_win, text="Insert what you want in search box \n", fg='green', bg='white')
        info_label.grid(row=0, column=0, columnspan=2)
        search_entry = Entry(nlp_win, width=50)
        search_entry.grid(row=1, column=0, columnspan=2)
        search_btn = Button(nlp_win,
                            text="GO",
                            padx=22,
                            bg='brown', fg='white',
                            command=launch
                            )
        search_btn.grid(row=2, column=0, columnspan=2)
        #mic_btn = Button(nlp_win, text="MIC", padx=20, bg='brown', fg='white')
        #mic_btn.grid(row=3, column=0, columnspan=2)
        #main_menu_btn = Button(nlp_win,
        #                       text="Return to main menu",
        #                       padx=20,
        #                       bg='brown', fg='white',
        #                       command=go_to_menu
        #                       )
        #main_menu_btn.grid(row=4, column=0)
        #gui_mode_btn = Button(nlp_win,
        #                      text="Switch to GUI",
        #                      bg='brown', fg='white',
        #                      padx=20,
        #                      command=switch_to_gui
        #                      )
        #gui_mode_btn.grid(row=4, column=1)

    def gui_page(self):

        def destroy_win():
            gui_win.destroy()

        gui_win = Tk()
        gui_win.title("VPA GUI")
        gui_win.config(padx=30, pady=30)

        msg = Label(gui_win, text="Welcome")
        msg.grid(column=0, row=0)

        # For weather btn
        weather_btn = Button(gui_win, text="Weather Info",
                             command=self.weather_page,
                             bg='brown', fg='white')
        weather_btn.grid(row=1, column=0)
        # For price tracker
        price_tracker_btn = Button(gui_win,
                                   text="Price Tracker",
                                   command=self.price_track_page,
                                   bg='brown', fg='white')
        price_tracker_btn.grid(row=2, column=0)
        #habit_tracker_btn = Button(gui_win,
        #                           text="System management",
        #                           command=self.system_admin_page,
        #                           bg='brown', fg='white')
        #habit_tracker_btn.grid(row=3, column=0)

    def weather_page(self):

        def destroy_win():
            weather_win.destroy()

        def store_names():
            weather_data.save_names(city_entry.get(), country_entry.get())
            weather_win.destroy()
            self.weather_page()

        def confirm_msg():
            msg = messagebox.askquestion('Warning',
                                         'Are you sure you want to chenge city name ?', icon='warning')
            if msg == 'yes':
                weather_win.destroy()
                change_names()

        def change_names():
            os.system("rm weather.txt")
            self.weather_page()

        data = None
        weather_data = WeatherData()
        weather_win = Tk()
        weather_win.title("Weather Forcast Information")
        weather_win.config(padx=30, pady=30)
        weather_win.resizable(0, 0)

        if not weather_data.status:
            Label(weather_win, text="Welcome").grid(
                row=0, column=0, columnspan=2)
            Label(weather_win,
                  text="Enter your location detail here").grid(row=1, column=0, columnspan=2)
            Label(weather_win,
                  text="City name : ").grid(row=2, column=0)
            city_entry = Entry(weather_win, width=20)
            city_entry.grid(row=2, column=1)
            Label(weather_win, text="Country name : ").grid(row=3, column=0)
            country_entry = Entry(weather_win, width=20)
            country_entry.grid(row=3, column=1)
            Button(weather_win,
                   text="Done",
                   command=store_names, bg='brown', fg='white').grid(row=8, column=0, columnspan=2)

        else:
            data = weather_data.get_current_data()
            will_rain = weather_data.rain_alert()
            Label(weather_win,
                  text="Current Weather Forcast").grid(row=0, column=0, columnspan=2)
            Label(weather_win,
                  text=f"Temperature   :   ").grid(row=1, column=0)
            Label(weather_win, text=f"{data['temp']} C").grid(row=1, column=1)
            Label(weather_win,
                  text=f"Wind              : ").grid(row=2, column=0)
            Label(weather_win, text=f"{data['wind speed']['speed']}  m/s").grid(row=2, column=1)
            Label(weather_win, text=f"Status            :").grid(row=3, column=0)
            Label(weather_win, text=f"{data['status']}").grid(row=3, column=1)
            Button(weather_win,
                   text="Ok",
                   command=destroy_win,
                   bg='brown',
                   fg='white').grid(row=4, column=0)
            Button(weather_win,
                   text="Change city name",
                   bg='brown', fg='white',
                   command=confirm_msg).grid(row=4, column=1)

    def price_track_page(self):
        def destroy_win():
            track_win.destroy()

        def store_data():
            url1 = flipkart_url.get()
            url2 = amazon_url.get()
            # url3 = snapdeal_url.get()
            price = price_entry.get()
            data = [url1, url2, price]
            price_tracker.save_url(data)
            track_win.destroy()
            self.price_track_page()

        def confirm_msg():
            msg = messagebox.askquestion('Warning',
                                         'Are you sure you want to chenge url ?', icon='warning')
            if msg == 'yes':
                track_win.destroy()
                change_url()

        def change_url():
            os.system('rm data/url.txt')
            track_win.destroy()
            self.price_track_page()

        price_tracker = PriceTracker()
        track_win = Tk()
        track_win.title("Price Tracker")
        track_win.config(padx=10, pady=10)
        track_win.resizable(0, 0)
        # bg = PhotoImage(master=track_win, file="./data/card_back.png")
        # Label(track_win, image=bg).place(x=0, y=0)

        # if url does not exist already
        if not price_tracker.status:
            Label(track_win, text="Welcome").grid(
                row=0, column=0, columnspan=2)
            Label(track_win, text="Enter url from Flipkart bellow : ").grid(
                row=1, column=0, columnspan=2)
            Label(track_win, text="Enter url from Amazon bellow : ").grid(
                row=3, column=0, columnspan=2)
            # Label(track_win, text="Enter url from Snapdeal bellow : ").grid(row=5, column=0, columnspan=2)
            flipkart_url = Entry(track_win, width=30)
            amazon_url = Entry(track_win, width=30)
            # snapdeal_url = Entry(track_win, width=30)
            flipkart_url.grid(row=2, column=0, columnspan=2)
            amazon_url.grid(row=4, column=0, columnspan=2)
            # snapdeal_url.grid(row=6, column=0, columnspan=2)
            Label(track_win, text="Desired Price").grid(
                row=7, column=0, columnspan=2)
            price_entry = Entry(track_win, width=10)
            price_entry.grid(row=8, column=0, columnspan=2)
            Button(track_win, text="Done", command=store_data,
                   bg='brown', fg='white').grid(row=9, column=0)
            Button(track_win,
                   text="Cancel",
                   command=destroy_win, bg='brown', fg='white').grid(row=9, column=1)
        #
        # if url exist already
        else:
            data = price_tracker.get_data()
            # Labels:
            # for amazon
            Label(track_win, text="PRICE TRACKER", fg='green',
                  pady=10).grid(row=0, column=0, columnspan=4)
            Label(track_win, text="Amazon", padx=150).grid(row=1, column=0)
            Label(track_win, text=f"Product Name : {data['amazon'][0]}").grid(
                row=2, column=0)
            Label(track_win, text=f"Current Price: {data['amazon'][1]}").grid(
                row=3, column=0)
            # for flipkart
            Label(track_win, text="Flipkart", padx=150).grid(row=1, column=1)
            Label(track_win, text=f"Product Name : {data['flipkart'][0]}").grid(
                row=2, column=1)
            Label(track_win, text=f"Current Price: {data['flipkart'][1]}").grid(
                row=3, column=1)
            # for extra info
            Label(track_win, text=f"Desired Price: {data['desired price']}").grid(
                row=4, column=0, columnspan=3)
            Label(track_win, text=f"Lowest Price website : {data['low price website']}").grid(
                row=5, column=0, columnspan=3)
            Label(track_win,
                  text=f"Is price lower than desired price : {data['is low']}").grid(row=6, column=0, columnspan=3)
            Button(track_win, text='Ok', command=destroy_win, bg='brown',
                   fg='white').grid(row=7, column=0, columnspan=3)
            Button(track_win, text='Change urls', command=change_url,
                   bg='brown', fg='white').grid(row=8, column=0, columnspan=3)

    def habit_track_page(self):
        def destroy_win():
            track_win.destroy()

        def store_data():
            username = user_name_entry.get()
            token = token_entry.get()
            tracker.store_data(username, token)
            track_win.destroy()

        track_win = Tk()
        track_win.title("habit Tracker")
        track_win.config(padx=10, pady=10)
        track_win.resizable(0, 0)
        tracker = HabitTracker()

        # TODO: Create user window
        Label(track_win, text="Create a user in pixela",
              pady=10).grid(row=0, column=0, columnspan=3)
        Label(track_win, text="User Name : ").grid(row=1, column=0)
        user_name_entry = Entry(track_win, width=20)
        user_name_entry.grid(row=1, column=1)
        Label(track_win, text="Token : ").grid(row=2, column=0)
        token_entry = Entry(track_win, width=20)
        token_entry.grid(row=2, column=1)
        Button(track_win, text="Create user", command=store_data,
               bg='brown', fg='white').grid(row=3, column=0)
        Button(track_win, text="Cancel", command=destroy_win,
               bg='brown', fg='white').grid(row=3, column=1)
        # TODO: Create graph with id window

    def system_admin_page(self):
        pass

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
        entry_window.resizable(0, 0)
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

        submit_btn = Button(entry_window, text="Submit",
                            command=insert_data, bg='brown', fg='white')
        submit_btn.grid(row=3, column=0, columnspan=3)
        # to give padding to all widgets in window
        for child in entry_window.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def padding_adder(self, obj):
        for child in obj.winfo_children():
            child.grid_configure(padx=10, pady=10)
