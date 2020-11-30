def products(sales_tax = 0.088):
    product = input("Enter product name:\t")
    price = float(input("Enter price of " + product + " "))

    total_price = price + (price * sales_tax)
    print(product + " costs a total of " + str(total_price))    

products()

