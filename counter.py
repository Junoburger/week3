quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

print("Please enter the number of coins: ")
num_quarters = float(input("# of quarters: "))
num_dimes = float(input("# of dimes: "))
num_nickels = float(input("# of nickels: "))
num_pennies = float(input("# of pennies: "))

total_quarters = num_quarters * quarter
total_dimes = num_dimes * dime
total_nickels = num_nickels * nickel
total_pennies = num_pennies * penny
total = total_quarters + total_dimes + total_nickels + total_pennies


def truncate(n):
    return int(n * 100) / 100


truncatedTotal = truncate(total)

dollars = int(str(truncatedTotal).rsplit('.')[0])
cents = int(str(truncatedTotal).rsplit('.')[1])

print("The total is", dollars,
      "dollars" if dollars > 1 else "dollar",
      "and", cents, "cents" if cents > 1 else "cent")
