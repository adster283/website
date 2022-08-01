from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from lxml import html, etree

def get_trending_tickers():

    url = "https://www.tipranks.com/compare-stocks/value"

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"}
    webpage = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"})

    soup = BeautifulSoup(webpage.content, "html.parser") 

    dom = etree.HTML(str(soup)) 

    try:
        tickers ={
        "0" : (dom.xpath('//*[@id="root"]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/div/a')[0].text ),
        "1" : (dom.xpath('//*[@id="root"]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/table/tbody/tr[2]/td[1]/div/div/a')[0].text ),
        }
    except:
        tickers={"0": "NA","1": "NA"}

    print("tickers:", tickers)
    return tickers

def convert_ticker(ticker):
    print("converter received", ticker)
    if ":" in ticker:
        pos = ticker.find(":")
        if ticker[pos+1:] == "au":
            ticker = ticker[:pos] + "." + "ax"
        else:
            ticker = ticker[:pos] + "." + ticker[pos+1:]

    print("converter returning", ticker)
    return ticker

def get_current_price_yahoo(ticker):
    ticker = convert_ticker(ticker)

    url = f"https://nz.finance.yahoo.com/quote/{ticker}"

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"}
    webpage = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"})

    soup = BeautifulSoup(webpage.content, "html.parser") 

    dom = etree.HTML(str(soup)) 

    print("prices scrape using", ticker)

    try:
        try:
            prices = {
            "price" : (dom.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')[0].text ),
            "price_change" : (dom.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[3]/span')[0].text )
            }
        except:
            prices = {
            "price" : (dom.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text ),
            "price_change" : (dom.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[3]/span')[0].text )
            }
    except:
        prices = {"price": "NA", "price_change": "NA"}

    print(prices)
    return prices

def get_current_estimate(ticker):
    ticker = convert_ticker(ticker)


    url = f"https://nz.finance.yahoo.com/quote/{ticker}/analysis"

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"}
    webpage = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"})

    soup = BeautifulSoup(webpage.content, "html.parser") 

    dom = etree.HTML(str(soup)) 

    try:
        growth = (dom.xpath('//*[@id="Col1-0-AnalystLeafPage-Proxy"]/section/table[6]/tbody/tr[5]/td[2]')[0].text )
    except:
        growth = "NA"

    return float((growth[:-1]))/100

def get_current_div(ticker):
    ticker = convert_ticker(ticker)


    url = f"https://nz.finance.yahoo.com/quote/{ticker}"

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"}
    webpage = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"})

    soup = BeautifulSoup(webpage.content, "html.parser") 

    dom = etree.HTML(str(soup)) 

    try:
        div = (dom.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]')[0].text )
    except:
        div = "NA"

    return div

def get_current_ratios(ticker):
    ticker = convert_ticker(ticker)


    url = f"https://nz.finance.yahoo.com/quote/{ticker}/key-statistics"

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"}
    webpage = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition std-1)"})

    soup = BeautifulSoup(webpage.content, "html.parser") 

    dom = etree.HTML(str(soup)) 

    try:
        ratios={
        "pe" : (dom.xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[3]/td[2]')[0].text ),
        "pb" : (dom.xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[7]/td[2]')[0].text ),
        "peg" : (dom.xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[5]/td[2]')[0].text )
        }
    except:
        ratios = {"pe": "NA", "pb": "NA", "peg":"NA"}
        
    return ratios


if __name__ == "__main__":
    ticker = "fph:nz"
    if ":" in ticker:
        print(ticker)
        pos = ticker.find(":")
        ticker = ticker[:pos] + "." + ticker[pos+1:]
        print(ticker)
    get_current_price("fph.nz")
    print(get_current_estimate("fph.nz"))