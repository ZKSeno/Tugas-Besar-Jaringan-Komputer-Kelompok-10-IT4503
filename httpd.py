import socket

#inisialisasi function yang digunakan untuk menjalankan TCP Server
def tcpserver():
    # inisialisasi host dan server yang akan digunakan
    serverHost = "127.0.0.1"
    serverPort = 8080
    # server membuat socket TCP
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # kaitkan host dan server dengan socket TCP
    serverSocket.bind((serverHost, serverPort))
    # server mendengarkan permintaan koneksi TCP dari klien
    serverSocket.listen()
    # print bahwa server sudah dapat digunakan
    print("The server is up and running")

    #looping hingga semua aktivitas klien di server selesai
    while True:
        # buat socket di server untuk menampung klien
        clientSocket, addr = serverSocket.accept()
        # terima request yang akan dikirimkan ke socket klien baru tadi
        response = handle_request()
        # kirim request dan respon html yang diinginkan ke socket
        clientSocket.send(response.encode())
        # tutup socket klien
        clientSocket.close()
    #matikan socket server
    serverSocket.close()

#buat function baru untuk mengelola request (request handling)
def handle_request():
    #tetapkan tipe file yang akan diterima dan ditampilkan oleh server
    content_type = "Content-Type: text/html\r\n\r\n"
    try:
        # buka file HTML yang akan ditampilkan di web server
        file = open("index.html")
        message_body = file.read()
        # deklarasi respons yang akan dikirim ke server apabila sukses terkirim
        response_line = "HTTP/1.1 200 OK\r\n"
    # terapkan error handling untuk mengelola apabila file/path file tidak ditemukan
    except:
        file = "File Not Found"
        message_body = file
        response_line = "HTTP/1.1 404 File Not Found\r\n"
    # rangkai data respons yang akan dikirim ke server
    response = response_line+content_type+message_body 
    return response

#jalankan server
if __name__ == "__main__":
    tcpserver()
