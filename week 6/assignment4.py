# 1st assignment
import random
import string

# generate one password
def make_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# save multiple passwords into a txt file
password = []
for i in range(5):  # change 5 to how many you want
    with open("passwords.txt", "a") as file:
        file.write(make_password(12) + "\n")  # change 12 to length you want

print("Passwords saved in passwords.txt")

