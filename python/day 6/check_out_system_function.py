
VAT_RATE = 0.075 

def add_to_cart():
  
    cart = []
    while True:
        name = input("Enter product name (or 'done' to finish): ")
        if name.lower() == "done":
            break

        try:
            price = float(input(f"Enter price of {name}: "))
            quantity = int(input(f"Enter quantity of {name}: "))
        except ValueError:
            print("Invalid input! Price and quantity must be an integer.")
            continue

        cart.append({"name": name, "price": price, "quantity": quantity})
        print(f"{quantity} x {name} added to cart.\n")

    return cart


def get_totals(cart):
   
    total = sum(item["price"] * item["quantity"] for item in cart)

    if total >= 500000:
        discount_rate = 0.15
    elif total >= 200000:
        discount_rate = 0.10
    elif total >= 100000:
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    discount = total * discount_rate
    vat = (total - discount) * VAT_RATE
    grand_total = (total - discount) + vat

    return total, discount, vat, grand_total


def display_invoice(cart, total, discount, vat, grand_total):
   
    print("\n========== MOSCOW STORE INVOICE ==========")
    print("{:<20} {:>10} {:>10} {:>12}".format("Product", "Price", "Qty", "Subtotal"))
    print("-" * 55)

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        print("{:<20} {:>10.2f} {:>10} {:>12.2f}".format(
            item["name"], item["price"], item["quantity"], subtotal
        ))

    print("-" * 55)
    print(f"{'Total:':<42} N{total:,.2f}")
    print(f"{'Discount:':<42} N{discount:,.2f}")
    print(f"{'VAT (7.5%):':<42} N{vat:,.2f}")
    print(f"{'Grand Total:':<42} N{grand_total:,.2f}")
    print("=============================================")
    print("Thank you for shopping with Moscow Store!")
