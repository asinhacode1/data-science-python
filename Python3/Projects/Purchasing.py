# creating and operating a list of things and their prices

# prices
price_potato = 1.88
price_milk = 6.15
price_onion = 2.33

# sales tax
sales_tax = 0.088

# quantity
potato = 0
milk = 0
onion = 0


# customer 1
potato = 3
milk = 2
onion = 4

# total customer_1 price to be paid
total_c_1_b4_tax = (potato * price_potato) + (milk * price_milk) + (onion * price_onion)
print("Total c1 b4 tax: " + str(total_c_1_b4_tax))

# after tax
total_c_1_b4_tax += (total_c_1_b4_tax * sales_tax)
print("Total c1 after tax: " + str(total_c_1_b4_tax))
