#1st assignment
tasks=[]
def show():print("\n".join(f"{i+1}. {t}"for i,t in enumerate(tasks))or"Empty")
def add():tasks.append(input("Task: "))
def rem():show(); 
tasks and(tasks.pop(int(input("Remove #: "))-1) if input else None)

def menu():
  while True:
    c=input("1.Show 2.Add 3.Remove 4.Exit\n:")
    if c=="1":show()
    elif c=="2":add()
    elif c=="3":rem()
    elif c=="4":break

menu()


#2nd assignment
def calculator(a, b):
    print(f"Add: {a+b}")
    print(f"Subtract: {a-b}")
    print(f"Multiply: {a*b}")
    print(f"Divide: {a/b if b!=0 else 'Error (division by zero)'}")

# Practical
calculator(10, 5)


#3rd assignment
# Store 5 numbers in a list
numbers = [10, 20, 30, 40, 50]

# Calculate sum and average
total = sum(numbers)
average = total / len(numbers)

# Print results
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)



#4th assignment
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # only check up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#5th assignment

def find_largest(numbers):
    return max(numbers)

# Example usage
nums = [12, 45, 7, 89, 34]
print("Numbers:", nums)
print("Largest number:", find_largest(nums))
