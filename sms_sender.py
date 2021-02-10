import user_data
from twilio.rest import Client


class SendSms:
    """This class will send sms on your mobile phone"""
    def __init__(self, text: str):
        self.account_sid = user_data.twilio_account_sid
        self.auth_token = user_data.twilio_auth_token
        self.text = text
        self.send_sms()

    def send_sms(self):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            body=self.text,
            from_= user_data.twilio_from,
            to= user_data.twilio_to
        )

        print(message.status)
