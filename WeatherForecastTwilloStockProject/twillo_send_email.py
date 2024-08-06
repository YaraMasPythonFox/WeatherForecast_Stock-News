import requests
from twilio.rest import Client
from Get_news_about_stocks_company import Get_News

account_sid = "Your twillo cid"
auth_token = "Your twillo  auth_token"
trial_phone = "Your twillo trial_phone"


class Send_SMS():

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="message",
        from_=trial_phone,
        to="Your phone",
    )
    print(message.status)

