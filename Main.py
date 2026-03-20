Name = input("Enter customer name: ")
Product = input("Enter product name: ")
Price = float(input("Enter price per unit (KZT): "))
Amount = int(input("Enter quantity: "))
subtotal = Price*Amount
if subtotal > 5000:
     total=0.90*subtotal
     discount=0.10*subtotal
else:
     total = subtotal
     discount = 0
print('==============================')
print('         SHOP RECEIPT')
print('==============================')
print(f'Customer   : {Name}')
print(f'Product    : {Product}')
print(f'Price      : {Price}')
print(f'Quantity   : {Amount}')
print("------------------------------")
print(f"Subtotal  : {subtotal} (KZT)")
print(f"Discount  : {discount} (KZT)")
print(f"Total     : {total} (KZT)")
print("==============================")
print('Discount applied: ', bool(discount))
print('Paid more than 3000: ', total > 3000)