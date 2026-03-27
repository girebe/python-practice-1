

name = input()


while True:
    if (not name.isalpha()):
        name = input('Enter correct name: ')
    else: break


name.capitalize()
items = 0
subtotal = 0

while True:
    product = input("Enter product name or 'done' to finish: ")
    if (product.lower() != 'done'):
        while True:
            try:
                price = int(input("Enter price: "))
            except ValueError:
                print('Enter a correct price')
            else:
                break
        items += 1
        subtotal += price
    else:break
    
if subtotal < 3000:
    discount = 0
    discount_tier = 'No discount'
    
elif 3000 <= subtotal <7000:
    discount = int(subtotal*0.05)
    subtotal *= int(0.95)
    discount_tier = 5
    
else:
    discount = int(subtotal*0.15)
    subtotal = int(subtotal*0.85)
    discount_tier = 15

print(f'Customer: {name}')
print(f'Items: {items}')
print(f'Subtotal: {subtotal}')
print('-'*20)
print(f'Discount tier: {discount_tier}')
print(f'Discount: {discount} KZT')
print(f'Total: {subtotal}')

print('-'*20)
print(f'Name uppercase: {name.upper()}\nName lowercase: {name.lower()}\nName length: {len(name)}')
if len(name) >5:
    print('long name')
else:
    print('short name')









