lovely_loveseat_description = """Love Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
print(lovely_loveseat_description.split('.')[0])
#price
lovely_loveseat_price = 254.00
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
#price
stylish_settee_price = 180.50
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
#price

luxurious_lamp_price = 52.15
sales_tax = .088
customer_one_total = 0
reciept={}
reciept[lovely_loveseat_description.split('.')[0]]=lovely_loveseat_price
reciept[luxurious_lamp_description.split('.')[0]]=luxurious_lamp_price

customer_one_total += lovely_loveseat_price
customer_one_total += luxurious_lamp_price
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
print("Customer One Items: " )
print (reciept)
for i in reciept:
    
    print(i, "= Rs.", reciept[i])
print("Customer One Total: Rs. " , (customer_one_total))
