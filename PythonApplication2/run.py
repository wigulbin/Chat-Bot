from sockets import openSocket, pong, sendMessage
from initialize import joinRoom
from read import getUser, getMessage
import string

#This is called by start and is run in the background on it's own thread
def run():
    s = openSocket()
    joinRoom(s)
    readbuffer = ""

    while True:
        persist = True
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        
        for line in temp:
            #Line holds what was sent to it by the chat
            print(line)

            #Checks for the ping sent by twitch server and calls the pong method
            if "PING" in line:
                pong() 
                sendMessage(s, "test")
            else:
                user = getUser(line)
                message = getMessage(line)
                print user +" typed: " + message

def insertCommand():
    input = raw_input('Enter a new command\n')
    with open('commands.txt', 'a') as file:
        file.write("\n"+input)
           