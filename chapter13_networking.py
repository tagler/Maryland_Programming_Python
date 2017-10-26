# CLIENT

import socket

# server information 
HOST = 'localhost'
PORT = 4444
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

while True:
    client_input = input('please enter something: ')
    
    # encode and send to server
    encoded_input = client_input.encode()
    server.send( encoded_input )
    
    # recieve from server and decode
    data_rec = server.recv(1024)
    data_decoded = data_rec.decode()

    # data output
    print(data_decoded)
    print( int(data_decoded) % 100 )

server.close()
