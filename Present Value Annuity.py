# Prompt the user for input values
pmt = float(input("Enter the payment amount: "))
r = float(input("Enter the discount rate as a decimal: "))
n = int(input("Enter the number of payments: "))

# Calculate the present value of the annuity
pv = pmt * ((1 - (1 + r)**(-n)) / r)

# Display the result
print("The present value of the annuity is: ${:.2f}".format(pv))