"""
Author: Viktor Basharkevich
This script pulls data about stock prices via yahoo finance's Python API.
It is used by the GUI to get data about certain stocks.

What program will do:
Get stock data (Webscraping and pandas part)
Display a graph (Matplotlib part or/and pyqt5)
Create a line for or predict the stock price.
It would be nice to be all wrapped up in a GUI
"""
import matplotlib
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import style
from matplotlib import dates
import datetime
from datetime import date
import matplotlib.dates
import plotly.graph_objects as go
import plotly
import py


# This is our class that will get data for a stock and use pandas to create/read csv files
class YahooStockInfo:
    def __init__(self, name):  # Initiates object and calls other functions to make more attributes
        self.name = name  # Name (ex: SPY)
        self.createData()  # Creates the csv file with stock info
        self.StockPriceHigh1Y()  # Creates attribute stock_high_1y with 1 year high
        self.StockPriceLow1Y()  # Creates attribute stock_low_1y with 1 year low
        self.LatestPrice()  # Returns latest price of stock

    @property  # Creates the actual yfinance object with all the info
    def Yahoo_Obj(self):
        return yf.Ticker(self.name)

    @property  # Filename of the csv file holding daily info of the stock
    def file_name(self):
        return self.name + "_data_base.csv"

    def createData(self):  # Creates csv file inside Databases directory for holding info of the stock
        hist_1y = self.Yahoo_Obj.history(period="1y")
        data_frame = pd.DataFrame(data=hist_1y)
        self.path_for_csv = "Databases\\" + self.file_name
        data_frame.to_csv(self.path_for_csv)

    def StockPriceHigh1Y(self):  # Finds the highest price since 1Y and sets it as an attribute
        data = pd.read_csv(self.path_for_csv)
        stockprices = np.array(data["Close"])
        self.stock_high_1y = stockprices.max()

    def StockPriceLow1Y(self):  # Finds the lowest price since 1Y and sets it as an attribute
        data = pd.read_csv(self.path_for_csv)
        stockprices = np.array(data["Close"])
        self.stock_low_1y = stockprices.min()

    def LatestPrice(self):  # Finds the price of closing from yesterday and sets it as an attribute
        data = pd.read_csv(self.path_for_csv)
        stockprices = np.array(data["Close"])
        self.stock_closing_price = stockprices[-1]

    def GoingUpOrDown(self):  # Returns if the stock has had more up or down days
        data = pd.read_csv(self.path_for_csv)
        stockprices = np.array(data["Close"])
        up_day = 0
        down_day = 0
        for i in range(1, len(stockprices)):
            if stockprices[i] > stockprices[i-1]:
                up_day += 1
            elif stockprices[i] < stockprices[i-1]:
                down_day += 1
        if up_day > down_day:
            return "Up " + str(up_day) + " out of " + str(len(stockprices)) + " days."
        if up_day < down_day:
            return "Down " + str(down_day) + " out of " + str(len(stockprices)) + " days."
        if up_day == down_day:
            return "No gain. As many down days as up days."

    def ReturnGraph(self):
        hist_1y = self.Yahoo_Obj.history(period="1y")
        return pd.DataFrame(data=hist_1y)


def main():  # Used for on the fly testing to see if things work.

    UBER = YahooStockInfo("UBER")
    SPY = YahooStockInfo("SPY")
    # UBER.ReturnGraph()



    # Testing, plotly and matplotlib graphs. Non-essential and just for testing things out
    """
    SPY = YahooStockInfo("SPY")
    print(SPY.stock_high_1y)
    print(SPY.GoingUpOrDown())
    data = pd.read_csv(SPY.file_name)

    # This uses plotly to show a stock in a stock graph that is in html and is interactive
    fig = go.Figure(data=[go.Candlestick(x=data["Date"],
                                         open=data["Open"],
                                         high=data["High"],
                                         low=data["Low"],
                                         close=data["Close"])])
    # fig.show()  # Shows the html file in browser (not downloaded)
    plotly.offline.plot(fig, filename='graph.html')  # saves the plotly graph to the machine as .html

    # This shows a tock chart using matplotlib (not that great)
    style.use("ggplot")
    matplotlib.pyplot.plot_date(data["Date"], data["Close"])
    pyplot.show()"""


if __name__ == "__main__":
    main()


"""
SPY = yf.Ticker("SPY")
short_hist = SPY.history(period="14d")
long_hist = SPY.history(period="max")




# spy_file.write(long_hist)
# spy_file.close()
print(date.today())# df = pd.DataFrame(data=long_hist)
# df.to_csv("spy_data.csv")


style.use("ggplot")
# pyplot.scatter(df["Stock"], df["Close"])
pyplot.show()"""
