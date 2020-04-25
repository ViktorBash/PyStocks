"""
Will return name when given ticker symbol of a company's stock, (for companies on NASDAQ/NYSE)
To use: import the script, then:
Object_name = TickerToName(ticker)
Then just do Object_name.self.company_name and that gives the company name
Example: Inputting in GOOG returns Alphabet Inc
"""

import pandas as pd
import numpy as np

# We read in a csv for both the NYSE and NASDAQ that holds a list of stocks. Then we make these numpy arrays
NASDAQ_dataframe = pd.read_csv("NASDAQ_List.csv")
NYSE_dataframe = pd.read_csv("NYSE_List.csv")

NYSE_dataframe = NYSE_dataframe[["Symbol", "Name"]]
NYSE_dataframe_np = np.array(NYSE_dataframe)

NASDAQ_dataframe = NASDAQ_dataframe[["Symbol", "Name"]]
NASDAQ_dataframe_np = np.array(NASDAQ_dataframe)


# This class takes in a ticker name and returns the name of the company. It can later be expanded to return more info.
class TickerToName:
    # Initialization, will only have one parameter (ticker name)
    def __init__(self, ticker):
        self.ticker = ticker
        self.ReturnTicker()

    # Makes self.company_name equal to the name of the company. If ticker doesn't match in either np array, then
    # company_name is simply set to the ticker name that was inputted.
    def ReturnTicker(self):
        for i in range(0, len(NYSE_dataframe_np)):
            if self.ticker == NYSE_dataframe_np.item(i, 0):
                self.company_name = str(NYSE_dataframe_np.item(i, 1))
                return ""

        for i in range(0, len(NASDAQ_dataframe_np)):
            if self.ticker == NASDAQ_dataframe_np.item(i, 0):
                self.company_name = NASDAQ_dataframe_np.item(i, 1)
                return ""
        else:
            self.company_name = self.ticker


# Testing environment
def main():
    BBQ_corp = TickerToName("BBQ")
    print(BBQ_corp.company_name)


if __name__ == "__main__":
    main()
