#server
import socket

import sys

import threading


def listenToClientMessages(clientsocket,addr):

# read the name from client

    msg = clientsocket.recv(1024)

    clname = msg.split(':')[0]

    clientName[clname] = clientsocket

    received.append(msg)

    print("Client " + msg)

# check if both clients have sent messages

    if(len(received)==2):

        sendToAllClients()

# Send message to all other clients except the sender

def sendToAllClients():
    for (name,c) in clientName.items():
        c.send("%s received before %s" % (received[0],received[1]))
        c.close()

print("Sent acknowledgment to both X and Y")

def getServerSocket():
    print("getsocket")
    port = int(sys.argv[1])

    ip = '127.0.0.1'

    s = socket.socket()

    s.bind((ip, port))

    s.listen(5)

    return s

def listenToNewConnections(s):
    print("listen to New")
    print(s)
    #count = 0

    #while count!=2:

    c,addr = s.accept()

# on new connection list to messages from this client on different

# thread so that we don't block other clients from connecting

    t = threading.Thread(target=listenToClientMessages, args=[c, addr])

# start the thread

    t.start()
    
    #count+=1

def main():
    print("in main")
    global clientName,received

    clientName = {}

    received = []

# Initialize server socket to listen to connections

    s = getServerSocket()

# start listening to new connections

    listenToNewConnections(s)

main()
