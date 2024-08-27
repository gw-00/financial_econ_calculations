import yfinance as yf

# Prompt user to enter the ticker symbol of a publicly traded company
ticker_symbol = input(str(("Enter the ticker symbol of a publicly traded company: ")))

# Use yfinance to get financial data for the company
company_data = yf.Ticker(ticker_symbol)

# Get the company name
company_name = company_data.info['longName']
print(f"\nFinancial data for {company_name} ({ticker_symbol}):\n")

# Get the company's balance sheet, income statement, and cash flow statement
balance_sheet = company_data.balance_sheet
income_statement = company_data.financials
cash_flow_statement = company_data.cashflow

# Print the financial data for the company
print(f"Balance Sheet:\n{balance_sheet}")
print(f"\nIncome Statement:\n{income_statement}")
print(f"\nCash Flow Statement:\n{cash_flow_statement}")
