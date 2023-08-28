# add first furniture variable
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. "
# set price for lovely loveseat
lovely_loveseat_price = 254.00

# add second furniture variable
stylish_settee_description = "Stylish Settee. Faux leather on birth. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. "
# set price for stylish settee
stylish_settee_price = 180.50

# add variable for luxurious lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
# set price for luxurious lamp
luxurious_lamp_price = 52.15

# set value for sales tax at 8.8%
sales_tax = .088

# first customer running tally
customer_one_total = 0

# (1) list of the descriptions of things
customer_one_itemization = ""

# (2) add description of lovely loveseat to itemization
customer_one_itemization += lovely_loveseat_description

# (3) add description of luxurious lamp to itemization
customer_one_itemization += luxurious_lamp_description

# add price of item to customer total 
customer_one_total += lovely_loveseat_price

# add price of second item to customer todal
customer_one_total += luxurious_lamp_price

# create customer one tax variable
customer_one_tax = customer_one_total * sales_tax

# add sales tax to customer's total cost
customer_one_tax + customer_one_total

# reciept
# print out heading for itemization
print("Customer One Items")
# print customer's itemization
print(customer_one_itemization)
# add heading for total cost
print("Customer One Total:")
# show sales tax rate
print("Sales tax:", sales_tax)
# print tax paid
print("Taxes Paid:", customer_one_tax)
# print total
print(customer_one_total + customer_one_tax)
