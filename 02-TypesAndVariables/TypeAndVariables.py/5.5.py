price = input("Enter price: ")
price = float(price)
discount = input('Enter discount %: ')
discount = float(discount)
discount = (discount/100)
reduction = price*discount
prise_with_discount = price -reduction
print(f'Price with discount: {round(prise_with_discount,2)}')