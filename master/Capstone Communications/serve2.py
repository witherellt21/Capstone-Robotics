import socket

class Server():
    def __init__(self):
        self.IP = "192.168.0.39"
        self.PORT = 1236
        self.s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.s.bind((self.IP, self.PORT))
        self.s.listen()

    def receiveConnection(self):
        print('Awaiting connection to ', self.IP, ' at ', self.PORT)
        self.conn, self.addr = self.s.accept()
        self.disconnect_counter = 0
        print('Connected by', self.addr)

    def receive(self):
        data = self.conn.recv(1024)
        msg = data.decode("utf-8")
        if len(msg) > 0:
            return msg
        else:
            self.disconnect_counter += 1
        #print(data)
'''
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send( bytes( "Hey there!!!", "utf-8"))
    clientsocket.close()
'''

server = Server()
server.start()
server.receiveConnection()

while True:
    msg = server.receive()
    if not msg == None:
        print(msg)
    if server.disconnect_counter == 5:
        server.receiveConnection()
    #if len(msg) > 0:
        #rint('hello')
    #print(msg)