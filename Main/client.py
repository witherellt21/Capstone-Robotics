'''
Author: Taylor Witherell
Filename: client.py
Description: Contains client class for connecting to a host server and establishing a communications pipeline
'''

import socket

class Client():

    def __init__(self):
        self.IP = ''
        self.PORT = None
        self.s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    def connect( self ):
        self.s.connect( (self.IP, self.PORT) )

    def send( self, string ):
        self.s.sendall( bytes( string, "utf-8" )  )

    def receive( self ):
        msg = self.s.recv(1024)
        message = msg.decode(("utf-8"))
        #print(message)