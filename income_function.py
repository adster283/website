from fetch_function import *

def get_income_statement(data):

    dict = {}

    try:
        dict["dates"] = ("", data["financials"]["annual"]["period_end_date"])
    except:
        pass
    try:
        dict["revenue"] = ("Revenue", data["financials"]["annual"]["revenue"])
    except:
        pass
    try:
        dict["cogs"] = ("Cost of Goods Sold", data["financials"]["annual"]["cogs"])
    except:
        pass
    try:
        dict["gross_profit"] = ("Gross Profit", data["financials"]["annual"]["gross_profit"])
    except:
        pass
    try:
        dict["sga"] = ("Sales, General, & Administrative", data["financials"]["annual"]["sga"])
    except:
        pass
    try:
        dict["rnd"] = ("Research & Development", data["financials"]["annual"]["rnd"])
    except:
        pass
    try:
        dict["special_charges"] = ("Special Charges", data["financials"]["annual"]["special_charges"])
    except:
        pass
    try:
        dict["other_opex"] = ("Other Operating Expense", data["financials"]["annual"]["other_opex"])
    except:
        pass
    try:
        dict["total_opex"] = ("Total Operating Expense", data["financials"]["annual"]["total_opex"])
    except:
        pass
    try:
        dict["operating_income"] = ("Operating Profit", data["financials"]["annual"]["operating_income"])
    except:
        pass
    try:
        dict["interest_income"] = ("Interest Income", data["financials"]["annual"]["interest_income"])
    except:
        pass
    try:
        dict["interest_expense"] = ("Interest Expense", data["financials"]["annual"]["interest_expense"])
    except:
        pass
    try:
        dict["net_interest_income_normal"] = ("Net Interest Income (Non-financial)", data["financials"]["annual"]["net_interest_income_normal"])
    except:
        pass
    try:
        dict["other_nonoperating_income"] = ("Other Income (Expense)", data["financials"]["annual"]["other_nonoperating_income"])
    except:
        pass
    try:
        dict["pretax_income"] = ("Pre-Tax Profit", data["financials"]["annual"]["pretax_income"])
    except:
        pass
    try:
        dict["income_tax"] = ("Income Tax", data["financials"]["annual"]["income_tax"])
    except:
        pass
    try:
        dict["net_income_continuing"] = ("Earnings from Continuing Operations", data["financials"]["annual"]["net_income_continuing"])
    except:
        pass
    try:
        dict["net_income_discontinued"] = ("Earnings from Discontinued Operations", data["financials"]["annual"]["net_income_discontinued"])
    except:
        pass
    try:
        dict["income_allocated_to_minority_interest"] = ("Minority Interest Income", data["financials"]["annual"]["income_allocated_to_minority_interest"])
    except:
        pass
    try:
        dict["income_allocated_to_minority_interest"] = ("Other Income Statement Items", data["financials"]["annual"]["income_allocated_to_minority_interest"])
    except:
        pass
    try:
        dict["net_income"] = ("Net Income", data["financials"]["annual"]["net_income"])
    except:
        pass
    try:
        dict["preferred_dividends"] = ("Preferred Dividends", data["financials"]["annual"]["preferred_dividends"])
    except:
        pass
    try:
        dict["net_income_available_to_shareholders"] = ("Net Income Available to Shareholders", data["financials"]["annual"]["net_income_available_to_shareholders"])
    except:
        pass
    try:
        dict["eps_basic"] = ("Basic EPS", data["financials"]["annual"]["eps_basic"])
    except:
        pass
    try:
        dict["eps_diluted"] = ("Diluted EPS", data["financials"]["annual"]["eps_diluted"])
    except:
        pass
    try:
        dict["shares_basic"] = ("Basic Shares Outstanding", data["financials"]["annual"]["shares_basic"])
    except:
        pass
    try:
        dict["shares_diluted"] = ("Diluted Shares Outstanding", data["financials"]["annual"]["shares_diluted"])
    except:
        pass
    try:
        dict["shares_eop"] = ("Shares Outstanding (End of Period)", data["financials"]["annual"]["shares_eop"])
    except:
        pass
    try:
        dict["shares_eop_change"] = ("Shares Outstanding (End of Period) Change", data["financials"]["annual"]["shares_eop_change"])
    except:
        pass
    try:
        dict["premiums_earned"] = ("Total Premiums Earned", data["financials"]["annual"]["premiums_earned"])
    except:
        pass
    try:
        dict["net_investment_income"] = ("Net Investment Income", data["financials"]["annual"]["net_investment_income"])
    except:
        pass
    try:
        dict["fees_and_other_income"] = ("Services, Fees, & Commissions", data["financials"]["annual"]["fees_and_other_income"])
    except:
        pass
    try:
        dict["net_policyholder_claims_expense"] = ("Policy Claims & Benefits", data["financials"]["annual"]["net_policyholder_claims_expense"])
    except:
        pass
    try:
        dict["policy_acquisition_expense"] = ("Policy Acquisition Expense", data["financials"]["annual"]["policy_acquisition_expense"])
    except:
        pass
    try:
        dict["interest_expense_insurance"] = ("Interest Expense (Insurance)", data["financials"]["annual"]["interest_expense_insurance"])
    except:
        pass
    try:
        dict["total_interest_income"] = ("Total Interest Income", data["financials"]["annual"]["total_interest_income"])
    except:
        pass
    try:
        dict["total_interest_expense"] = ("Total Interest Expense", data["financials"]["annual"]["total_interest_expense"])
    except:
        pass
    try:
        dict["net_interest_income"] = ("Net Interest Income", data["financials"]["annual"]["net_interest_income"])
    except:
        pass
    try:
        dict["total_noninterest_revenue"] = ("Total Noninterest Revenue", data["financials"]["annual"]["total_noninterest_revenue"])
    except:
        pass
    try:
        dict["credit_losses_provision"] = ("Credit Losses Provision", data["financials"]["annual"]["credit_losses_provision"])
    except:
        pass
    try:
        dict["net_interest_income_after_credit_losses_provision"] = ("Net Interest Income After Credit Losses Provision", data["financials"]["annual"]["net_interest_income_after_credit_losses_provision"])
    except:
        pass
    try:
        dict["total_noninterest_expense"] = ("Total Noninterest Expense", data["financials"]["annual"]["total_noninterest_expense"])
    except:
        pass
    try:
        dict["da_income_statement_supplemental"] = ("Depreciation & Amortization (Supplemental Income Statement Item)", data["financials"]["annual"]["da_income_statement_supplemental"])
    except:
        pass

    return dict

if __name__ == "__main__":
    pass
    #data = get_full_data("intc", False, True)
