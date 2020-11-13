import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

clientSocket.connect((host, port))

message = clientSocket.recv(1024) #The maximum amount of data it will receive


