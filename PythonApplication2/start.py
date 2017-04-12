import run
import thread
from threading import Thread
import threading
import time

#Lets the run.py file run in the background so commands can still be issued while the bot is running
class backgroundBot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        run.run()

#starts program
def startProgram():

    #infinite loop start
    while True:

        #takes user input as a raw_input, input() would be fine if this was run in python 3
        answer = raw_input('What would you like to do?\n 1. Start Bot\n 2. Add command\n')

        #checks answer for yes or no, tells them if output is incorrect
        if answer == "1":
            background = backgroundBot()
            background.start()
        elif answer == "2":
            run.insertCommand()
        #If answer is invalid it proompts the user to enter again
        else:
            print "Incorrect input, please input Yes or No"
        time.sleep(2)
startProgram()