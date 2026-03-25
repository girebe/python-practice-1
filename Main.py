Name = input("Enter customer name: ")
Product = input("Enter product name: ")
Price = float(input("Enter price per unit (KZT): "))
Amount = int(input("Enter quantity: "))
subtotal = Price*Amount
discount_tier = ''
if subtotal < 3000:
     discount = 0
     discount_tier = 'No discount'
elif 3000 <= subtotal < 7000:
     total = subtotal*0.95
     discount = subtotal * 0.05
     discount_tier = '5%'
else:
     total = subtotal * 0.85
     discount = subtotal * 0.15
     discount_tier = '15%'
print('==============================')
print('         SHOP RECEIPT')
print('==============================')
print(f'Customer        : {Name}')
print(f'Product         : {Product}')
print(f'Price           : {Price}')
print(f'Quantity        : {Amount}')
print("------------------------------")
print(f"Subtotal        : {subtotal} (KZT)")
print(f'Discount tier   : {discount_tier}')
print(f"Discount        : {discount} (KZT)")
print(f"Total           : {total} (KZT)")
print("==============================")
print('Discount applied: ', bool(discount))
print('Paid more than 3000: ', total > 3000)



print(f'\n\n\n\nName uppercase: {Name.upper()}')
print(f'Name lowercase: {Name.lower()}')
print(f'Name lowercase: {Name.lower()}')
print(f'Name length: {Name.len()}')
if Name.len() > 5:
     print('long name')
else:
     print("short name")


