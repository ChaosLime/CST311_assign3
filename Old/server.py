#TCPserver.py
from socket import *
import time
serverPort = 12000
# Create a TCP socket
serverSocket = socket(AF_INET,SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
#We will use count to differentiate the connections
count = 0
#time will be to see who sent the first message
while count < 3:
        count += 1
        #For the first connection
        if count == 1:
                #From the first we will get the name
                connectionSocket1, addr1 = serverSocket.accept()
                name1 = connectionSocket1.recv(1024).decode()
        #Second Conncetion
        elif count == 2:
                #From the second we will get the name
                connectionSocket2, addr2 = serverSocket.accept()
                name2 = connectionSocket2.recv(1024).decode()
#Exchange names
connectionSocket1.send(name2.encode())
connectionSocket2.send(name1.encode())
#Now that the names have been exchanged we will transfer messages
#Ending connection with them both
count = 0
while True:
        count += 1
        if count%2==1:
                #Get Message from user 1 and send to user 2
                message1 = connectionSocket1.recv(1024).decode()
                print (name1+": "+message1)
                #Ending case, message is exit
                if message1 == 'exit':
                        connectionSocket2.send(message1.encode())
                        break
                connectionSocket2.send(message1.encode())
        else:
                #Get Message from user 2 and send to user 1
                message2 = connectionSocket2.recv(1024).decode()
                #ending case, message is exit
                print (name2+": "+message2)
                if message2 == 'exit':
                        connectionSocket1.send(message2.encode())
                        break
                connectionSocket1.send(message2.encode())
#Making and sending confirmation of the chat ending
time.sleep(1)
endMessage = 'End of chat confirmed, have a good day!'
connectionSocket1.send(endMessage.encode())
connectionSocket2.send(endMessage.encode())
#Closing sockets
connectionSocket1.close()
connectionSocket2.close()
