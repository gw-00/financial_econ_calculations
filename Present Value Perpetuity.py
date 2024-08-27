# Prompt the user for input values
c = float(input("Enter the constant cash flow: "))
r = float(input("Enter the discount rate as a decimal: "))

# Calculate the present value of the perpetuity
pv = c / r

# Display the result
print("The present value of the perpetuity is: ${:.2f}".format(pv))
