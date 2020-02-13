#server
from socket import *
import sys
import traceback
from threading import Thread


def main():
    global clientName,received
    clientName = {}
    received = []
# Initialize server socket to listen to connections
    s = getServerSocket()
# start listening to new connections
    listenToNewConnections(s)
    
def getServerSocket():
    port = 12000 
    ip = '127.0.0.1'
    s = socket(AF_INET,SOCK_STREAM)
    s.bind((ip, port))
    s.listen(5)
    return s
        
    
def listenToClientMessages(conn,addr):
# read the name from client
    msg = conn.recv(1024)
    decodedMsg = msg.decode()
    clname = decodedMsg.split(':')[0]
    UserName = decodedMsg.split(': ')[1]
    clientName[clname] = conn
    received.append(decodedMsg)
    print("length: " + str(len(received)))
    print("Decoded Msg: " +decodedMsg)
    print("Client: " + clname)
    print("UserName: " + UserName )

# check if both clients have sent messages
    if(len(received)==2):
        sendToAllClients()
# Send message to all other clients except the sender

def sendToAllClients():
    for (name,c) in clientName.items():
        conn.send("%s received before %s" % (received[0],received[1]))
        conn.close()

print("Sent acknowledgment to both X and Y")



def listenToNewConnections(s):

    print("listening")
    count = 0
    #while count!=2:
        #conn ,addr=s.accept()
    while True:
        connection, address = s.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

# on new connection list to messages from this client on different
# thread so that we don't block other clients from connecting
    t = threading.Thread(target=listenToClientMessages, args=[conn, addr])
# start the thread
    t.start()    
    count+=1



main()
