import socket

# Seperti kodingan sebelumnya, library socket dipanggil untuk menghubungkan/menjalin koneksi antar client-proxy-server

Proxy = socket.socket()
ProxyName = socket.gethostname()
ClientPort = 8080

# Pada bagian awal, terdapat pembuatan socket atas nama variabel "Proxy".
# Selain itu, terdapat juga pengambilan IP dengan socket.gethostname, dan terjadi pen-declare-an port 8080.
# Port yang digunakan adalah 8080 untuk menghubungkan proxy dengan client terlebih dahulu

Proxy.bind((ProxyName, ClientPort))
Proxy.listen(2)

# Selanjutnya, proxy akan mulai menjalin koneksinya dengan informasi yang sudah didapatkan dari client.

while True:
    print("Waiting for client...")
    client, ClientIP = Proxy.accept()
    print("Connection found from ", ClientIP)
    
    # Selanjutnya, proxy akan mengecek apakah terdapat client yang terhubung. Jika ada, maka akan ditampilkan IPnya.

    ClientName = client.recv(1024).decode()
    ClientAge = client.recv(1024)

    Age = str(ClientAge, 'utf8')
    AgeInt = int(Age)
    MinimumAge = 18

    # Proxy akan kemudian menerima nama dan umur client yang akan digunakan untuk melakukan verifikasi
    # Kemudian, ada juga perubahan type data dari bytes menjadi str kemudian menjadi int untuk melakukan verifikasi.

    if AgeInt >= MinimumAge:
        server = socket.socket()
        server.connect((ProxyName, 8081))
        server.send(ClientName.encode())
        
        # Selanjutnya, akan terjadi pembuatan socket untuk menghubungkan proxy dengan server/host, dimana kemudian proxy
        # akan mengirimkan nama client yang sudah diterima sebelumnya kepada Host/Server untuk diproses

        HostName = server.recv(1024).decode()
        client.send(HostName.encode())

        # Selanjutnya, Host akan memberi usernamenya kembali kepada proxy untuk dioper kepada Client.

        while True:
            Message = server.recv(1024).decode()
            client.send(Message.encode())
            Message2 = client.recv(1024).decode()
            server.send(Message2.encode())

        # Pada bagian akhir, koneksi client-proxy-server sudah terhubung dan chat dapat digunakan secara bergilir

    else:
        client.send("Age Invalid!".encode())

    # Else bagian terakhir digunakan jika client yang ingin connect tidak memenuhi kriteria umurnya.

# Referensi:
# https://stackoverflow.com/questions/33913308/socket-module-how-to-send-integer
# https://realpython.com/convert-python-string-to-int/
# https://stackoverflow.com/questions/402504/how-to-determine-a-python-variables-type
# https://careerkarma.com/blog/python-string-to-int/
# https://www.programcreek.com/python/example/730/socket.recv
# https://www.codegrepper.com/code-examples/python/frameworks/file-path-in-python/how+to+decode+recv+data+in+python
# https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
# https://appdividend.com/2021/04/09/how-to-convert-python-bytes-to-int/
# https://stackoverflow.com/questions/42467634/python3-socket-module-decoding-str
# https://www.w3schools.com/python/python_conditions.asp
# https://www.youtube.com/watch?v=D9UvxHYChD8&list=PLk6vOUIjcauWAzYx5zn5JTnDL9R-Osk_H&index=7




