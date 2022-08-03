from fetch_function import *

def get_balance_sheet(data):

    dict = {}
    try:
        dict["dates"] = ("", data["financials"]["annual"]["period_end_date"])
    except:
        pass
    try:
        dict["cash_and_equiv"] = ("Cash and Equivalents", data["financials"]["annual"]["cash_and_equiv"])
    except:
        pass
    try:
        dict["st_investments"] = ("Short-Term Investments", data["financials"]["annual"]["st_investments"])
    except:
        pass
    try:
        dict["receivables"] = ("Accounts Receivable", data["financials"]["annual"]["receivables"])
    except:
        pass
    try:
        dict["inventories"] = ("Inventories", data["financials"]["annual"]["inventories"])
    except:
        pass
    try:
        dict["other_current_assets"] = ("Other Current Assets", data["financials"]["annual"]["other_current_assets"])
    except:
        pass
    try:
        dict["total_current_assets"] = ("Total Current Assets", data["financials"]["annual"]["total_current_assets"])
    except:
        pass
    try:
        dict["equity_and_other_investments"] = ("Equity & Other Investments", data["financials"]["annual"]["equity_and_other_investments"])
    except:
        pass
    try:
        dict["ppe_gross"] = ("Gross PPE", data["financials"]["annual"]["ppe_gross"])
    except:
        pass
    try:
        dict["accumulated_depreciation"] = ("Accumulated Depreciation", data["financials"]["annual"]["accumulated_depreciation"])
    except:
        pass
    try:
        dict["ppe_net"] = ("Net PPE", data["financials"]["annual"]["ppe_net"])
    except:
        pass
    try:
        dict["intangible_assets"] = ("Intangible Assets", data["financials"]["annual"]["intangible_assets"])
    except:
        pass
    try:
        dict["goodwill"] = ("Goodwill", data["financials"]["annual"]["goodwill"])
    except:
        pass
    try:
        dict["other_lt_assets"] = ("Other Long-Term Assets", data["financials"]["annual"]["other_lt_assets"])
    except:
        pass
    try:
        dict["total_assets"] = ("Total Assets", data["financials"]["annual"]["total_assets"])
    except:
        pass
    try:
        dict["accounts_payable"] = ("Accounts Payable", data["financials"]["annual"]["accounts_payable"])
    except:
        pass
    try:
        dict["tax_payable"] = ("Tax Payable", data["financials"]["annual"]["tax_payable"])
    except:
        pass
    try:
        dict["current_accrued_liabilities"] = ("Current Accrued Liabilities", data["financials"]["annual"]["current_accrued_liabilities"])
    except:
        pass
    try:
        dict["st_debt"] = ("Short-term Debt", data["financials"]["annual"]["st_debt"])
    except:
        pass
    try:
        dict["current_deferred_revenue"] = ("Current Deferred Revenue", data["financials"]["annual"]["current_deferred_revenue"])
    except:
        pass
    try:
        dict["current_deferred_tax_liability"] = ("Current Deferred Tax Liability", data["financials"]["annual"]["current_deferred_tax_liability"])
    except:
        pass
    try:
        dict["current_capital_leases"] = ("Current Capital Lease Obligation", data["financials"]["annual"]["current_capital_leases"])
    except:
        pass
    try:
        dict["other_current_liabilities"] = ("Other Current Liabilities", data["financials"]["annual"]["other_current_liabilities"])
    except:
        pass
    try:
        dict["total_current_liabilities"] = ("Total Current Liabilities", data["financials"]["annual"]["total_current_liabilities"])
    except:
        pass
    try:
        dict["lt_debt"] = ("Long-term Debt", data["financials"]["annual"]["lt_debt"])
    except:
        pass
    try:
        dict["noncurrent_capital_leases"] = ("Capital Lease Obligation", data["financials"]["annual"]["noncurrent_capital_leases"])
    except:
        pass
    try:
        dict["pension_liabilities"] = ("Pension Liabilities", data["financials"]["annual"]["pension_liabilities"])
    except:
        pass
    try:
        dict["noncurrent_deferred_revenue"] = ("Noncurrent Deferred Revenue", data["financials"]["annual"]["noncurrent_deferred_revenue"])
    except:
        pass
    try:
        dict["other_lt_liabilities"] = ("Other Long-Term Liabilities", data["financials"]["annual"]["other_lt_liabilities"])
    except:
        pass
    try:
        dict["total_liabilities"] = ("Total Liabilities", data["financials"]["annual"]["total_liabilities"])
    except:
        pass
    try:
        dict["common_stock"] = ("Common Stock", data["financials"]["annual"]["common_stock"])
    except:
        pass
    try:
        dict["preferred_stock"] = ("Preferred Stock", data["financials"]["annual"]["preferred_stock"])
    except:
        pass
    try:
        dict["retained_earnings"] = ("Retained Earnings", data["financials"]["annual"]["retained_earnings"])
    except:
        pass
    try:
        dict["aoci"] = ("Accumulated Other Comprehensive Income", data["financials"]["annual"]["aoci"])
    except:
        pass
    try:
        dict["apic"] = ("Additional Paid-in Capital", data["financials"]["annual"]["apic"])
    except:
        pass
    try:
        dict["treasury_stock"] = ("Treasury Stock", data["financials"]["annual"]["treasury_stock"])
    except:
        pass
    try:
        dict["other_equity"] = ("Other Equity", data["financials"]["annual"]["other_equity"])
    except:
        pass
    try:
        dict["minority_interest_liability"] = ("Minority Interest Liability", data["financials"]["annual"]["minority_interest_liability"])
    except:
        pass
    try:
        dict["total_equity"] = ("Total Equity", data["financials"]["annual"]["total_equity"])
    except:
        pass
    try:
        dict["total_liabilities_and_equity"] = ("Total Liabilities & Equity", data["financials"]["annual"]["total_liabilities_and_equity"])
    except:
        pass
    try:
        dict["total_investments"] = ("Total Investments", data["financials"]["annual"]["total_investments"])
    except:
        pass
    try:
        dict["deferred_policy_acquisition_cost"] = ("Deferred Policy Acquisition Costs", data["financials"]["annual"]["deferred_policy_acquisition_cost"])
    except:
        pass
    try:
        dict["unearned_premiums"] = ("Unearned Premiums", data["financials"]["annual"]["unearned_premiums"])
    except:
        pass
    try:
        dict["future_policy_benefits"] = ("Future Policy Benefits", data["financials"]["annual"]["future_policy_benefits"])
    except:
        pass
    try:
        dict["loans_gross"] = ("Gross Loans", data["financials"]["annual"]["loans_gross"])
    except:
        pass
    try:
        dict["allowance_for_loan_losses"] = ("Allowance for Loan Losses", data["financials"]["annual"]["allowance_for_loan_losses"])
    except:
        pass
    try:
        dict["unearned_income"] = ("Unearned Income", data["financials"]["annual"]["unearned_income"])
    except:
        pass
    try:
        dict["loans_net"] = ("Net Loans", data["financials"]["annual"]["loans_net"])
    except:
        pass
    try:
        dict["deposits_liability"] = ("Total Deposits", data["financials"]["annual"]["deposits_liability"])
    except:
        pass

    return dict

if __name__ == "__main__":
    pass
    #data = get_full_data("intc", False, True)