import socket
import os
import re
# "re" dalam kasus ini digunakan untuk proses peng-ekstraksian string pada tahap-tahap akhir codingan ini

# Pertama-tama, kita men-declare host yang ingin kita "listen"
hostIP = "127.0.0.1"

# Hanya untuk melakukan pengecekan:
# print(hostIP)

# Setelah itu, kita dapat mulai membuat socket untuk mencari koneksi, dan melakukan binding dengan public interface
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

# Pengkondisian IF di atas digunakan untuk mengecek OS yang akan melakukan/menjalankan sniffing. Dalam kasus ini, 
# device saya akan mengikuti statement If yang pertama dikarenakan saya menggunakan OS Windows, 
# maka dari itu, dapat dilakukan proses sniff untuk semua packet dimana Linux hanya memperbolehkan sniffing ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind ((hostIP,8080))

# Pada kasus ini, socket yang digunakan oleh sniffer memiliki sebuah parameter tambahan, "socket_protocol", 
# yang digunakan untuk memilih protokol yang akan kita gunakan, yang sudah kita declare pada bagian awal koding
# Selanjutnya, untuk proses bind, kita tidak akan memilih port yang spesifik (0) dikarenakan kita sebagai 
# sniffer dianggap tidak mengetahui dimana terjadinya koneksi tersebut


# Kemudian, kita dapat meng-include IP Header dalam proses capturenya
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
# Selanjutnya, kita melakukan pengecekan lagi, jika device yang melakukan sniffing menggunakan OS Windows (nt), 
# maka akan dilakukan tahap pengiriman IOCTL kepada network card driver
# untuk meng-enable promiscuous mode (sebuah mode operasi yang dapat meng-intercept 
# dan membaca keseluruhan packet yang hadir pada networknya)

# Untuk membaca chattingan yang disniff:

while True:
    # print (sniffer.recvfrom(65565))
    
    # Sebelumnya sudah terjadi pencobaan hanya dengan "print (sniffer.recvfrom(65565))", tetapi hasil yang diterima terlalu panjang.
    # Contoh hasil output:
        # (b'E\x00\x005Q\x12@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\x1f\x91\xf5\x80\xdf\xb5\xc1{\x15\xed\xcc\x07P\x18\xff\x9a>H\x00\x00MulaiDariSini', ('192.168.204.1', 0)) (Terdapat 32 "/" dan 29 "x sebelum isi text)
        # (b"E\x00\x005Q\x14@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\x1f\x90\xf5'9\x1b:\x1c\xf7y\xfc\xb8P\x18\xff\x98Z`\x00\x00MulaiDariSini", ('192.168.204.1', 0)) (Terdapat 29 "/" dan 29 "x" sebelum isi text)

        # (b"E\x00\x000Q\x16@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\xf5'\x1f\x90\xf7y\xfc\xb89\x1b:)P\x18\xff\x99\xbf[\x00\x00Start123", ('192.168.204.1', 0)) (Terdapat 29 "/" dan 29 "x" sebelum isi text)
        # (b'E\x00\x000Q\x18@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\xf5\x80\x1f\x91\x15\xed\xcc\x07\xdf\xb5\xc1\x88P\x18\xff\x99\xa3E\x00\x00Start123', ('192.168.204.1', 0)) (Terdapat 34 "/" dan 34 "x" sebelum isi text)

        # (b'E\x00\x003Q\x1a@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\x1f\x91\xf5\x80\xdf\xb5\xc1\x88\x15\xed\xcc\x0fP\x18\xff\x92@\xbf\x00\x00CobaLagi123', ('192.168.204.1', 0)) (Terdapat 34 "/" dan 34 "x" sebelum isi text)
        # (b"E\x00\x003Q\x1c@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\x1f\x90\xf5'9\x1b:)\xf7y\xfc\xc0P\x18\xff\x90\\\xd7\x00\x00CobaLagi123", ('192.168.204.1', 0)) (Terdapat 31 "/" dan 29 "x" sebelum isi text)

        # (b"E\x00\x00/Q(@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\xf5'\x1f\x90\xf7y\xfc\xc09\x1b:4P\x18\xff\x8e\x95{\x00\x00aaaaaaa", ('192.168.204.1', 0)) (Terdapat 28 "/" dan 28 "x" sebelum isi text)
        # (b'E\x00\x00/Q*@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\xf5\x80\x1f\x91\x15\xed\xcc\x0f\xdf\xb5\xc1\x93P\x18\xff\x8eye\x00\x00aaaaaaa', ('192.168.204.1', 0)) (Terdapat 32 "/" dan 32 "x" sebelum isi text)

        # (b'E\x00\x001Q,@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\x1f\x91\xf5\x80\xdf\xb5\xc1\x93\x15\xed\xcc\x16P\x18\xff\x8b\x12\xfa\x00\x00bbbbbbbbb', ('192.168.204.1', 0)) (Terdapat 34 "/" dan 34 "x" sebelum isi text)
        # (b"E\x00\x001Q.@\x00\x80\x06\x00\x00\xc0\xa8\xcc\x01\xc0\xa8\xcc\x01\x1f\x90\xf5'9\x1b:4\xf7y\xfc\xc7P\x18\xff\x89/\x12\x00\x00bbbbbbbbb", ('192.168.204.1', 0)) (Terdapat 28 "/" dan 28 "x" sebelum isi text)

    # Setelah saya baca lebih lanjut, ternyata dapat kita lihat bahwa message sebenarnya terdapat di bagian akhir string ("\x00MulaiDariSini").
    # Dari ke5 contoh yang saya coba, dapat dilihat bahwa ada pola yang dapat dikatakan cukup sama, dimana inout yang diterima setidaknya memiliki 28 "/" dan 28 character "x" (bisa jadi lebih dari 28)

    # Pertama-tama, saya akan mendeclarekan keseluruhan message yang diterima ke dalam variabel "nonDecodedString"
    preDecodedString = sniffer.recvfrom(65565)
    
    # Setelah ditelusuri lebih lanjut, ternyata tuples yang diterima memiliki 2 index, maka dari itu, 
    # saya hanya akan meng-convert index ke-0 menjadi bytes terlebih dahulu
    convertedNonDecodedString = bytes(preDecodedString[0])

    if convertedNonDecodedString[40:] != b'':
        # print("============================")
        # print(convertedNonDecodedString)
        # print(type(convertedNonDecodedString))
        # print("============================\n")

        print("Full String:")
        print(convertedNonDecodedString)
        # Kedua baris di atas dapat di-command jika merasa terlalu ter-spam

        # Setelah ditelusuri lebih lanjut (menggunakan bruteforce mengganti angka pada 
        # convertedNonDecodedString[40:]" dari 1 hingga 40),
        # ternyata isi dari chat yang dikirim oleh server dan client berada pada bytes ke-40, maka dari itu:
        print("Isi Chat:")
        print(convertedNonDecodedString[40:])
        # Command ini digunakan untuk membaca bytes yang diterima hanya dari bytes 40 ke atas.

        print("==========================")
    else:
        continue

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)



# Referensi:
# Slide Binus: https://newbinusmaya.binus.ac.id/lms/view-article/95c97bef-9fb0-42bd-9f54-90e0ca22e4e4/220b721d-8ba3-4e01-9488-2cbc9a246eb9/e5e7200b-2316-43e5-a075-aaaede75c4ab
# https://searchsecurity.techtarget.com/definition/promiscuous-mode
# https://www.codegrepper.com/code-examples/python/get+nth++character+of+string+python
# https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
# https://www.browserling.com/tools/letter-frequency
# https://www.geeksforgeeks.org/python-extract-string-after-nth-occurrence-of-k-character/
# https://docs.python.org/2/library/string.html#string.count
# https://www.programiz.com/python-programming/methods/string/count
# https://www.delftstack.com/howto/python/tuple-to-string-python/#use-the-str.join-function-to-convert-tuple-to-string-in-python
# https://stackabuse.com/convert-bytes-to-string-in-python/
# https://stackoverflow.com/questions/20024490/how-to-split-a-byte-string-into-separate-bytes-in-python