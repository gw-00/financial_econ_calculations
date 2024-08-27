'''Functions for financial calculations'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm

'''Function for calculating the value of Net Working Capital'''
def net_working_capital(current_assets, current_liabilities):
    net_working_capital = current_assets - current_liabilities
    print("The net working capital is ${}".format(net_working_capital))
    return net_working_capital

''''Function that calculates the current ratio'''
def current_ratio(current_assets, current_liabilities):
    current_ratio = current_assets / current_liabilities
    print("The current ratio is {}".format(current_ratio))
    return current_ratio

''''Function that calculates the quick ratio'''
def quick_ratio(current_assets, current_liabilities, inventory):
    quick_ratio = (current_assets - inventory) / current_liabilities
    print("The quick ratio is {}".format(quick_ratio))
    return quick_ratio

'''Function that calculates the cash ratio'''
def cash_ratio(cash, current_liabilities):
    cash_ratio = cash / current_liabilities
    print("The cash ratio is {}".format(cash_ratio))
    return cash_ratio

'''Function that calculates the NWC to total assets ratio'''
def nwc_to_total_assets(net_working_capital, total_assets):
    nwc_to_total_assets = net_working_capital / total_assets
    print("The net working capital to total assets ratio is {}".format(nwc_to_total_assets))
    return nwc_to_total_assets

'''Function that calculates the interval measure'''
def interval_measure(current_assets, avg_daily_operating_costs):
    interval_measure = current_assets / avg_daily_operating_costs
    print("The interval measure is {}".format(interval_measure))
    return interval_measure

'''Function that calculates the total debt ratio'''
def total_debt_ratio(total_assets, total_equity):
    total_debt_ratio = (total_assets - total_equity) / total_assets
    print("The total debt ratio is {}".format(total_debt_ratio))
    return total_debt_ratio

'''Function that calculates the debt to equity ratio'''
def debt_to_equity(total_debt, total_equity):
    debt_to_equity = total_debt / total_equity
    print("The debt to equity ratio is {}".format(debt_to_equity))
    return debt_to_equity

'''Function that calculates the equity multiplier'''
def equity_multiplier(total_assets, total_equity):
    equity_multiplier = total_assets / total_equity
    print("The equity multiplier is {}".format(equity_multiplier))
    return equity_multiplier

'''Function that calculates the long term debt ratio'''
def long_term_debt_ratio(long_term_debt, total_equity):
    long_term_debt_ratio = long_term_debt / (long_term_debt + total_equity)
    print("The long term debt ratio is {}".format(long_term_debt_ratio))
    return long_term_debt_ratio

'''Function that calculates the times interest earned ratio'''
def times_interest_earned(EBIT, interest):
    times_interest_earned = EBIT / interest
    print("The times interest earned ratio is {}".format(times_interest_earned))
    return times_interest_earned

'''Function that calculates the cash coverage ratio'''
def cash_coverage_ratio(EBIT, depreciation, interest):
    cash_coverage_ratio = (EBIT + depreciation) / interest
    print("The cash coverage ratio is {}".format(cash_coverage_ratio))
    return cash_coverage_ratio

'''Function that calculates Inventory Turnover'''
def inventory_turnover(cost_of_goods_sold, inventory):
    inventory_turnover = cost_of_goods_sold / inventory
    print("The inventory turnover is {}".format(inventory_turnover))
    return inventory_turnover

'''Function that calculates the days sales in inventory'''
def days_sales_in_inventory(inventory_turnover):
    days_sales_in_inventory = 365 / inventory_turnover
    print("The days sales in inventory is {}".format(days_sales_in_inventory))
    return days_sales_in_inventory

'''Function that calculates the receivables turnover'''
def receivables_turnover(sales, accounts_receivable):
    receivables_turnover = sales / accounts_receivable
    print("The receivables turnover is {}".format(receivables_turnover))
    return receivables_turnover

'''Function that calculates the days sales in receivables'''
def days_sales_in_receivables(receivables_turnover):
    days_sales_in_receivables = 365 / receivables_turnover
    print("The days sales in receivables is {}".format(days_sales_in_receivables))
    return days_sales_in_receivables

'''Function that calculates NWC turnover'''
def nwc_turnover(sales, net_working_capital):
    nwc_turnover = sales / net_working_capital
    print("The net working capital turnover is {}".format(nwc_turnover))
    return nwc_turnover

'''Function that calculates the fixed asset turnover'''
def fixed_asset_turnover(sales, net_fixed_assets):
    fixed_asset_turnover = sales / net_fixed_assets
    print("The fixed asset turnover is {}".format(fixed_asset_turnover))
    return fixed_asset_turnover

'''Function that calculates the total asset turnover'''
def total_asset_turnover(sales, total_assets):
    total_asset_turnover = sales / total_assets
    print("The total asset turnover is {}".format(total_asset_turnover))
    return total_asset_turnover

'''Function that calculates the cash conversion cycle'''
def cash_conversion_cycle(days_sales_in_inventory, days_sales_in_receivables, days_payables_outstanding):
    cash_conversion_cycle = days_sales_in_inventory + days_sales_in_receivables - days_payables_outstanding
    print("The cash conversion cycle is {}".format(cash_conversion_cycle))
    return cash_conversion_cycle

'''Function that calculates the profit margin'''
def profit_margin(net_income, sales):
    profit_margin = net_income / sales
    print("The profit margin is {}".format(profit_margin))
    return profit_margin

'''Function that calculates the return on assets'''
def return_on_assets(net_income, total_assets):
    return_on_assets = net_income / total_assets
    print("The return on assets is {}".format(return_on_assets))
    return return_on_assets

'''Function that calculates the return on equity'''
def return_on_equity(net_income, total_equity):
    return_on_equity = net_income / total_equity
    print("The return on equity is {}".format(return_on_equity))
    return return_on_equity

'''Function that calculates the price to earnings ratio'''
def price_to_earnings(price_per_share, earnings_per_share):
    price_to_earnings = price_per_share / earnings_per_share
    print("The price to earnings ratio is {}".format(price_to_earnings))
    return price_to_earnings

'''Function that calculates the price to earnings growth ratio'''
def price_to_earnings_growth(price_to_earnings, growth_rate):
    price_to_earnings_growth = price_to_earnings / growth_rate
    print("The price to earnings growth ratio is {}".format(price_to_earnings_growth))
    return price_to_earnings_growth

'''Function that calculates the price to sales ratio'''
def price_to_sales(price_per_share, sales_per_share):
    price_to_sales = price_per_share / sales_per_share
    print("The price to sales ratio is {}".format(price_to_sales))
    return price_to_sales

'''Function that calculates the market to book ratio'''
def market_to_book(price_per_share, book_value_per_share):
    market_to_book = price_per_share / book_value_per_share
    print("The market to book ratio is {}".format(market_to_book))
    return market_to_book

'''Funtion that calculates the Tobin's Q ratio'''
def tobins_q(total_market_value, replacement_cost_assets):
    tobins_q = total_market_value / replacement_cost_assets
    print("The Tobin's Q ratio is {}".format(tobins_q))
    return tobins_q

'''Function that calculates the enterprise value'''
def enterprise_value(total_market_value_stock, book_value_liabilities, cash):
    enterprise_value = total_market_value_stock + book_value_liabilities - cash
    print("The enterprise value is {}".format(enterprise_value))
    return enterprise_value

'''Function that calculates the enterprise value to EBITDA ratio'''
def enterprise_value_to_ebitda(enterprise_value, EBITDA):
    enterprise_value_to_ebitda = enterprise_value / EBITDA
    print("The enterprise value to EBITDA ratio is {}".format(enterprise_value_to_ebitda))
    return enterprise_value_to_ebitda

'''Function that calculates the future value factor'''
def future_value_factor(interest_rate, periods):
    future_value_factor = round((1 + interest_rate) ** periods, 4)
    print("The future value factor is {}".format(future_value_factor))
    return future_value_factor

'''Function that calculates the present value factor'''
def present_value_factor(interest_rate, periods):
    present_value_factor = round(1 / ((1 + interest_rate) ** periods), 4)
    print("The present value factor is {}".format(present_value_factor))
    return present_value_factor
