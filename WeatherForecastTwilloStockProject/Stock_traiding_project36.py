import requests
from twilio.rest import Client
from datetime import datetime, timedelta

#all apikey must be your

COMPANY_NAME = "Tesla Inc"
symbol = "TSLA"
apikey = "apikey"

news_apikey = "news_apikey"
URL_NEWS = "URL news"

account_sid = "your account_sid"
auth_token = "your twillo auth_token"
trial_phone = "Your twillo trial_phone"


params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': symbol,
    'apikey': apikey,
}

response = requests.get(url='https://www.alphavantage.co/query', params=params)
data = response.json()['Time Series (Daily)']
print(data)
# When STOCK price increase/decreases by 4% between yesterday and the day before yesterday then print("Get News").
#today = datetime.now()
#yesterday = (today - timedelta(days=1)).strftime('%Y-%m-%d')
#day_before_yesterday = (today - timedelta(days=2)).strftime('%Y-%m-%d')

daily_data = [value for(key,value) in data.items()]
yesterday_data = daily_data[0]
yesterday_price = yesterday_data['4. close']
day_before_yesterday_data = daily_data[1]
day_before_yesterday_price = day_before_yesterday_data['4. close']

stock_growth = (abs((float(yesterday_price) - float(day_before_yesterday_price)) / float(day_before_yesterday_price)) * 100)
print(stock_growth)

if stock_growth > 3:
    news_params = {"qInTitle": COMPANY_NAME,
                   "apiKey": news_apikey,
                   }
    response = requests.get(url=URL_NEWS, params=news_params)
    news_data = response.json()["articles"]
    articles = news_data[1:4]
    print(articles)
    message = [f"Headline:{article['title']}. \nBrief: {article['description']}" for article in articles]
    print(message)
    client = Client(account_sid, auth_token)
    for article in articles:
        message = client.messages.create(
            body=article,
            from_=trial_phone,
            to="Phone number",
        )
    print(message.status)
else:
    print("No")