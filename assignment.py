#1st assignment
# Ask the user for input
color = input("What is your favorite color: ")
animal = input("What is your favorite animal: ")
food = input("What is your favorite food: ")

#  Create a sentence using the inputs
sentence = f"Imagine a {color} {animal} eating {food} in the zoo"

#  Display the sentence
print(sentence)


#2nd assignment
# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

#  Display the result
print(f"There are {word_count} words in your sentence.")


# 3rd assignment
# Profit and Loss

# Function to calculate Profit.
def Profit(costPrice, sellingPrice) :

    profit = (sellingPrice - costPrice)

    return profit

# Function to calculate Loss.
def Loss(costPrice, sellingPrice) :

    Loss = (costPrice - sellingPrice)

    return Loss

# Driver code
if __name__ == "__main__" :

    costPrice, sellingPrice = 1500, 2000

    if sellingPrice == costPrice :
        print("No profit nor Loss")

    elif sellingPrice > costPrice :
        print(Profit(costPrice, sellingPrice), "Profit")

    else :
        print(Loss(costPrice, sellingPrice), "Loss")