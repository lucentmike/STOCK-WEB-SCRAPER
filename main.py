import requests
from selectorlib import Extractor

#Create a stock class that takes in ticker and scrapes the current price
class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def get(self):
        #runs a request method to site, grab contents, converts it into text
        request = requests.get(f"https://www.marketwatch.com/investing/stock/{self.ticker}")
        content = request.content 
        content = request.text 

        #Use yaml file to identify the x-path of the data you want
        name = Extractor.from_yaml_file('files/name.yaml')
        price = Extractor.from_yaml_file('files/price.yaml')
        change = Extractor.from_yaml_file('files/change.yaml')
        #extracts the content into variable
        price_result = price.extract(content)
        name_result = name.extract(content)
        change_result = change.extract(content)
        #extracts the number value from dictonary key
        price = price_result["temp"]
        price = price.replace(",",".")
        name = (name_result["temp"])
        change = (change_result["temp"])

        print(f"Scraping Data For: {name}")
        print(f"{name}({self.ticker.upper()}), Current Price: {price} Change: {change}\n")


if __name__ == "__main__":
    tickers = ["aapl" , "msft", "dis", "csco", "nvda", "tsla", "orcl", "hp", "jnj", "sofi", "bac", "nkla", "ms", "usb", "pg", "qs",]

    for tick in tickers:
        tick = Stock(tick)
        tick.get()

