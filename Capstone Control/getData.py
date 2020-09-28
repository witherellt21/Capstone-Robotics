'''
Author: Taylor Witherell
Filename: data.py
Description: Instantiates the server class and includes methods for receiving data from the client, breaking it into isolated variables
and also has the ability for sending data back to the client.
'''

from server import Server

class Receiver():

    def __init__(self, IP, PORT):
        self.server = Server(IP, PORT)
        self.server.start()
        self.server.receiveConnection()

    def receive(self):
        msg = self.server.receive()
        self.datalist = []
        #msg = 'accel = 20, sonar = 30, temp = 70'
        if not msg == None:
            #print(msg)
            self.separateData(msg)
        #if self.server.disconnect_counter == 5:
            #self.server.receiveConnection()

    def send(self, string):
        self.server.send(string)

    def separateData(self, msg):
        self.datalist = msg.split(',,')

    def getTemp(self, last):
        for data in self.datalist:
            if 'temp' in data:
                try: return float(data.split('=')[1].strip())
                except: return last
        return last

    def getAccel(self, last):
        for data in self.datalist:
            if 'accel' in data.strip(' '):
                try: return data.split('=')[1].strip()
                except: return last
        return last
                
    def getGyro(self, last):
        for data in self.datalist:
            if 'gyro' in data:
                try: return data.split('=')[1].strip()
                except: return last
        return last

    def getSonar(self, last):
        for data in self.datalist:
            if 'sonar' in data:
                try: return float(data.split('=')[1].strip())
                except: return last
        return last

    def getAllData(self):
        if len(self.datalist) > 2:
            accel = self.datalist[0].strip()
            lidar = self.datalist[1].strip()
            temp = self.datalist[2].strip()

            return accel, lidar, temp

'''

r = Receiver('192.168.0.2', 1234)

accel = ''
sonar = ''
imu = ''

msgs = ['accel = 20, sonar = 30, temp = 70', 'sonar = 30, temp = 70']

i = 0
while True:

    if i > len(msgs)-1:
        break

    #msg = r.receive()
    msg = msgs[i]

    r.separateData(msg)



    accel = r.getAccel(accel)
    sonar = r.getSonar(sonar)
    imu = r.getIMU(imu)

    print("Received:  ", r.datalist, "\n")

    #string = input("Type a message: ")
    #r.send(string)

    print("\n")

    i += 1

    #print('Lidar =', r.getLidar())
    #print('Temp =', r.getTemp())
    #print('Accel =', r.getAccel())
    #if len(msg) > 0:
        #rint('hello')
    #print(msg)
'''
