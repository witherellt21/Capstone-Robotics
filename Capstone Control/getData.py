'''
Author: Taylor Witherell
Filename: data.py
Description: Instantiates the server class and includes methods for receiving data from the client, breaking it into isolated variables
and also has the ability for sending data back to the client.
'''

from server import Server

class Receiver():

    def __init__(self):
        self.server = Server("192.168.0.39", 1234)
        self.server.start()
        self.server.receiveConnection()

    def receive(self):
        msg = self.server.receive()
        if not msg == None:
            #print(msg)
            self.separateData(msg)
        if self.server.disconnect_counter == 5:
            self.server.receiveConnection()

    def send(self, string):
        self.server.send(string)

    def separateData(self, msg):
        self.datalist = msg.split(',')

    def getLidar(self):
        if len(self.datalist) > 1:
            return self.datalist[1].strip()

    def getTemp(self):
        if len(self.datalist) > 2:
            return self.datalist[2].strip()

    def getAccel(self):
        if len(self.datalist) > 0:
            return self.datalist[0].strip()

    def getAllData(self):
        if len(self.datalist) > 2:
            accel = self.datalist[0].strip()
            lidar = self.datalist[1].strip()
            temp = self.datalist[2].strip()

            return accel, lidar, temp


r = Receiver()

while True:
    r.receive()

    print("Received:  ", r.datalist, "\n")

    string = input("Type a message: ")
    r.send(string)

    print("\n")

    #print('Lidar =', r.getLidar())
    #print('Temp =', r.getTemp())
    #print('Accel =', r.getAccel())
    #if len(msg) > 0:
        #rint('hello')
    #print(msg)