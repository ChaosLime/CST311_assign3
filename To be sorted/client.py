from socket import *
import sys
import threading
global clientName, received
##client

# Client passed in as commandline argument (X/Y)
client = str(sys.argv[1])
# Name of client (Alice/Bob)
name = sys.argv[2]
# connect with server at port in commandline argument

def main():

    ip = '127.0.0.1'
    port = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    print(getConnection(ip,port))
    t = threading.Thread(target=receiveMessages, args=[clientSocket])
    t.start()
    sendMessages(clientSocket)



def getConnection(port, ip):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    while True:
        try:
            clientSocket.connect((ip, port))
        except:
            break
    return clientSocket

# method to send message to server

def sendMessages(clientSocket):

    global msgsent
    
    while True:
        #Get message to send
        message = input(name+': ')
        clientSocket.send(message.encode())
        #Take care of ending case
        if(message == 'exit'):
            print ('Chat has ended')
            break
        remen = clientSocket.recv(1024)
        remde = remen.decode()
        if(message == 'exit'):
            print ('The other user has ended the chat')
            break
        



    
    
    print (endingde)
    msgsent = "%s: %s"%(client,name)
    print("msgsent: " + msgsent)
    #encode message to be sent to server
    clientSocket.send(msgsent.encode())

# receive message from server

def receiveMessages(s):
    print("recieve")

    #dmsg = msg.decode()
    #print("dmsg:" + dmsg)


main()
