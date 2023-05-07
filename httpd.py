import socket

def tcpserver():
    serverHost = "127.0.0.1"
    serverPort = 8080
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen()
    print("The server is up and running")

    while True:
        clientSocket, addr = serverSocket.accept()
        response = handle_request()
        clientSocket.send(response.encode())
        clientSocket.close()

    serverSocket.close()

def handle_request():
    content_type = "Content-Type: text/html\r\n\r\n"
    try:
        file = open("index.html", "r")
        message_body = file.read()
        response_line = "HTTP/1.1 200 OK\r\n"
    except:
        file = "File Not Found"
        message_body = file
        response_line = "HTTP/1.1 404 File Not Found\r\n"
    response = response_line+content_type+message_body 
    return response

if __name__ == "__main__":
    tcpserver()