# 1st assignment
# Ask the user for a number
num = float(input("Enter a number: "))

# Check if number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#2nd assignment
# Ask user for password
password = input("Enter your password: ")

# Check if it matches the target password
if password == "secret123.":
    print("Access granted!")
else:
    print("Access denied!")


#3rd assignment
# Ask the user for a number
num = int(input("Enter a number: "))

# Check divisibility by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")


#4th assignment
for num in range(1, 21):
    if num % 2 == 0:
        print(num)


#5th assignment
total = 0
for num in range(1, 11):
    total += num

print("Sum from 1 to 10 is:", total)


#6th assignment
count = 0

while True:
    num = float(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    if num > 0:
        count += 1

print("Count of positive numbers entered:", count)# 1st assignment
# Ask the user for a number
num = float(input("Enter a number: "))

# Check if number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#2nd assignment
# Ask user for password
password = input("Enter your password: ")

# Check if it matches the target password
if password == "secret123.":
    print("Access granted!")
else:
    print("Access denied!")


#3rd assignment
# Ask the user for a number
num = int(input("Enter a number: "))

# Check divisibility by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")


#4th assignment
for num in range(1, 21):
    if num % 2 == 0:
        print(num)


#5th assignment
total = 0
for num in range(1, 11):
    total += num

print("Sum from 1 to 10 is:", total)


#6th assignment
count = 0

while True:
    num = float(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    if num > 0:
        count += 1

print("Count of positive numbers entered:", count)
