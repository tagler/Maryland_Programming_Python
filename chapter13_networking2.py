# SERVER

import socket

# server information 
HOST = 'localhost'
PORT = 4444
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server
server.bind((HOST, PORT))
server.listen(10)
connection, address = server.accept()
print(address," has connected!")

while True:
    # recieve/decode data from client
    data_recv = connection.recv(1024) 
    remote_data_string_input = data_recv.decode()

    # data processing 
    value = 0
    for each_letter in remote_data_string_input:
        value += ord(each_letter)
    data_output = (str(value))
    
    # encode/send data to client
    data_output_encoded = data_output.encode()
    connection.send( data_output_encoded )

connection.close()
