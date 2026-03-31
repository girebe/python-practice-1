#TaskA1

store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 0000000")

print('=' * 30)
print(f'{store_info[0]}\n{store_info[1]}\n{store_info[2]}')
print('=' * 30)

#TaskA2

names = []
prices = []
while True:
    a = input('Enter product name (or \'done\' to finish): ')
    if a.lower() != 'done':
        names.append(a)
        b = int(input('Enter price: '))
        prices.append(b)
    else: break
    

print('-'* 30)
print(f'Your cart ({len(names)} items): ')
print('-'* 30)
for i in range(len(names)):
    print(f'{names[i]} - {prices[i]} KZT')
print('-'* 30)

#TaskA3

weekly_products = set()
while True:
    a = input('Enter product name (or \'done\' to finish): ')
    if a.lower() != 'done':
        weekly_products.add(a)
    else: break
print(f'Unique products: {len(weekly_products)}\n{weekly_products}')

#TaskA4

name = input('Enter customer name: ')
if sum(prices) < 3000:
    discount = 0
    total = sum(prices)
    discount_type = 'No discount'
elif 3000<=sum(prices) <7000:
    discount = sum(prices) * 0.05
    total = sum(prices) * 0.95
    discount_type = 'Standard discount'
else:
    discount = sum(prices) * 0.15
    total = sum(prices) * 0.85
    discount_type = 'Premium discount'
    
    

receiptry = {'customer': name, 'items' : len(names), 'subtotal': sum(prices), 'discount': discount, 'total': total}


print('='*30)
print(f'Receipt - {store_info[0]}')
print('='*30)
print(f'Customer: {receiptry["customer"]}\nItems: {receiptry["items"]}')
print('-'*30)
for i in range(len(names)):
    print(f'{names[i]} - {prices[i]} KZT')
print('-'*30)
print(f'subtotal: {receiptry["subtotal"]} KZT\nDiscount: {receiptry['discount']} KZT\nTotal: {receiptry["total"]} KZT')

print('='*30)