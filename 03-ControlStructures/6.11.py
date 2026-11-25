current_price = float(input("Current product price: "))
previos_price = float(input("Previous prduct price:"))
reduced = (1 - current_price/previos_price) *100
if reduced >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {round(reduced,2)}%")
    