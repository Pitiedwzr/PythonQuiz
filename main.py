import time
import random
import json

#Output rules
print("Welcome to a quiz of Arcaea! Arcaea is a rhythm game, In this quiz you need to answer a few questions to get score, Let me show you the rules:")
time_wait = 0
#time_wait = 1
time.sleep(time_wait)
print("1.Each question will have a time limit for answering, if you fail to answer or answer an incorrect answer, you won't receive scores.")
time.sleep(time_wait)
print("2.There are some bonus questions, the score of bonus questions depends on the time you use, so you'd answer bonus questions as fast as possible and correctly.")
time.sleep(time_wait)
print("3.You can choose the difficulty level that is suitable for you, different level have their own ranking board.")
#time_wait = 2
time.sleep(time_wait)

#Questions
pst_ques = [
    {
        "question": "Which partner has a skill? ",
        "choices": ["Hikari", "Tairitsu"],
        "answer": "Hikari",
        "hint": "the partner have a EASY skill"
    },
    {
        "question": 'Which word common means "Perfect"',
        "choices": ["PURE", "FAR", "LOST"],
        "answer": "PURE",
        "hint": ""
    }
]
pre_ques = [
    {
        "question": "",
        "choices": ["", "", "", ""],
        "answer": "",
        "hint": ""
    }
]
ftr_ques = [
    {
        "question": "",
        "choices": ["", "", "", ""],
        "answer": "",
        "hint": ""
    }
]

#Ask for nickname
nickname = input("Please press your nickname so we can save your score ranking!")

#Check User is ready or not
ready = input('When you are ready, press "start" to start the quiz!')
while not ready.lower() == "start":
    ready = input('''Still not ready? That's ok, when you ready just type "start":''')

#Difficult choose
print("Past (Easy):")
print("Designed for beginners or those who want to start with an easier challenge.")
print("Present (Normal):")
print("Offers a moderate challenge suitable for those with some knowledge of game.")
print("Future (Hard):")
print("For a more advanced and challenging experience.Get ready to expand your thinking.This difficulty requires the participant to be familiar with the skills of the game (involving PTT calculations etc.)")
level_chosen = input("Please choose a different level(Pst, Pre, Ftr):").lower()

#Check is level that user chooes vaild
while level_chosen not in ["pst", "pre", "ftr"]:
    level_chosen = input("Invalid level choice. Please choose a valid level (Pst, Pre, Ftr):").lower()

#Set questions to the correct level
if level_chosen == "pst":
    questions = pst_ques
elif level_chosen == "pre":
    questions = pre_ques
elif level_chosen == "ftr":
    questions = ftr_ques
print(f"You choose the {level_chosen} level.")

# Randomize the order of questions
random.shuffle(questions)

# Iterate through the questions
for question in questions:
    # Print the question
    print(question["question"])
    
    # Randomize the order of answer choices
    random.shuffle(question["choices"])
    
    # Print the answer choices
    for number, choice in enumerate(question["choices"]):
        print(f"{number + 1}. {choice}")
    
    # Get user input for the answer
    user_answer = input("Enter your answer (Write the whole answer): ")
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect!")