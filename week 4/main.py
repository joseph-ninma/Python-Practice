# try:
#     items = []
#     for i in range(3):
#         item = input('add item to your inventory: ')
#         items.append(item)
#     print(f"your inventory: {items}")
#     items[0] = 'diamond' + items[0]
#     print(f"Upgraded inventory {items}")
# except Exception as err:
#     print(err)

#slicing and reversing a list

# tools = ['axe', 'shovel', 'hammer','spade', 'sword']
# print(f"First 3 tools {list[0:3]}")
# print(f"Reversed list =  {list [::-1]}")
# print(f"Reversed: {tools.reverse()}")



# games = ['fortnite', 'Beach buggy', 'Minecraft']

# game = str(input("What is your favourite game: ")).strip()

# if game in games:
#     print("your game is part of our list")

# else:
#     print("your game is not found in our list")


# games.sort()
# print(games)


def add(num1, num2):
    return num1 + num2
number =  add(7, 10)
print(number)


def square(num1):
    return num1 * num1
number = square(5)
print(number)


def positive(num):
    try:
        if num > 0:
            print(f"This number {num} is positive")
        elif num == 0:
            print("This number is in between positive and negative")
        else:
            print(f"This number {num} is negative")
    except Exception as err:
        print(err)

number = positive(0)

