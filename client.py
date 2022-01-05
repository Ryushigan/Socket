import socket
import sys
import time

# Seperti sebelumnya, ketiga library tersebut diimport terlebih dahulu dikarenakan kodingan ini juga akan memerlukan fungsi-fungsi pada library-library tersebut

Socket = socket.socket()
ServerHost = socket.gethostname()
ClientPort = 8080

# Seperti pada script server, socket akan dibuat terlebih dahulu, yang kemudian akan dimasukkan ke dalam variabel "Socket".
# Kemudian, hostname dari server yang sudah dibuat akan diterima dan disimpan oleh "Client" sebagai variabel "ServerHost"
# Untuk port, yang digunakan adalah port 8080, yang kemudian akan disimpan ke dalam variabel "ClientPort"
# Pada kasus ini, Port yang digunakan adalah 8080, bukan 8081, dikarenakan port 8081 digunakan untuk komunikasi antara server dan proxy, sedangkan
# port 8080 digunakan untuk komunikasi antara client dengan proxy

ClientIP = socket.gethostbyname(ServerHost)
print("This is your IP address: ", ClientIP)

# Kemudian, terdapat proses penyimpanan IP Address ke dalam variabel "IP", yang kemudian akan di-display/tampilkan kembali kepada client.

ServerHost = input("Please enter host's IP address:")
Socket.connect((ServerHost, ClientPort))

ClientName = input("Please enter your name: ")
Socket.send(ClientName.encode())

# Selanjutnya, user diminta untuk memasukkan IP Address dari server host yang akan dijoin, yang kemudian diikuti oleh username Client tersebut.
# Socket pun akan kemudian mencoba meng-connect client kepada IP dari host yang sudah dimasukkan sebelumnya dengan fungsi "connect"

print("Warning! This chat is limited to 18+ years old")

ClientAge = input("How old are you? ")
Socket.send(bytes(str(ClientAge), 'utf8'))

# Selanjutnya, Client akan dimintai umurnya, dikarenakan adanya verifikasi umur untuk mengakses chat ini.
# Command yang digunakan adalah send(bytes(str(ClientAge), 'utf8')) agar proxy dapat menerima inputan dalam bentuk string, yang kemudian akan diubah menjadi integer untuk verifikasi
# pada pihak proxy.

ServerName = Socket.recv(1024)
ServerName = ServerName.decode()

# Selanjutnya, setelah Client berhasil ter-connect pada server, Username Client tersebut akan dikirimkan ke host server tersebut,
# kemudian terdapat proses penerimaan data dengan fungsi "recv()". Selain itu, data yang sudah diterima di-decode dengan fungsi "decode()".


if ServerName == "Age Invalid!":
    print("You are too young to access this chat!")
else:
    print(ServerName,"has joined the chat!")

# Kemudian, jika ternyata umur client tersebut tidak memenuhi kriteria, proxy akan mengirimkan kembali sebuah "kode", yang akan diterima oleh client, dimana akan memberitahu client
# tersebut bahwa umur client tersebut tidak cukup, dan langsung melepas/men-disconnect-kan client dari proxy

# Saat Client sudah berhasil terhubung dengan host server, maka akan muncul pemberitahuan "*User* has joined the chat!"


while True:
    message = (Socket.recv(1024)).decode()
    print(ServerName, ": ", message)
    message = input("You : ")
    Socket.send(message.encode())

# Selama proses penerimaan dan pengiriman message, message tersebut akan di-encode dan decode sebelumnya.

# Referensi:
# https://www.thepythoncode.com/article/make-a-chat-room-application-in-python
# https://www.askpython.com/python/examples/create-chatroom-in-python
# https://pymotw.com/2/socket/tcp.html
# https://www.geeksforgeeks.org/simple-chat-room-using-python/