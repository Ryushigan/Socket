import socket
import sys
import time

# Library "socket" digunakan karena "socket" memiliki fungsi-fungsi yang diperlukan dalam mengimplementasikan socket.
# Library "sys" digunakan untuk menyediakan system module yang berguna dalam menyediakan data yang berhubungan dengan system (directory, functions, methods).
# Library "time" digunakan untuk mengolah unit atau deskripsi waktu yang akan digunakan nantinya.

NewSocket = socket.socket()
HostName = socket.gethostname()
IPAddress = socket.gethostbyname(HostName)

# Pertama-tama, kita dapat mulai membuat socket, hal ini dapat kita lihat pada function "socket.socket()"
# Selain membuat socket, kita juga kemudian dapat menentukan hostname dengan function "socket.gethostname()", yang merupakan bagian dari library socket juga
# Setelah membuat socket dan menentukan hostname, kita kemudian dapat mengambil IP address user lain dan menyimpannya ke dalam "IPAddress"

port = 8081

# Untuk port yang digunakan, port 8081 dipilih dikarenakan kebanyakan mesin/device memiliki port 8081 yang kosong / tidak digunakan. 
# Pada kasus ini, port yang digunakan untuk menghubungkan ke Proxy adalah 8081

NewSocket.bind((HostName, port))

# Kemudian kita dapat menyambungkan port dan host dengan function "bind".

print("Binding complete!")
print("Your current IP: ", IPAddress)

# Kedua command di atas digunakan untuk memastikan bahwa process "Binding" berhasil dan kemudian menunjukkan IP Address dari pengguna tersebut

NewSocket.listen(2)

# Kemudian, "NewSocket.listen(1)" digunakan untuk melakukan proses "listen". Parameter "1" dapat digantikan dengan angka lain (1, 2, 3, ...)

Connect, Add = NewSocket.accept()

# Selanjutnya, jika sebuah user berhasil ter-connect, maka user tersebut akan dimasukkan ke variable "Connect" dan "Add", dimana kemudian akan ada sejenis 
# "list" dari user yang sudah berhasil connect

print("Received connection from ", Add[0])
print("Connection Established. Connected From: ",Add[0])

# Kedua command di atas digunakan untuk menunjukkan apakah koneksi dari user ke-[x] sudah diterima, dan apakah koneksi tersebut sudah berhasil disambungkan.

Client = (Connect.recv(1024)).decode()
print(Client + " has joined the chat.")

# Command diatas digunakan untuk menerima "message" dari Client, dimana pada kali ini adalah nama/username dari client tersebut yang sudah dioper dari client ke proxy

Username = input("Please enter your name: ")
Connect.send(Username.encode())

# Selanjutnya, server/host dapat mengirimkan usernamenya kepada proxy yang kemudian akan dioper ke client

while True:
    message = input("You: ")
    Connect.send(message.encode())
    message = Connect.recv(1024)
    message = message.decode()
    print(Client, ":", message)

# Terakhir, saat pengguna memasukkan/mengirimkan pesannya, pesan tersebut akan diencode dengan menggunakan fucntion "encode()" dan disend menggunakan function "send()".
# Dalam menerima pesan, function yang digunakan adalah "recv()", yang dapat menerima informasi sebesar 1024 bytes, yang kemudian akan di-decode menggunakan function "decode()".

# Referensi:
# https://www.thepythoncode.com/article/make-a-chat-room-application-in-python
# https://www.askpython.com/python/examples/create-chatroom-in-python
# https://pymotw.com/2/socket/tcp.html
# https://www.geeksforgeeks.org/simple-chat-room-using-python/