import socket
import sys
import traceback
import time
from threading import Thread


def main():
    host = "127.0.0.1"
    port = 12000

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

    # infinite loop- do not reset for every requests
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

    soc.close()


def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True
    count = 0
    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        server_output = "From Server: " + client_input
        if "quit" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            print(server_output)
            connection.sendall(server_output.encode("utf8"))
            #connection.sendall("-".encode("utf8"))



def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)


    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    result = str(decoded_input)

    return result

## TODO find a way to get inputs from server
## back to all clients short of the one that sent it.

main()
