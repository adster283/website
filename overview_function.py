import json

def overview_financials(data, visual=False):
    """
    Returns a list of summarised financials for the company.
    Arguments:
        data: json file containing all the data for the given company
        visual: if true this will print the summary list to the terminal
    Returns:
        Returns a list containing 8 financial figures summerised.
    """

    try:
        #calculate 5 year pe ratio
        try:
            pe_list = data["financials"]["quarterly"]["price_to_earnings"]
            pe_list = pe_list[-20:]
            pe_5yr = sum(pe_list)/len(pe_list)
        except:
            pe_5yr = "NA"

        #calculate 5 year roic
        try:
            roic_list = data["financials"]["quarterly"]["roic"]
            roic_list = roic_list[-20:]
            roic_5yr = (sum(roic_list)/len(roic_list))*100
        except:
            roic_5yr = "NA"

        #calculate 5 year pfcf
        try:
            pfcf_list = data["financials"]["quarterly"]["price_to_fcf"]
            pfcf_list = pfcf_list[-20:]
            pfcf_5yr = sum(pfcf_list)/len(pfcf_list)
        except:
            pfcf_5yr = "NA"

        #calculate 5 year revenue growth
        try:
            revenue_list = data["financials"]["annual"]["revenue"]
            revenue_list = revenue_list[-5:]
            revenue_growth = []
            for i in range(4):
                revenue_growth.append(revenue_list[i+1]/revenue_list[i]*100-100)
            revenue_5yr = sum(revenue_growth)/len(revenue_growth)
        except:
            revenue_5yr_5yr = "NA"

        #calculate 5 year income
        try:
            income_list = data["financials"]["annual"]["operating_income"]
            income_list = income_list[-5:]
            income_growth = []
            for i in range(4):
                income_growth.append(income_list[i+1]/income_list[i]*100-100)
            income_5yr = sum(income_growth)/len(income_growth)
        except:
            income_5yr = "NA"

        #calculate 5 year shares
        try:
            shares_list = data["financials"]["annual"]["shares_basic"]
            shares_5yr = (shares_list[-1]/shares_list[-5]*100)-100
        except:
            shares_5yr = "NA"

        #calculate 5 year cash flow growth
        try:
            cfo_list = data["financials"]["annual"]["cfo_growth"]
            cfo_list = cfo_list[-20:]
            cfo_5yr = sum(cfo_list)/len(cfo_list)
        except:
            cfo_5yr = "NA"

        #calculate 5 year debt to fcf
        try:
            ltl = data["financials"]["annual"]["lt_debt"][-1]
            fcf = data["financials"]["annual"]["fcf"]
            fcf = fcf[-5:]
            fcf = sum(fcf)/len(fcf)
            ltl_5yr = ltl/fcf
        except:
            ltl_5yr = "NA"

        overview_list = {"pfcf_5yr":pfcf_5yr, "income_5yr":income_5yr, "ltl_5yr":ltl_5yr, "cfo_5yr":cfo_5yr, "shares_5yr":shares_5yr, "revenue_5yr":revenue_5yr, "roic_5yr":roic_5yr, "pe_5yr":pe_5yr}

        #calculate a total value for the overview out of 8
        overview_total = 0
        try:
            if pfcf_5yr < 22: overview_total += 1
            if income_5yr > 0: overview_total += 1
            if cfo_5yr > 0: overview_total += 1
            if shares_5yr < 0: overview_total += 1
            if revenue_5yr > 0: overview_total += 1
            if roic_5yr > 9: overview_total += 1
            if pe_5yr < 22: overview_total += 1
            if ltl_5yr < 5: overview_total += 1
        except:
            pass


        if visual == True:
            print("symbol", data["metadata"]["symbol"])
            print("pfcf", str(round(pfcf_5yr, 2)), end="")
            print("\t"*4, "< 22")
            if isinstance(income_5yr, (int, float, complex)):
                print("income", str(round(income_5yr, 2)) +  "%", end="")
                print("\t"*3, "> 0")
            else:
                print("income", income_5yr +  "%", end="")
                print("\t"*3, "> 0")
            print("ltl", str(round(ltl_5yr, 2)), end="")
            print("\t"*4, "< 5")
            if isinstance(cfo_5yr, (int, float, complex)):
                print("cfo", str(round(cfo_5yr, 2)), end="")
                print("\t"*4, "> 0")
            else:
                print("cfo", cfo_5yr, end="")
                print("\t"*4, "> 0")
            print("shares", str(round(shares_5yr, 2)), "%", end="")
            print("\t"*3, "< 0")
            print("revenue", str(round(revenue_5yr, 2)), "%", end="")
            print("\t"*3, "> 0")
            print("roic", str(round(roic_5yr, 2)), "%", end="")
            print("\t"*3, "> 9")
            print("pe", str(round(pe_5yr, 2)), end="")
            print("\t"*4, "< 22")
            print(f"{overview_total}/8")
        return overview_list
    except:
        print("...unable to overview finacials at this time...")

if __name__ == "__main__":

    # read in test data
    with open("output.json") as f:
        data = json.load(f)

    #review financials
    overview_financials(data, True)


