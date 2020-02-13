from socket import *
serverName = 'localhost'
serverPort = 12000
#Making a socket to communicate with server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#Sending Client and Name information
#Take in input user name
name = input('Please input your display name:')
clientSocket.send(name.encode())
#Getting response from server about chatting mate
frienden = clientSocket.recv(1024)
friendde = frienden.decode()
print ('You are chatting with: '+ friendde)
print ('Send the first message, then reply one message at a time! (When finished chatting type "exit" to stop)')
while True:
        #Get message to send
        message = input(name+': ')
        clientSocket.send(message.encode())
        #Take care of ending case
        if message == 'exit':
                print ('Chat has ended')
                break
        #Received message from chat buddy
        remen = clientSocket.recv(1024)
        remde = remen.decode()
        if remde == 'exit':
                print ('The other user has ended the chat')
                break
        print (friendde+": "+remde)
endingen = clientSocket.recv(1024)
endingde = endingen.decode()
print (endingde)
#Closing Socket
clientSocket.close()
