
from client import Client

c = Client("192.168.2.2", 20001)

c.connect()

while True:
    print(c.receive())
