#!/usr/bin/env python
#Brock Ellefson Trent Baker
import sys
import socket
import threading

class Server:
    def __init__(self, port):
        self.port = port
        self.data = ''

    def processData(self, data):
        self.data = data

    def resetData(self):
        self.data = ''

    def runServer(self):
        print('Server starting')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", self.port))
        while 1:
            s.listen(5)
            conn, addr = s.accept()
            print("Android connected to server")
            data = conn.recv(1024)
            self.processData(data)
            s.close()

    def run(self):
        print ('Server Thread Starting\n')
        while True:
            self.runServer()




class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.ttsmsg = ''

    def runClient(self):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates socket
            s.connect((self.ip, self.port)) #connects us to server
            print ("Client connected")
            s.send(bytes(self.ttsmsg)) #post to server
            print('Sent message: ' + self.ttsmsg)
            s.close() #close connection

    def run(self):
        print ('Client Thread Starting\n')
        while True:
            if self.ttsmsg is not '': #if we have a message to send to Android
                self.runClient()
                self.ttsmsg = ''
