#Request the price of a commodity and the discount percentage.
#Displays the discount amount and the price to pay.


c = float(input('Price: R$ '))
d = float(input('Discount%: '))
discount = c * d / 100
new = c - discount
print(f'Discount: R$ {discount:.2f}')
print(f'Price to pay: R$ {new:.2f}')
