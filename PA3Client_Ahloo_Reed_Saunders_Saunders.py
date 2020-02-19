#Client.py
#Austin Ah Loo
#Mikie Reed
#Mitchell Saunders
#Nicholas Saunders
import socket
import sys
import threading

port = 12000

client = sys.argv[1]

# Name of client (Alice/Bob)

#method that handles the connection to the socket.
def getConnection(port, ip):
    s = socket.socket()
    while True:
        try:
            s.connect((ip, port))
            break
        except:
            pass
    return s

# method to send message to server
def sendMessages(s):

    global msgsent

    msgsent = "%s: %s"%(client,name)

    s.send(msgsent.encode())

# receive message from server

def receiveMessages(s):

    msg = s.recv(1024).decode()

    print(msgsent)

    print(msg)

def main():
    global name

    ip = '127.0.0.1'
    #takes in input form user for their "name"
    name = raw_input("Enter your name here: ")

    print name
    #gets connection.
    s = getConnection(port,ip)

    s.send(name.encode())

    t = threading.Thread(target=receiveMessages, args=[s])
    #starts a thread of the client.
    t.start()
    #sends messages.
    sendMessages(s)

main()
