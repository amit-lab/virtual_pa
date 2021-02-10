import user_data
from twilio.rest import Client


class SendSms:
    def __init__(self, text: str):
        self.account_sid = user_data.twilio_account_sid
        self.auth_token = user_data.twilio_auth_token
        self.text = text
        self.send_sms()

    def send_sms(self):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            body=self.text,
            from_="+19388883662",
            to="+917020894348"
        )

        print(message.status)
