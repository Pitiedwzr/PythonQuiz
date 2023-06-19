import time
import json

#Rules
print("Welcome to a quiz of Arcaea! Arcaea is a rhythm game, In this quiz you need to answer a few questions to get score, Let me show you the rules:")
time_wait = 1
time.sleep(time_wait)
print("1.Each question will have a time limit for answering, if you fail to answer or answer an incorrect answer, you won't receive scores.")
time.sleep(time_wait)
print("2.There are some bonus questions, the score of bonus questions depends on the time you use, so you'd answer bonus questions as fast as possible and correctly.")
time.sleep(time_wait)
print("3.You can choose the difficulty level that is suitable for you, different level have their own ranking board.")
time_wait = 2
time.sleep(time_wait)

#Ask for nickname
nickname = input("Please press your nickname so we can save your score ranking!")
ready = input('When you are ready, press "start" to start the quiz!')

#Questions
pst_ques = [
    {
        "question": "Which partner has a skill? ",
        "choices": ["Hikari", "Tairitsu"],
        "answer": "Hikari",
        "hint": "the partner have a EASY skill"
    },
    {
        "question": "",
        "choices": ["", "", "", ""],
        "answer": "",
        "hint": ""
    }
]

#Check User is ready or not
while not ready.lower() == "start":
    ready = input("Still not ready? That's ok, when you ready just type 'start'")

#Difficult choose
print("Past: For people who just played the game.")
print("Present: For people who played a longer time.")
print("Future: For people who played very long time.")
level_choosen = input("Please choose a different level(Pst, Pre, Ftr):").lower()
print(f"You choose the {level_choosen} level.")
