import matplotlib.pyplot as plt
import numpy as np

#function that calculates the price elasticity of demand by asking user for initial and final prices and initial and final quantities, the function outputs the number to 4 decimals, 
#the function then tells whether it is elastic, inelastic, or unitary elastic, perfectly elastic or perfectly inelastic
#then graphs the demand curve with price on the y axis and quantity on the x axis
def price_elasticity_of_demand():
    initial_price = float(input("Enter the initial price: "))
    final_price = float(input("Enter the final price: "))
    initial_quantity = float(input("Enter the initial quantity: "))
    final_quantity = float(input("Enter the final quantity: "))
    price_elasticity_of_demand = ((initial_quantity - final_quantity) / (initial_quantity * final_quantity)) / ((initial_price - final_price) / (initial_price + final_price))
    print("The price elasticity of demand is:", round(price_elasticity_of_demand, 4))
    if price_elasticity_of_demand > 1:
        print("The demand is elastic.")
    elif price_elasticity_of_demand < 1:
        print("The demand is inelastic.")
    elif price_elasticity_of_demand == 1:
        print("The demand is unitary elastic.")
    elif price_elasticity_of_demand == 0:
        print("The demand is perfectly elastic.")
    elif price_elasticity_of_demand == -1:
        print("The demand is perfectly inelastic.")
    x = np.linspace(0, 100, 1000)
    y = (initial_quantity - final_quantity) / (initial_quantity * final_quantity) * x + (initial_price - final_price) / (initial_price + final_price)
    plt.plot(x, y)
    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.title("Price Elasticity of Demand")
    plt.show()

#calls the function
price_elasticity_of_demand()
