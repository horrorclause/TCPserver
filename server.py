import socket

#Creating the socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Designating the host & port number
host = socket.gethostname()
port = 444

#Binding to socket
serverSocket.bind(('192.168.1.241', port))

#Starting the TCP listener
serverSocket.listen(3)


while True:
    #Starting connection
    clientSocket, address = serverSocket.accept()

    print("Received connection from %s " % str(address))

    message = 'Thank you for connecting to the server' + '\r\n'
    
    clientSocket.send(message.encode('ascii'))

    clientSocket.close()

    