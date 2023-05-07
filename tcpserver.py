import socket

serverHost = "127.0.0.1"
serverPort = 80
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen()
print("The server is ready to receive")

while True:
    clientSocket, addr = serverSocket.accept()
    request = clientSocket.recv(1024).decode()
    print("From Client: "+request)

    response = "Oke"
    clientSocket.send(response.encode())
    clientSocket.close()

serverSocket.close()