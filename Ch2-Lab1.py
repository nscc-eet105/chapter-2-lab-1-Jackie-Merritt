#Jackie_Merritt/Lab2/6/17/2025

#Input name variables
firstname = input("Please input your first name: ")
lastname = input("Please input your last name: ")
ammount = float(input("Please input marble quantity: "))

#Input math variables
price = 1.20
total = float(ammount * price)

print()

#Print Invoice section
print("Order placed for  " + firstname + " " + lastname)
print()
print(f'{ammount:.0f} marbles ordered at ${price:.2f} per')
print()
print(f'The total cost is ${total:.2f}')
