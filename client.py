import socket
from threading import Thread

targetPort = 0

print("What's your name?")
clientName = input(">> ")

if clientName == "Ulet":
    targetPort = 8080

elif clientName == "Keket":
    targetPort = 8081

else:
    print("Invalid name! Please try again!")

# print(targetPort)

client = socket.socket()
client.connect(("127.0.0.1", targetPort))

print("You have connected to the server")

def readMessage(client: socket.socket):
    while True:
        message = client.recv(1024).decode()
        if message == "exit":
            client.close()
            break
        print(f"\nServer: {message}\nYou: ", end='')

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