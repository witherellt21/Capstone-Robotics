from server import Server

IP = "192.168.2.2"
PORT = 20001

s = Server(IP, PORT)

s.start()

s.receiveConnection()

b = 0
while True:
    try:
        s.send(str(b))
        b = (b+1) % 10
    except:
        break

print('done')
s.close()