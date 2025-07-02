import random 
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level):
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return




def check_answer(guessed_number,secret_number,attempts):
    if guessed_number < secret_number:
       print("your guess is too low")
       return attempts -1
    elif guessed_number > secret_number:
        print("your guess is too high")
        return attempts -1
    else:
        print(f"your guess is correct the answer is {secret_number}")




# Randomly generate a number between 1 and 100
print("let me think of a number between 1 and 100.")
secret_number = random.randint(1, 100)
level = ""
while level not in ["easy", "hard"]:
    level = input("choose level of difficulty type 'easy' or 'hard':\n").lower()
    if level not in ["easy","hard"]:
        print("invalid input. choose again")
attempts = set_difficulty(level)




guessed_number = 0
while guessed_number != secret_number:
    print(f"you have {attempts} remaining")
    guessed_number = int(input("guess a number:\n"))
    if guessed_number < 1 or guessed_number > 100:
        print("out of range input")
        continue
    attempts = check_answer(guessed_number,secret_number,attempts)
    if attempts == 0:
        print("you lose")
        break
    elif guessed_number == secret_number:
        break
    