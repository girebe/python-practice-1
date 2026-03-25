

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

print(f'Customer: {name}')
print(f'Items: {items}')
print(f'Subtotal: {subtotal}')






