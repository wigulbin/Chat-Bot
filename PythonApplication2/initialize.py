import string

from sockets import sendMessage

#Joins twitch room and prints the information given to the readbuffer
def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:

        #readbuffer holds the information from the socket passed to it
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Successfully joined chat")
    
#Makes sure that the line has been read completely
def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True