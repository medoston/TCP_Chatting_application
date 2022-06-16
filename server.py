from encrypt import*
import socket
import threading


#SETTIG THE IP, PORTS And server
host = '127.0.0.1'
port = 55555
USERS = []
nicknames = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


# sending the messages
def send_MSG(message):
    for client in USERS:
        client.send(message)

def handle(client):
    while True:
        message = client.recv(1024)
        send_MSG(message)

def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected through {}".format(str(address)))

        #storing the nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        USERS.append(client)

        #Printing the nick Nickname
        print("pick a Nickname {}".format(nickname))
        send_MSG("*----------------------------------------------*\n\t\t{} joined!\n*----------------------------------------------*".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server is On....")
receive()

