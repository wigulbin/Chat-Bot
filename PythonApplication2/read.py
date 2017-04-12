import string

#Reads the input from run.py and gets the user
def getUser(line):
    separate = line.split(":",2)
    user = separate[1].split("!",1)[0] 
    return user

#Same as above except with getting the message
def getMessage(line):
    separate = line.split(":", 2)
    
    message = separate[len(separate)-1]
    return message