# Change here the payment 
print("Welcome to our shop!")


# Item prices

item1 = float(input("Enter the price of 1st item:"))
item2 = float(input("Enter the price of 2nd item:"))
item3 = float(input("Enter the price of 3rd item:"))
final = (item1) + (item2) + (item3)

print(f"Total price: {final:.2f} PHP")

# Check if discount applies
if final > 100:
    print("10% discount (minimum spend of 100 PHP)")
    total = final * 0.90  # Apply 10% discount
    print(f"DISCOUNTED PRICE: {total:.2f} PHP")
else:
    print("(10% discount not applied)")
    total = final  # No discount applied

payment = int(input("Enter your payment here: ")) #INPUT PAYMENT HERE

# Calculate loyalty points

# Check if payment is sufficient
if payment >= total:
    print("---Payment successful---")
    change = payment - total
    print(f"Amount of change: {change:.2f} PHP")
    loyalty_points = total // 10 # loyalty
    print(f"Loyalty points earned: {loyalty_points:.2f} pts")

else:
    print("Invalid payment, please try again!")