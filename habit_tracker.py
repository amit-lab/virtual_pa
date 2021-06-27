import requests
import datetime

class HabitTracker:

    def __init__(self):
        # Variables
        self.status = self.check_data()
        self.user_status = None
        self.graph_status = None
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_colors = {
            'green': 'shibafu',
            'red': 'momiji',
            'blue': 'sora',
            'yellow': 'ichou',
            'purple': 'ajisai',
            'black': 'kuro',
        }
        if self.status:
            data = self.get_data()
            self.username = data[0]
            self.token = data[1]
            self.graph_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs"

    def create_user(self, username, token):
        """ 
        This function creates a user on pixela.
        This function requires two parameters:
            username:str - This is a username for your account on pixela.
            token:str - This is used as a password in pixela.
        """
        user_params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
    
        responce = requests.post(url=self.pixela_endpoint, json=user_params)
        res = responce.text['isSuccess']
        if res == 'true':
            return True
        elif res == 'false':
            return False
        
    def create_graph(self, id_: str, graph_name: str, unit: str, type_: str, color: str):
        """This function will create new graph at pixela
           This function requires following parameters:
                id: unique id for graph,
                name: General name for that graph,
                unit of measure: measurement unit (e.g., km, minute, kilogram, etc,
                type of data: int or float,
                color of graph: (green, red, blue, yellow, purple, black) any one of these"""
    
        graph_config = {
            "id": id_,
            "name": graph_name,
            "unit": unit,
            "type": type_,
            "color": self.graph_colors[color],
        }
        headers = {
            'X-USER-TOKEN': self.token
        }
    
        responce = requests.post(
            url=self.graph_endpoint, 
            json=graph_config, 
            headers=headers
        )
        res = responce.text['isSuccess']
        if res == 'true':
            return True
        elif res == 'false':
            return False
    
    def post_pixel(self, graph_name: str, quantity: str):
        """This function will add new activity pixel at pixela at given graph id"""
        pixel_endpoint = f"{self.graph_endpoint}/{graph_name}"
        today = str(datetime.datetime.now().date())
        today = today.split('-')
        pixel_config = {
            'date': f"{today[0]}{today[1]}{today[2]}",
            'quantity': quantity,
        }
        headers = {
            "X-USER-TOKEN": self.token
        }
     
        responce = requests.post(
            url=pixel_endpoint, json=pixel_config, headers=headers)
        res = responce.text['isSuccess']
        if res == 'true':
            return True
        elif res == 'false':
            return False

    def store_data(self, username, token):
        with open("data/habit_track_user", 'w') as f:
            f.write(username+'\n'+token)

    def get_data(self):
        with open("data/habit_track_user", 'r') as f:
            return f.readlines()

    def check_data(self):
        try:
            with open("data/habit_track_user", 'r') as _:
                return True
        except FileNotFoundError:
            return False

