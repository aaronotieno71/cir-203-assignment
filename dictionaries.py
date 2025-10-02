
inventory = {
    "Shirt": 25,
    "Jeans": 15,
    "Sneakers": 8,
    "Bags": 12,
    "Jackets": 5
}


inventory["Socks"] = 20
inventory["Shirt"] = 30


def low_stock_products(stock_dict):
    return [item for item, qty in stock_dict.items() if qty < 10]

print("Products with low stock:", low_stock_products(inventory))


del inventory["Jackets"]
print("Updated inventory:", inventory)


for product, qty in inventory.items():
    print(f"Product: {product} — Quantity: {qty}")

