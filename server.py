import socket
from threading import Thread

username = ""
uletIP = ""
uletPort = 0
keketIP = ""
keketPort = 0

print("Welcome back, Server, which chat do you want to host / connect to?")
print("1. Ulet")
print("2. Keket")

chatTarget = input(">> ")
# print(f"your target: {chatTarget}")
# print(type(chatTarget))

if chatTarget == '1':
    uletSocket = socket.socket()
    uletIP = "127.0.0.1"
    uletPort = 8080
    username = "Ulet"
    # print(uletIP)
    # print(uletPort)
    uletSocket.bind((uletIP, uletPort))
    uletSocket.listen(3)
    client, addr = uletSocket.accept()
    # print(client)
    # print(addr)
elif chatTarget == '2':
    keketSocket = socket.socket()
    keketIP = "127.0.0.1"
    keketPort = 8081
    username = "Keket"
    # print(keketIP)
    # print(keketPort)
    keketSocket.bind((keketIP, keketPort))
    keketSocket.listen(3)
    client, addr = keketSocket.accept()
    # print(client)
    # print(addr)
else:
    print("Invalid chat, please try again")


print(f"{username} has connected..")
# print(chatTarget)

def readMessage(client: socket.socket):
    while True:
        message = client.recv(1024).decode()
        if message == "exit":
            client.close()
            break
        print(f"\n{username}: {message}\nYou: ", end='')
        # print(message, end='')

def sendMessage(client: socket.socket):
    while True:
        message = input('You: ')
        if message == "exit":
            client.close()
            print("Thank you")
            break
        client.send(message.encode())

tr = Thread(target=readMessage, args=(client, ))
ts = Thread(target=sendMessage, args=(client, ))

tr.start()
ts.start()

# tr.join()
# ts.join()

# print("Thank you")