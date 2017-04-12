import socket, string
from settings import HOST, PORT, PASS, NICK, CHANNEL

#Connects use settings.py information
def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + NICK + "\r\n")
    s.send("JOIN #" + CHANNEL + "\r\n")
    return s


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(messageTemp + "\r\n")
    print("Sent: " + messageTemp)

#When the bot receives a ping this respons with the necessary pong and prints to the console
def pong():
    s=socket.socket()
    s.connect((HOST, PORT))
    s.send("PONG :tmi.twitch.tv\r\n")
    print "PONG sent"
    return
