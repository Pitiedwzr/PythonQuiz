import time
import random
import json

# Output rules
print("Welcome to a quiz of Arcaea! Arcaea is a rhythm game, In this quiz you need to answer a few questions to get score, Let me show you the rules:")
time_wait = 0 # Set delay time to 0 to easy debug
#time_wait = 1
time.sleep(time_wait)
print("1.Each question will have a time limit for answering, if you fail to answer or answer an incorrect answer, you won't receive scores.")
time.sleep(time_wait)
print("2.There are some bonus questions, the score of bonus questions depends on the time you use, so you'd answer bonus questions as fast as possible and correctly.")
time.sleep(time_wait)
print("3.You can choose the difficulty level that is suitable for you, different level have their own ranking board.")
#time_wait = 2
time.sleep(time_wait)

# Questions
pst_ques = [
    {
        "question": "Which partner has a skill? ",
        "choices": ["Hikari", "Tairitsu"],
        "answer": "Hikari",
        "bonus": False,
        "time": 20,
        "hint": ""
    },
    {
        "question": 'Which word common means "Perfect"? ',
        "choices": ["PURE", "FAR", "LOST"],
        "answer": "PURE",
        "bonus": True,
        "time": 20,
        "hint": ""
    }
]
pre_ques = [
    {
        "question": "Which song has the same artist with Tempestissimo? ",
        "choices": ["OMAKENO Stroke", "BLRINK", "World Ender", "Silent Rush"],
        "answer": "OMAKENO Stroke",
        "bonus": False,
        "time": 20,
        "hint": ""
    },
    {
        "question": "Which artist finish the song Axium Crisis? ",
        "choices": ["ak+q", "Aoi", "ARForest", "chitose"],
        "answer": "ak+q",
        "bonus": True,
        "time": 20,
        "hint": ""
    }
]
ftr_ques = [
    {
        "question": "Which song have the highest chart constant? ",
        "choices": ["Testify", "Tempestissimo", "Arcana Eden", "PRAGMATISM -RESURRECTION-"],
        "answer": "Testify",
        "bonus": False,
        "time": 20,
        "hint": ""
    },
    {
        "question": "What PTT you need to unlock the Beyond level in game? ",
        "choices": ["9", "10", "12.5"],
        "answer": "9.0",
        "bonus": True,
        "time": 20,
        "hint": ""
    }
]

# Save score as 0
score = 0

# Ask for nickname
nickname = input("Please press your nickname so we can save your score ranking!")

# Check User is ready or not
ready = input('When you are ready, press "start" to start the quiz!')
while not ready.lower() == "start":
    ready = input('''Still not ready? That's ok, when you ready just type "start":''')

# Difficult choose
print("Past (Easy):")
print("Designed for beginners or those who want to start with an easier challenge.")
print("Present (Normal):")
print("Offers a moderate challenge suitable for those with some knowledge of game.")
print("Future (Hard):")
print("For a more advanced and challenging experience.Get ready to expand your thinking.This difficulty requires the participant to be familiar with the skills of the game (involving PTT calculations etc.)")
# Line 77, 78 and 80 is for get a high score at hard level to challenging, but I haven't done the score-save part so it just a placeholder
#print("Beyond (Challenging):")
#print("The ultimate challenge.This level of difficulty requires the participant to know almost everything about the game (which will involve how the game functions at a programmatic level)")
level_chosen = input("Please choose a different level(Pst, Pre, Ftr):").lower()
#level_chosen = input("Please choose a different level(Pst, Pre, Ftr, Byd):").lower()

# Check is level that user chooes vaild
while level_chosen not in ["pst", "pre", "ftr"]:
    level_chosen = input("Invalid level choice. Please choose a valid level (Pst, Pre, Ftr):").lower()

# Set questions to the correct level
if level_chosen == "pst":
    questions = pst_ques
elif level_chosen == "pre":
    questions = pre_ques
elif level_chosen == "ftr":
    questions = ftr_ques
print(f"You choose the {level_chosen} level.")

# Randomize the order of questions
random.shuffle(questions)

for question in questions:
    if question["bonus"]:
        print("Warning: Bonus question!")
        time_limit = question["time"]
        time.sleep(time_wait) # Give time to relize

        # Print the question and start timer
        print(question["question"])
        start_time = time.time()

        # Randomize the order of answer choices
        random.shuffle(question["choices"])
    
        # Print the answer choices
        for number, choice in enumerate(question["choices"]):
            print(f"{number + 1}. {choice}")
    
        # Get user input for the answer and stop the timer
        user_answer = input("Enter your answer (Write the whole answer after the number): ")
        answered_time = time.time()
        time_used = answered_time - start_time

        # Check if the answer is correct
        if user_answer == question["answer"]:
            bonus = round(1 + (1 - time_used / time_limit), 1)
            print(f"Correct! You have get a bonus with {bonus}, and you get {10 * bonus} scores!")
            score += 10 * bonus
        elif time_used > time_limit:
            print("You spend too long time on answer.")
        else:
            print("Incorrect.")
    else:
        time_limit = question["time"]

        # Print the question
        print(question["question"])
        start_time = time.time()

        # Randomize the order of answer choices
        random.shuffle(question["choices"])
        
        # Print the answer choices
        for number, choice in enumerate(question["choices"]):
            print(f"{number + 1}. {choice}")
    
        # Get user input for the answer
        user_answer = input("Enter your answer (Write the whole answer after the number): ")
        answered_time = time.time()
        time_used = answered_time - start_time
        
        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct! You get 10 scores.")
            score += 10
        elif time_used > time_limit:
            print("You spend too long time on answer.")
        else:
            print("Incorrect.")

print(f"You got {score} scores!")