import time
import random
import json
from colorama import init, Fore, Back, Style

# Initialization colorama
init()

# Output rules
print("Welcome to a quiz of Arcaea! Arcaea is a rhythm game, In this quiz you need to answer a few questions to get score, Let me show you the rules:")
time_wait = 1
time.sleep(time_wait)
print("1.Each question will have a time limit for answering, if you fail to answer or answer an incorrect answer, you won't receive scores.")
time.sleep(time_wait)
print("2.There are some bonus questions, the score of bonus questions depends on the time you use, so you'd answer bonus questions as fast as possible and correctly.")
time.sleep(time_wait)
print("3.You can choose the difficulty level that is suitable for you, different level have their own ranking board.")
#time_wait = 2
time.sleep(time_wait)

# Load questions
with open("questions/pst_question.json", "r") as json_file:
    pst_ques = json.load(json_file)
with open("questions/pre_question.json", "r") as json_file:
    pre_ques = json.load(json_file)
with open("questions/ftr_question.json", "r") as json_file:
    ftr_ques = json.load(json_file)
with open("questions/byd_question.json", "r") as json_file:
    byd_ques = json.load(json_file)

# Save score as 0
score = 0

# Ask for nickname
nickname = input("Please press your nickname so we can save your score ranking!")

# Check User is ready or not
ready = input("When you are ready, press \"start\" to start the quiz!")
while not ready.lower() == "start":
    ready = input("Still not ready? That's ok, when you ready just type \"start\":")

# Check user got a chance to challenging or not
with open("contestants_rank.json", "r") as file:
    contestants_rank = json.load(file)
for contestant in contestants_rank:
    if contestant["nickname"] == nickname and contestant["level_chosen"] == "ftr":
        ftr_score = contestant["score"]
        break
    else:
        ftr_score = 0

# Difficult choose
print("Past (Easy):")
print("Designed for beginners or those who want to start with an easier challenge.")
print("Present (Normal):")
print("Offers a moderate challenge suitable for those with some knowledge of game.")
print("Future (Hard):")
print("For a more advanced and challenging experience.Get ready to expand your thinking.This difficulty requires the participant to be familiar with the skills of the game (involving PTT calculations etc.)")
if ftr_score >= 100:
    print("Beyond (Challenging):")
    print("The ultimate challenge.This level of difficulty requires the participant to know almost everything about the game (which will involve how the game functions at a programmatic level)")
    level_chosen = input("Please choose a different level(Pst, Pre, Ftr, Byd):").lower()
    # Check is level that user chooes vaild
    while level_chosen not in ["pst", "pre", "ftr", "byd"]:
        level_chosen = input("Invalid level choice. Please choose a valid level (pst, pre, ftr, byd):").lower()
else:
    level_chosen = input("Please choose a different level(Pst, Pre, Ftr):").lower()
    # Check is level that user chooes vaild
    while level_chosen not in ["pst", "pre", "ftr"]:
        level_chosen = input("Invalid level choice. Please choose a valid level (pst, pre, ftr):").lower()

# Set questions to the correct level
if level_chosen == "pst":
    questions = pst_ques
elif level_chosen == "pre":
    questions = pre_ques
elif level_chosen == "ftr":
    questions = ftr_ques
elif level_chosen == "byd":
    questions = byd_ques
print(f"You choose the {level_chosen} level.")

# Randomize the order of questions
random.shuffle(questions)

for question in questions:
    if question["bonus"] == "True":
        print(Fore.YELLOW + "Warning: Bonus question!" + Style.RESET_ALL)

        time_limit = question["time"]
        time.sleep(time_wait) # Give time to relize

        # Print the question and start timer
        print(question["question"])
        start_time = time.time()

        # Randomize the order of answer choices
        random.shuffle(question["choices"])
    
        # Print the answer choices
        for number, choice in enumerate(question["choices"]):
            print(Fore.CYAN +  f"{number + 1}. {choice}" + Style.RESET_ALL)
    
        # Get user input for the answer and stop the timer
        user_answer = int(input("Enter your answer (Write the number of answer): "))
        answered_time = time.time()
        time_used = answered_time - start_time

        # Check if the answer is correct
        if time_used > time_limit:
            print("You spend too long time on answer.")
        elif question["choices"][user_answer - 1] == question["answer"]:
            bonus = round(1 + (1 - time_used / time_limit), 1)
            print(Fore.GREEN + f"Correct! You have get a bonus with {bonus}, and you get {10 * bonus} scores!" + Style.RESET_ALL)
            score += 10 * bonus
        else:
            print(Fore.RED + "Incorrect answer. The correct answer is:", question["answer"] + Style.RESET_ALL)
    else:
        time_limit = question["time"]

        # Print the question
        print(question["question"])
        start_time = time.time()

        # Randomize the order of answer choices
        random.shuffle(question["choices"])
        
        # Print the answer choices
        for number, choice in enumerate(question["choices"]):
            print(Fore.CYAN + f"{number + 1}. {choice}" + Style.RESET_ALL)
    
        # Get user input for the answer
        user_answer = int(input("Enter your answer (Write the number of answer): "))
        answered_time = time.time()
        time_used = answered_time - start_time
        
        # Check if the answer is correct
        if time_used > time_limit:
            print("You spend too long time on answer.")
        elif question["choices"][user_answer - 1] == question["answer"]:
            print(Fore.GREEN + "Correct! You get 10 scores." + Style.RESET_ALL)
            score += 10
        else:
            print(Fore.RED + "Incorrect answer. The correct answer is:", question["answer"] + Style.RESET_ALL)

print(Fore.CYAN + f"You got {score} scores in {level_chosen}!" + Style.RESET_ALL)

# Write results
for contestant in contestants_rank:
    if contestant["nickname"] == nickname and contestant["level_chosen"] == level_chosen:
        if contestant["score"] >= score:
            print(f"Your highest score is {contestant['score']} in {contestant['level_chosen']}, the score you got this time is lower than it, so it won't save into your rank.")
            updated = False
            exist = True
            break
        else:
            print(f"Congratulations! The score you got in [level_chosen] is higher than before, it will save into your rank!")
            contestant["score"] = score
            updated = True
            exist = True
            break
    else:
        updated = False
        exist = False

# Write the updated data back to contestants_rank.json
if not updated and not exist:
    results = {
        "nickname": nickname,
        "score": score,
        "level_chosen": level_chosen
    }
    # Add the new result to the loaded data
    contestants_rank.append(results)
    with open("contestants_rank.json", "w") as file:
        json.dump(contestants_rank, file, indent=4)
if updated and exist:
    with open("contestants_rank.json", "w") as file:
        json.dump(contestants_rank, file, indent=4)


if score >= 100 and level_chosen == "ftr":
    print(Fore.MAGENTA + "Because you have got a high score at Future level, you can choose Beyond level next time." + Style.RESET_ALL)
