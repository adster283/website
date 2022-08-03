from quickfs import QuickFS
import json
import os

keys = (
"ace8e5cc432ade6f056128c64543f154e16632ca",
"8d72fae71db051746ed3b6bee1e9c6a5f6544fd1",
"7df284372b2e30d50d36c6a81b1140b55bdfb3c8",
"edec86143897497c44c66e0c1fa5cb1886c67df2",
)



client = QuickFS(keys[0])

def get_symbols():
    """
    Returns all the supported tickers.
    Returns:
        list object with all possible tickers.
    """
    exchanges_list = (('US','NYSE'), ('US','NASDAQ'), ('US','OTC'), ('US','NYSEARCA'), ('US','BATS'), ('US','NYSEAMERICAN'), ('AU','ASX'), ('NZ', 'NZX'))
    complete_ticker_list = []
    try:
        for i in exchanges_list:
            print("fetching",  i[0], i[1], "tickers...")
            resp = client.get_supported_companies(country=i[0], exchange=i[1])
            complete_ticker_list.append(resp)
        return complete_ticker_list
    except:
        print("...unable to gather supported tickers at this time...")
        return "NA"


def get_full_data(symbol, save=False, respond=True):
    """
    Function fetches all data related to the given ticker symbol and returns a dict.
    Arguments:
        symbol: the ticker that needs to be fetched
        save: save to a json file for testing (optional)
        respond: if set to false the function will not return anything
    Returns:
        Reuturns dict of all available data.
    """
    try:
        data = client.get_data_full(symbol=symbol)
        print(client.get_usage())

        if str(client.resp) == "<Response [200]>":
            if save == True:
                with open('output.json', 'w') as outfile:
                    json.dump(data, outfile)
        else:
            pass

        if respond == True & (str(client.resp) == "<Response [200]>"):
            
            return data
        else:
            return "NA"
    except:
        print("...something went wrong getting ticker data...")

def get_current_price(symbol):
    """
    Returns the stock price at last close.
    Arguments:
        symbol: the ticker to request price of.
    Returns:
        Reuturns the price of given ticker at last close.
    """
    try:
        price = client.get_data_range(symbol=symbol, metric='price')
        if str(client.resp) == "<Response [200]>":
            return price
        else:
            return "NA"
    except:
        print("...unable to retreive current stock price...")

if __name__ == "__main__":
    print(get_full_data("pep", save=True, respond=True))
    #print(get_symbols())
