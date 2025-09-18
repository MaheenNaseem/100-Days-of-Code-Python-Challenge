import requests
import os
import smtplib

STOCK =  "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY= os.environ.get("STOCK_API_KEY")
NEWS_API_KEY= os.environ.get("NEWS_API_KEY")

my_email = "YOUR_EMAIL_ADDRESS"
my_password = "YOUR_EMAIL_PASSWORD"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}

stock_response = requests.get(url = "https://www.alphavantage.co/query", params = stock_parameters)
stock_response.raise_for_status()

# saves time series data from the fetched json
stock_data = stock_response.json()["Time Series (Daily)"]

# creates list of dictionary for the values fetched from stock data
data_list = [value for (key,value) in stock_data.items()]

# For getting previous days full formatted dates (such as; 2025-09-18)
yesterday_date = data_list[1]
day_before_yesterday_date = data_list[2]

# For fetching closing prices for previous days
yesterday_closing = float(yesterday_date['4. close'])
day_before_yesterday_closing =  float(day_before_yesterday_date['4. close'])

print(yesterday_closing, day_before_yesterday_closing)

# finding difference in stock price
difference = yesterday_closing - day_before_yesterday_closing

# calculate percentage and round the value
difference_percentage =round(((difference/yesterday_closing) * 100), 2)

# check if STOCK price increase/decreases by 5% between yesterday and the day before yesterday
if abs(difference_percentage) > 5:

    arrow = ""
    if difference > 0:
        arrow = "🔺"
    else:
        arrow = "🔻"

    news_parameters = {
        "q": STOCK,
        "language" : "en",
        "apiKey": NEWS_API_KEY
    }
  
    news_response = requests.get(url = "https://newsapi.org/v2/everything", params= news_parameters)
    news_response.raise_for_status()
	
    news_data = news_response.json()

    #saves the 3 articles from the news_data
    three_news_pieces_list = news_data["articles"][0:3]

    #creates a dictionary for title and description of the 3 articles
    news_data_dict = [
        {
            "title": three_news_pieces_list[data]['title'],
            "description": three_news_pieces_list[data]['description']
        } for data in range(len(three_news_pieces_list))
    ]

    with smtplib.SMTP("<---HOST--->", <---PORT--->) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        # send emails
        for i in range(len(news_data_dict)):
            message = (f"Subject: {COMPANY_NAME}{arrow} {difference_percentage}%\n\n"
                       f"Heading: \n{news_data_dict[i]['title']}\nDescription: \n{news_data_dict[i]['description']}")

            try:
                connection.sendmail(
                    from_addr=<---YOUR EMAIL--->,
                    to_addrs=<---RECIPENT EMAIL--->,
                    msg = message.encode('utf-8')
                )
            except smtplib.SMTPException as e:
                print(f"Mails {i} was not delivered.", e )
            else:
                print(f"Mails {i} delivered.")
