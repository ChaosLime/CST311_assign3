#server
import socket

import sys

import threading

global clientName, received

def listenToClientMessages(clientsocket,addr):

# read the name from client
    #msg = clientsocket.recv(1024) # Python2 (WORKING)
    msg = clientsocket.recv(1024).decode('utf-8') #Python3 (WORKING)

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
        #c.send("%s received before %s" % (received[0],received[1])) # Python2 (WORKING)
        #output = b'received before'
        c.sendall("%s received before %s" % (received[0].encode(), received[1].encode())) # Python3 (NOT WORKING YET)
        c.close()

    print("Sent acknowledgment to both X and Y")

def getServerSocket():

    port = int(sys.argv[1])

    ip = '127.0.0.1'

    s = socket.socket()

    s.bind((ip, port))

    s.listen(5)

    return s

def listenToNewConnections(s):

    count = 0

    while count!=2:

        c,addr = s.accept()

# on new connection list to messages from this client on different

# thread so that we don't block other clients from connecting

        t = threading.Thread(target=listenToClientMessages, args=[c, addr])

# start the thread

        t.start()

        count+=1

def main():

    global clientName,received

    clientName = {}

    received = []

# Initialize server socket to listen to connections

    s = getServerSocket()

    print("waiting for connections from clients...")
# start listening to new connections

    listenToNewConnections(s)

main()
