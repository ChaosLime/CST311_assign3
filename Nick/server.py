#Multithreading is needed specifically on the server side because the
#program needs to be able to recieve input from any connection at any
#time. Trying to implement this in a non-multi threaded application
#would result in issues with the timing of both sending and recieving
#messages from the clients.

import socket
import sys
import traceback
import time
from threading import Thread

#Global varible clients will hold a complete list of all connected clients.
#This will allow the server to send messages to each connected client.
clients = []
#TODO: Remove clients from list that have elected to leave the chatroom.

#Global variable last_sent_message is here to hold the last message that was sent
#by this server. This prevents duplicate messages from being sent to each client.
last_sent_message = ""

#Global variable necessasary for two things:
#1. Prevent messages to be sent to the server before two connection
#   are successfully made to the server
#2. Allow a the program the ability to count current connections, and thus
#   close the connection when the number of connections go below the minimum.
num_of_active_conn = 0

#Global variable enables main and client_thread to see if the client has made
#a successfull connection to two clients yet. If not, then it will not close
#the connection until this is True. Once the number of active connections
#dips below the minimum and this flag is true, then it will cause the termination
#of this server connection.
conn_succes = False

#TODO: Create a way to close the socket by command, or event. Currently it
#      will run continuosly until it is force closed.

def main():
    host = "127.0.0.1"
    port = 12000
    global clients
    global num_of_active_conn
    
    
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # SO_REUSEADDR flag tells the kernel to reuse a local socket in
    # TIME_WAIT state, without waiting for its natural timeout to expire

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(5)       # queue up to 5 requests
    print("Socket now listening")

    #Create a new thread per client connected. This loop will always be ready
    #to connect to a new client.
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
            #Providing that the thread was successfully created, the connection
            #will be added to the global list of active connections.
            clients.append(connection)
        except:
            print("Thread did not start.")
            traceback.print_exc()

    #Currently, the socket will never be closed as this code is unreachable.
    soc.close()


def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True
    count = 0
    global clients

    client_input = ""
    global last_sent_message
    
    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        if last_sent_message != client_input:
            if "quit" in client_input:
                print("Client is requesting to quit")
                connection.close()
                print("Connection " + ip + ":" + port + " closed")
                is_active = False
            else:
                print(client_input)

                for client in clients:
                    client.sendall(client_input.encode("utf8"))
                
            last_sent_message = client_input


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)


    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    result = str(decoded_input)

    return result

main()
