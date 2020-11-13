import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

serverSocket.bind((host, port))

serverSocket.listen(3)

#Test connection and present welcome message.
while True:
    clientSocket, address = serverSocket.accept()

    print("Received connection from " % str(address))

    message = 'Thank you for connecting to the server' + '\r\n'

    clientSocket.close()

    