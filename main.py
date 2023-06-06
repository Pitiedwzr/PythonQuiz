import time

#Rules
print("Welcome to a quiz of Arcaea! Arcaea is a rhythm game, In this quiz you need to answer a few questions to get score, Let me show you the rules:")
time_wait = 2
time.sleep(time_wait)
print("1.Each question will have a time limit for answering, if you fail to answer or answer an incorrect answer, you won't receive scores.")
time.sleep(time_wait)
print("2.There are some bonus questions, the score of bonus questions depends on the time you use, so you'd answer bonus questions as fast as possible and correctly.")
time.sleep(time_wait)
print("3.You can choose the difficulty level that is suitable for you, different level have their own ranking board.")

#Ask for nickname
time_wait = 4
time.sleep(time_wait)
nickname = input("Please press your nickname so we can save your score ranking!")
ready = input('When you are ready, press "start" to start the quiz!')

#Difficult choose
if ready.lower() == "start":
    print("Past: For people who just played the game")
    print("Present: For people")
    print("Future:")
    print("Please choose a different level:")

# Set the timer duration in seconds
#timer_duration = 10

# Start the timer
#start_time = time.time()

# Wait for the specified duration
#time.sleep(timer_duration)
