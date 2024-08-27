# Prompt the user for input values
pv = float(input("Enter the present value of the investment: "))
r = float(input("Enter the interest rate as a decimal: "))
n = int(input("Enter the number of periods: "))

# Calculate the future value of the investment
fv = pv * (1 + r)**n

# Display the result
print("The future value of the investment is: ${:.2f}".format(fv))