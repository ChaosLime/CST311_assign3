
import socket

import sys

import threading

##client

#port = int(sys.argv[1])
port = 12000

# Client passed in as commandline argument (X/Y)

#client = int(sys.argv[2])
client = sys.argv[1]

# Name of client (Alice/Bob)

#name = sys.argv[2]

# connect with server at port in commandline argument

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

    s.send(msgsent.encode()) #Python3 (WORKING)
    #s.send(msgsent) # Python2 (WORKING)

# receive message from server

def receiveMessages(s):

    msg = s.recv(1024).decode() # Python3 (WORKING)
    #msg = s.recv(1024)  # Python2 (WORKING)

    print(msgsent)

    print(msg)

def main():
    global name
    
    ip = '127.0.0.1'
    
    name = raw_input("Enter your name here: ")

    print name

    s = getConnection(port,ip)

    s.send(name.encode())

    t = threading.Thread(target=receiveMessages, args=[s])

    t.start()

    sendMessages(s)

main()
