import json
from scrape_yahoo_finance import *
from fetch_function import *

def price_to_earnings_growth(data, visual=True):
    """
    Returns an overview of the historic peg ratio for the company.
    Arguments:
        data: json file containing all the data for the given company
        visual: if true will print out to the terminal
    Returns:
        Returns the current, lowest and average peg ratio.
    """
    try:
        peg = data["financials"]["quarterly"]["peg_ratio"]
        peg_avg = sum(peg)/len(peg)
        current_peg = peg[-1]
        peg.sort()
        peg_low = peg[0]
        if visual == True:
            print("")
            print("price to earnings growth lowest: " + str(peg_low))
            print("price to earnings growth average: " + str(peg_avg))
            print("price to earnings growth current: " + str(current_peg))
        return {"peg_low":peg_low, "peg_avg":peg_avg, "peg":current_peg}
    except:
        print("...somehting went wrong with price to book valuation...")
        return "NA"


def price_to_earnings(data, visual=True):
    """
    Returns an overview of the historic p/e ratio for the company.
    Arguments:
        data: json file containing all the data for the given company
        visual: if true will print out to the terminal
    Returns:
        Returns the current, lowest and average p/e ratio.
    """
    try:
        pe = data["financials"]["quarterly"]["price_to_earnings"]
        pe_avg = sum(pe)/len(pe)
        current_pe = pe[-1]
        pe.sort()
        pe_low = pe[0]
        if visual == True:
            print("")
            print("price to earnings lowest: " + str(pe_low))
            print("price to earnings average: " + str(pe_avg))
            print("price to earnings current: " + str(current_pe))
        return {"pe_low":pe_low, "pe_avg":pe_avg, "pe":current_pe}
    except:
        print("...somehting went wrong with price to eanrings valuation...")
        return "NA"

def price_to_book(data, visual=True):
    """
    Returns an overview of the historic p/b ratio for the company.
    Arguments:
        data: json file containing all the data for the given company
        visual: if true will print out to the terminal
    Returns:
        Returns the current, lowest and average p/b ratio.
    """
    try:
        pb = data["financials"]["quarterly"]["price_to_book"]
        pb_avg = sum(pb)/len(pb)
        current_pb = pb[-1]
        pb.sort()
        pb_low = pb[0]
        if visual == True:
            print("")
            print("price to book lowest: " + str(pb_low))
            print("price to book average: " + str(pb_avg))
            print("price to book current: " + str(current_pb))
        return {"pb_low":pb_low, "pb_avg":pb_avg, "pb":current_pb}
    except:
        print("...somehting went wrong with price to book valuation...")
        return "NA"

def grahams_valuation(data, visual=True):
    """
    Function computes intrinsic value of the stock based on graham formula.
    Arguments:
        data: json file containing all the data for the given company
        visual: if true will print out to the terminal
    Returns:
        Returns the intrinsic value per share of the company.
    """
    try:
        current_bond = 4.1

        #calculate growth rate
        rev_growth = data["financials"]["annual"]["revenue_growth"]
        rev_growth.sort()
        high_rev_growth = rev_growth[-5:]
        rev_growth = rev_growth[:5]
        grow_rate = sum(rev_growth)/len(rev_growth)

        #get the eps for the company
        eps = data["financials"]["quarterly"]["eps_basic"]
        eps = sum(eps[-4:])

        price = (eps*(8.5+(2*grow_rate))*4.4)/current_bond
        if visual == True:
            print("grahams price valuation is: $" + str(round(price,2)))
        return price

    except:
        print("...something went wrong with grahams valuation...")
        return "NA"

def auto_dcf_formula(data, visual=True):
    """
    Function performs a fcf projection and then discounts back to present day to find intrinsic value.
    Arguments:
        data: json file containing all the data for the given company
        visual: if true will print out to the terminal
    Returns:
        Returns a low, fair, and high price to pay per share for the company.
    """
    try:
        if data["financials"]["annual"]["revenue"][-1] > 0:
            timeline = 4
            required_return = 0.15
            perpetual_rate = 0.025

            #calculate free cash flow
            cash_flow = data["financials"]["annual"]["cf_cfo"]
            capital = data["financials"]["annual"]["capex"]
            free_cash = []
            for i in range(len(cash_flow)):
                free_cash.append(cash_flow[i] + capital[i])

            #calculate free cash flow to income
            net_income = data["financials"]["annual"]["cfo_net_income"]
            fcf_to_income = []
            for i in range(len(net_income)):
                fcf_to_income.append(free_cash[i] / net_income[i])
            avg_fcf_to_income = sum(fcf_to_income)/len(fcf_to_income)

            #calculate growth rate
            rev_growth = data["financials"]["annual"]["revenue_growth"]
            rev_growth.sort()
            high_rev_growth = rev_growth[-5:]
            rev_growth = rev_growth[:5]
            grow_rate = sum(rev_growth)/len(rev_growth)
            try:
                high_grow_rate = get_current_estimate(data["metadata"]["symbol"])
            except: 
                high_grow_rate = -0.111111
            low_grow_rate = rev_growth[0]

            #calculate net income margins
            revenue = data["financials"]["annual"]["revenue"]
            rev_to_income = []
            for i in range(len(net_income)):
                rev_to_income.append(net_income[i] / revenue[i])
            avg_income_margin = sum(rev_to_income)/len(rev_to_income)

            #projected revenue and income
            projected_rev = []
            projected_rev.append((revenue[-1])*(1+grow_rate))
            for i in range(timeline-1):
                projected_rev.append(projected_rev[-1]*(1+grow_rate))
            projected_income = []
            for i in range(len(projected_rev)):
                projected_income.append(projected_rev[i]*avg_income_margin)

            #projected  low revenue and income
            low_projected_rev = []
            low_projected_rev.append((revenue[-1])*(1+low_grow_rate))
            for i in range(timeline-1):
                low_projected_rev.append(low_projected_rev[-1]*(1+low_grow_rate))
            low_projected_income = []
            for i in range(len(low_projected_rev)):
                low_projected_income.append(low_projected_rev[i]*avg_income_margin)

            #projected  high revenue and income
            high_projected_rev = []
            high_projected_rev.append((revenue[-1])*(1+high_grow_rate))
            for i in range(timeline-1):
                high_projected_rev.append(high_projected_rev[-1]*(1+high_grow_rate))
            high_projected_income = []
            for i in range(len(high_projected_rev)):
                high_projected_income.append(high_projected_rev[i]*avg_income_margin)

            #calculate projected cash flow
            projected_cash_flow = []
            for i in range(len(projected_rev)):
                projected_cash_flow.append(projected_income[i]*(1+avg_fcf_to_income))

            #calculate projected low cash flow
            low_projected_cash_flow = []
            for i in range(len(projected_rev)):
                low_projected_cash_flow.append(low_projected_income[i]*(1+avg_fcf_to_income))

            #calculate projected high cash flow
            high_projected_cash_flow = []
            for i in range(len(projected_rev)):
                high_projected_cash_flow.append(high_projected_income[i]*(1+avg_fcf_to_income))

            #getting shares outstanding
            shares = data["financials"]["annual"]["shares_diluted"]
            shares = shares[-1]

            #calculate terminal value
            terminal = (projected_cash_flow[-1]*(1+perpetual_rate))/(required_return - perpetual_rate)
            projected_cash_flow.append(terminal)

            #calculate low terminal value
            terminal = (low_projected_cash_flow[-1]*(1+perpetual_rate))/(required_return - perpetual_rate)
            low_projected_cash_flow.append(terminal)

            #calculate high terminal value
            terminal = (high_projected_cash_flow[-1]*(1+perpetual_rate))/(required_return - perpetual_rate)
            high_projected_cash_flow.append(terminal)

            #calcualate present value of cash flows
            present_cash_value = []
            for i in range(len(projected_cash_flow)):
                if i == (timeline - 1):
                    present_cash_value.append(projected_cash_flow[i] / ((1 + required_return)**(i+1)))
                elif i == timeline:
                    present_cash_value.append(projected_cash_flow[i] / ((1 + required_return)**i))

            #calcualate low present value of cash flows
            low_present_cash_value = []
            for i in range(len(low_projected_cash_flow)):
                if i == (timeline - 1):
                    low_present_cash_value.append(low_projected_cash_flow[i] / ((1 + required_return)**(i+1)))
                elif i == timeline:
                    low_present_cash_value.append(low_projected_cash_flow[i] / ((1 + required_return)**i))

            #calcualate high present value of cash flows
            high_present_cash_value = []
            for i in range(len(high_projected_cash_flow)):
                if i == (timeline - 1):
                    high_present_cash_value.append(high_projected_cash_flow[i] / ((1 + required_return)**(i+1)))
                elif i == timeline:
                    high_present_cash_value.append(high_projected_cash_flow[i] / ((1 + required_return)**i))

            #calculate todays value
            today_value = sum(present_cash_value)
            low_today_value = sum(low_present_cash_value)
            high_today_value = sum(high_present_cash_value)


            #calculate price to pay
            price = today_value/shares
            low_price = low_today_value/shares
            high_price = high_today_value/shares
            current_price = get_current_price(data["metadata"]["symbol"])

            if visual == True:
                print("low price estimate is: $" + str(round(low_price,2)), "Growth rate used:", str(round(low_grow_rate, 2)))
                print("fair price estimate is: $" + str(round(price, 2)), "Growth rate used:", str(round(grow_rate, 2)))
                print("high price estimate is: $" + str(round(high_price, 2)), "Growth rate used:", str(round(high_grow_rate, 2)))
                if current_price < price:
                    print(data["metadata"]["symbol"], end=" ")
                    print("is currently under valued by", str(round((price/current_price)*100-100,2)) + "%")
                elif current_price > price:
                    print(data["metadata"]["symbol"], end=" ")
                    print("is currently over valued by " + str(round(100-(price/current_price*100),2)) + "%")
                print("the current price is: $" + str(current_price))

            return {"price_low":(low_price, low_grow_rate), "price_med":(price, grow_rate), "price_high":(high_price, high_grow_rate), "price_close":current_price}

        else:
            print("!company has negative revenue in the last year!")
    except:
        print("...dcf not possible...")
        return "NA"


if __name__ == "__main__":

    # read in test data
    with open("output.json") as f:
        data = json.load(f)

        try:
            if data["metadata"]["company_type"] == "normal":
                auto_dcf_formula(data)
                grahams_valuation(data)

            elif data["metadata"]["company_type"] == "bank":
                price_to_book(data)
            else:
                print("dcf not applicable to this stock")

            price_to_earnings_growth(data)
            price_to_earnings(data)

        except:
            print("stock does not have the relevant data")
