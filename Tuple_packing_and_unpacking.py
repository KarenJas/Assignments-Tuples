#4. Mastering Tuple Packing and Unpacking in Python

def order_details(orders):
    #itterate through order
    for order in orders:
        #Unpack tuple
        customer_name, product, quantity = order
        #print order details
        print(f"Customer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")

#Test
#orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
#]
#order_details(orders)
