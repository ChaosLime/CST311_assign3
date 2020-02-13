import socket
import sys

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
    soc.sendall(msgsent.encode("utf8"))
        
    while message != 'quit':
        if soc.recv(5120).decode("utf8") == "-":
            pass        # null operation

        message = input(name + " -> ")
        msgsent = messagePrep(client_name,message)
        soc.sendall(msgsent.encode("utf8"))
     
    soc.send(b'--quit--')


def messagePrep(client_name, message):
    msgsent = client_name + " " + message
    return msgsent

## TODO be able to display inputs from other hosts from the server.

main()
