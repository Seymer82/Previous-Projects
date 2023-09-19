loveley_loveseat_description = "Loveley Loveseat. Tufted polyester blendn on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#price of loveseat
loveley_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
#price for stylish settee
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade"
# Price for luxurious lamp
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_total += 254.00
customer_one_total += 52.15

customer_one_itemization = "Loveley Loveseat. Tufted polyester blendn on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
customer_one_itemization2 = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade"

customer_one_tax = customer_one_total * sales_tax

total = customer_one_total + customer_one_tax

print ("Customer One Items:", end= " ")
print (customer_one_itemization + " " + customer_one_itemization2)
print ( "Customer One Total:", end= " ")
print ("{:.2f}".format(total))
