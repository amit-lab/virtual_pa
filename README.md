# virtual Personal Assistant

Requirements :
To install required python modules use following command:
    
    pip3 install tk twilio speech_recognition requests lxml beautifulsoup4
    
    
Step 1: get your api keys:
i) Go on the site : "https://openweathermap.org/api" and create account or log in if you have one and go to api section and get api key
and past it into user_data.py 
ii) Go on the site : "https://www.twilio.com/docs/usage/api" and create account or log in if you have one and go to api section and get the following data
    -> twilio_account_sid
    -> twilio_auth_token
    -> twilio_from
    -> twilio_to (your mobile number)
 and fill this information into user_data.py
 
 
Step2: run main.py
In this, if you are using non gui system (like if you are using putty or other ssh client) then it will automatically enter into voice command mode.
