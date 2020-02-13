
import socket

import sys

import threading

global clientName, received

##client

port = int(sys.argv[1])

# Client passed in as commandline argument (X/Y)

client = int(sys.argv[2])

# Name of client (Alice/Bob)

name = sys.argv[3]

# connect with server at port in commandline argument

def getConnection(port, ip):
    s = socket.socket()
    #print("getConnection")
    while True:
        try:
            print("try")
            s.connect((ip, port))
        except:
            print("pass")
            pass
    #s.connect((ip,port))
    #print(s)
    return s

# method to send message to server

def sendMessages(s):

    global msgsent

    msgsent = "%s: %s"%(client,name)
    print(msgsent)
    #type(msgsent)
    s.send(msgsent.encode())

# receive message from server

def receiveMessages(s):

    msg = s.recv(1024)

    print(msgsent)

    print(msg)

def main():

    ip = '127.0.0.1'

    s = getConnection(port,ip)
    #print("before")
    t = threading.Thread(target=receiveMessages, args=[s])
    #print("after")
    t.start()
    #print("after start()")
    sendMessages(s)
    #print("after send")

main()
