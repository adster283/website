from fetch_function import *

def get_cash_flow_statement(data):
    

    dict = {}

    try:
        dict["dates"] = ("", data["financials"]["annual"]["period_end_date"])
    except:
        pass
    try:
        dict["cfo_net_income"] = ("Net Income (Cash Flow Statement)", data["financials"]["annual"]["cfo_net_income"])
    except:
        pass
    try:
        dict["cfo_da"] = ("Depreciation, Depletion, & Amortization", data["financials"]["annual"]["cfo_da"])
    except:
        pass
    try:
        dict["cfo_receivables"] = ("Change in Receivables", data["financials"]["annual"]["cfo_receivables"])
    except:
        pass
    try:
        dict["cfo_inventory"] = ("Change in Inventory", data["financials"]["annual"]["cfo_inventory"])
    except:
        pass
    try:
        dict["cfo_prepaid_expenses"] = ("Change in Prepaid Assets", data["financials"]["annual"]["cfo_prepaid_expenses"])
    except:
        pass
    try:
        dict["cfo_other_working_capital"] = ("Change in Other Working Capital", data["financials"]["annual"]["cfo_other_working_capital"])
    except:
        pass
    try:
        dict["cfo_change_in_working_capital"] = ("Change in Working Capital", data["financials"]["annual"]["cfo_change_in_working_capital"])
    except:
        pass
    try:
        dict["cfo_deferred_tax"] = ("Change in Deferred Tax", data["financials"]["annual"]["cfo_deferred_tax"])
    except:
        pass
    try:
        dict["cfo_stock_comp"] = ("Stock Compensation", data["financials"]["annual"]["cfo_stock_comp"])
    except:
        pass
    try:
        dict["cfo_other_noncash_items"] = ("Other Cash from Operations", data["financials"]["annual"]["cfo_other_noncash_items"])
    except:
        pass
    try:
        dict["cf_cfo"] = ("Cash from Operations", data["financials"]["annual"]["cf_cfo"])
    except:
        pass
    try:
        dict["cfi_ppe_purchases"] = ("Cash from Purchases of PPE", data["financials"]["annual"]["cfi_ppe_purchases"])
    except:
        pass
    try:
        dict["cfi_ppe_sales"] = ("Cash from Sales of PPE", data["financials"]["annual"]["cfi_ppe_sales"])
    except:
        pass
    try:
        dict["cfi_ppe_net"] = ("Net Purchases of PPE", data["financials"]["annual"]["cfi_ppe_net"])
    except:
        pass
    try:
        dict["cfi_acquisitions"] = ("Cash from Acquisitions", data["financials"]["annual"]["cfi_acquisitions"])
    except:
        pass
    try:
        dict["cfi_divestitures"] = ("Cash from Divestitures", data["financials"]["annual"]["cfi_divestitures"])
    except:
        pass
    try:
        dict["cfi_acquisitions_net"] = ("Net Cash From Acquisitions and Divestitures", data["financials"]["annual"]["cfi_acquisitions_net"])
    except:
        pass
    try:
        dict["cfi_investment_purchases"] = ("Cash from Purchases of Investments", data["financials"]["annual"]["cfi_investment_purchases"])
    except:
        pass
    try:
        dict["cfi_investment_sales"] = ("Cash from Sales of Investments", data["financials"]["annual"]["cfi_investment_sales"])
    except:
        pass
    try:
        dict["cfi_investment_net"] = ("Net Purchases of Investments", data["financials"]["annual"]["cfi_investment_net"])
    except:
        pass
    try:
        dict["cfi_intangibles_net"] = ("Net Purchases of Intangible Assets", data["financials"]["annual"]["cfi_intangibles_net"])
    except:
        pass
    try:
        dict["cfi_other"] = ("Other Cash from Investing", data["financials"]["annual"]["cfi_other"])
    except:
        pass
    try:
        dict["cf_cfi"] = ("Cash from Investing", data["financials"]["annual"]["cf_cfi"])
    except:
        pass
    try:
        dict["cff_common_stock_issued"] = ("Common Stock Issued", data["financials"]["annual"]["cff_common_stock_issued"])
    except:
        pass
    try:
        dict["cff_common_stock_repurchased"] = ("Common Stock Repurchased", data["financials"]["annual"]["cff_common_stock_repurchased"])
    except:
        pass
    try:
        dict["cff_common_stock_net"] = ("Net Issuance of Common Stock", data["financials"]["annual"]["cff_common_stock_net"])
    except:
        pass
    try:
        dict["cff_pfd_issued"] = ("Preferred Stock Issued", data["financials"]["annual"]["cff_pfd_issued"])
    except:
        pass
    try:
        dict["cff_pfd_repurchased"] = ("Preferred Stock Repurchased", data["financials"]["annual"]["cff_pfd_repurchased"])
    except:
        pass
    try:
        dict["cff_pfd_net"] = ("Net Issuance of Preferred Stock", data["financials"]["annual"]["cff_pfd_net"])
    except:
        pass
    try:
        dict["cff_debt_issued"] = ("Total Debt Issued", data["financials"]["annual"]["cff_debt_issued"])
    except:
        pass
    try:
        dict["cff_debt_repaid"] = ("Total Debt Repaid", data["financials"]["annual"]["cff_debt_repaid"])
    except:
        pass
    try:
        dict["cff_debt_net"] = ("Net Issuance of Debt", data["financials"]["annual"]["cff_debt_net"])
    except:
        pass
    try:
        dict["cff_dividend_paid"] = ("Cash Paid for Dividends", data["financials"]["annual"]["cff_dividend_paid"])
    except:
        pass
    try:
        dict["cff_other"] = ("Other Cash from Financing", data["financials"]["annual"]["cff_other"])
    except:
        pass
    try:
        dict["cf_cff"] = ("Cash from Financing", data["financials"]["annual"]["cf_cff"])
    except:
        pass
    try:
        dict["cf_forex"] = ("Foreign Exchange Adjustments", data["financials"]["annual"]["cf_forex"])
    except:
        pass
    try:
        dict["cf_net_change_in_cash"] = ("Net Change in Cash", data["financials"]["annual"]["cf_net_change_in_cash"])
    except:
        pass

    return dict

if __name__ == "__main__":
    pass
    #data = get_full_data("cmo:nz", False, True)