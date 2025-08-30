# # dictionaries


# quiz = {'5 + 5 = ' : '10' , 'What is the capital of france ' : 'Paris' ,}
# score = 0
# for key, value in quiz.items():
#     answer = input(key + '')
#     try:
#         if answer.lower() == value.lower():
#             print("Your answer is correct")
#             score += 5
#         else:
#             print("You got it wrong")
#     except:
#         print('Invalid input')

# print(f"Your score = {score}")



task = []
for i in range(3):
    task.append(input("add task: "))
    with open('task.txt', 'w') as file:
        file.write("\n" .join(task))
        

