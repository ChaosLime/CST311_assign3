import socket
import sys
import traceback
from threading import Thread

#client starts with form as follows: for Client X and User Bob
#python client.py X Bob

#These determine the first and secondary inputs when starting the program.
client = str(sys.argv[1])
name = sys.argv[2]

##This client should be able to handle any level of clients, from 1 to 10 theroically
def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12000
    client_name = "Client-%s %s:"%(client,name)
    #prompt at top of the program to let the user know who the client is, and the user
    print(client_name)
    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()


    print("Enter 'quit' to exit")

    message = input(name + " -> ")

    msgsent = messagePrep(client_name,message)
    #this sends the message to the server here, first iteration.
    #send client info here to server?
    soc.sendall(msgsent.encode("utf8"))

    while message != 'quit':
        #I don't know if this is even needed.
        if soc.recv(5120).decode("utf8") == "-":
            pass        # null operation
        try:
            Thread(target=server_input_thread, args=(soc, host, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

        message = input(name + " -> ")
        #second iteration for message to be sent to server.
        #this is due to the fact that when connecting to the server
        #the clients thread has to send a packet to be received
        #by the server.
        msgsent = messagePrep(client_name,message)
        soc.sendall(msgsent.encode("utf8"))

    soc.send(b'--quit--')


def messagePrep(client_name, message):
    msgsent = client_name + " " + message
    return msgsent

def receive_input(connection, max_buffer_size):
    server_response = connection.recv(max_buffer_size)
    server_response_size = sys.getsizeof(server_response)

    if server_response_size > max_buffer_size:
        print("The input size is greater than expected {}".format(server_response_size))

    decoded_input = server_response.decode("utf8").rstrip()  # decode and strip end of line
    result = str(decoded_input)

    return result

## TODO be able to display inputs from other hosts from the server.
def server_input_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True
    server_response = receive_input(connection, max_buffer_size)
    #is buffer empty?
    print("in server thread")

    while is_active:
        print(server_response)
        #does this socket connection share a buffer?
        connection.sendall(server_response.encode("utf8"))

        #connection.close()

main()
