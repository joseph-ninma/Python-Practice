print('Welcome to my computer quiz!')

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0  # Initialize score

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does SON stand for? ").lower()
if answer == "standard organisation of nigeria":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does CBN stand for? ").lower()
if answer == "central bank of nigeria":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does NIGCOMSAT stand for? ").lower()
if answer == "nigeria communication satellite":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does NDLEA stand for? ").lower()
if answer == "natinal drug law enforcement agency":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
