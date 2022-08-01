from overview_function import *
from valuation_function import *
from metadata_function import *
from fetch_function import *

def get_complete(ticker):
        print("complete has", ticker)
        data = get_full_data(ticker, True, True)

        analysis =[
                overview_financials(data, True),
                grahams_valuation(data, False),
                auto_dcf_formula(data, False),
                price_to_book(data, False),
                data,
                price_to_earnings(data, False),
                price_to_earnings_growth(data, False),
                get_metadata(data),
        ]

        return analysis

if __name__ == "__main__":
        print(get_complete("intc"))