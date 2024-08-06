import requests
COMPANY_NAME = "Tesla Inc"
news_apikey = "news_apikey"
URL = "https://newsapi.org/v2/everything"

# get the first 3 news pieces for the COMPANY_NAME.
class Get_News():
    news_params = {"qInTitle":COMPANY_NAME,
            "apiKey":news_apikey,
    }
    response = requests.get(url=URL, params=news_params)
    news_data = response.json()["articles"]
    articles  =  news_data[0:3]
    message = [f"Headline:{article['title']}. \nBrief: {article['description']}"for article in articles]


