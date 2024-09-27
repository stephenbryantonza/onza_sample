print("Welcome to our bank!")
print("We are lending a loan for you!")
print("---- Terms and Conditions ----")
print("> The customer must have a monthly salary greater than or equal to 30,000.00 to be eligible for a loan.")
print("> The requested loan amount must be less than or equal to 10 times the customer's monthly salary.")
print("---- Do you want to loan? ----")

answer = input("Enter your answer (yes or no): ")

if answer == "yes":
    print("You selected yes!")
else:
    print("Thank you for coming!")
    exit()

print("---- Answer the following questions ----")

salary = int(input("How much is your salary: "))

if salary >= 30000:
    print("You are qualified for a loan!")
else:
    print("Sorry, you are not qualified for a loan due to low salary. Thank you and come again!")
    exit()

loan_avail = salary * 10

while True:
    loan = int(input("How much do you wish to loan: "))
    interest = loan * 0.10
    finalpay = loan + interest

    if loan > loan_avail:
        print(f"{loan} can't be processed, too high loan request")
        print("Please enter a valid amount.")
    else:
        print("10% interest being applied...")
        print(f"Amount to pay: {finalpay} pesos")   
        print(f"(increased by: {interest} pesos)")        
        break 

months = int(input("How many months are you willing to pay: "))
monthly = finalpay / months
print("---- Loan accepted! ----")
print(f"You will pay {monthly:.2f} pesos every month!")
print("Thank you for choosing our bank!")
print(f"(you have received {loan} in your wallet)")
