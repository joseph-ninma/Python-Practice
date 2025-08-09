name = input("What is your name: ")
print(name)
age = input("What is your age: ")
print(name, "you are", age ,"years old")

name = str(input( "what is your name: " ).strip()) 
game = str(input("which game do you like: ").lower()) 
print (f"wow, {name} your favourite game is {}")

no_1 = int(input("please write a number: ")) 

no_2 = int(input("please write a number: "))

sum =  no_1 + no_2
sub = no_1 - no_2
expo = no_1 ** no_2
div = no_1 / no_2
mul = no_1 * no_2

print(sum)
print(sub)
print(expo)
print(div)
print(mul)

name = input("what is your name: ")
print(f"{name} contains {len(name)} characters")

age = int(input("What is your age: "))
year  = 2025
dob = year - age
print(dob)

text = input("Write something about web design: ")
print(text.find("web design"))


text_1 = input("please write a word: ")
text_2 = input("please write a word: ")
text = f"{text_1} {text_2}"
print(text)