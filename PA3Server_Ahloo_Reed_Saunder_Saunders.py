#Server.py
#Austin Ah Loo
#Mikie Reed
#Mitchell Saunders
#Nicholas Saunders
#Multithreading is needed specifically on the server side because the
#program needs to be able to recieve input from any connection at any
#time. Trying to implement this in a non-multi threaded application
#would result in issues with the timing of both sending and recieving
#messages from the clients.
import socket
import sys
import threading

global clientName, received

def listenToClientMessages(clientsocket,addr):

# read the name from client
    msg = clientsocket.recv(1024).decode('utf-8')
    clname = msg.split(':')[0]
    clientName[clname] = clientsocket

    #check if : is within message to determine if a valid message.
    if ":" not in msg:
        received.append(msg)

    print("Client " + msg)

    #check if both clients have sent messages
    if(len(received) == 2):

        sendToAllClients()

# Send message to all other clients except the sender (not the server)

def sendToAllClients():
    for (name,c) in clientName.items():
        #outputs who recieved before whom
        c.sendall("%s received before %s" % (received[0].encode(), received[1].encode()))
        c.close()

    print("Sent acknowledgment to both X and Y")

def getServerSocket():

    port = 12000
    ip = '127.0.0.1'

    s = socket.socket()
    # SO_REUSEADDR flag tells the kernel to reuse a local socket in
    # TIME_WAIT state, without waiting for its natural timeout to expire
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
