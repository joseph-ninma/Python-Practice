
# 1st assignment
# write a text 
text = "hello"
# reversing the text
reversed_text = text[::-1]
# print it out
print(reversed_text)


 #2nd assignment
# Define a string
text = "Python is awesome"
# Define the word to search for
word = "awesome"

# Check if the word exists in the string
if word in text:
    print("Word found!")   # Runs if word is present
else:
    print("Word not found.")   # Runs if word is absent


# 3rd assignment
# Creating an acronym from user input

# Ask user for a phrase
phrase = input("Enter a phrase: ")

# Create acronym by taking first letter of each word
acronym = "".join(word[0].upper() for word in phrase.split())

# Show result
print("Acronym:", acronym)


# 4th assignment
# Ask the user to enter a sentence
text = input("Enter a sentence: ")

# Split into words
words = text.split()

# Count words
word_count = len(words)

print("Number of words:", word_count)


# 5th assignment
text = "python is one of the most famous programming language in the world"
result = text.title()
print(result)  


# 6th assignment
# A list
my_list = [10, 20, 30, 40, 50]

# Get the length of the list
length = len(my_list)

print("Length of the list is:", length)


# 7th assignment
tasks=[]

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTask():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Task:")
        for index, task in enumerate(tasks) :
            print(f"Tasks #{index}. {tasks}")

def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Choose the # of the task you want to delete"))
        if taskToDelete>=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
        print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")



if __name__ == "__main__":
    # Create a loop to run the app
    print("Welcome to the to do list app :)")
    while True:
        print("\n Please select one of the following options")
        print("------------------------------------")
        print("1. Add a new task")
        print("2. Delete a new task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice of task: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            ListTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye!!!")



