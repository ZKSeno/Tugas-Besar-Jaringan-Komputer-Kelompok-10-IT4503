import socket

serverName = input(str("Alamat IP server: "))
serverPort = int(input(str("Port: ")))

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

request = input(str("Masukkan pesan yang akan dikirim ke server: "))
clientSocket.send(request.encode())

response = clientSocket.recv(1024).decode()
print("From Server: "+response)

clientSocket.close()