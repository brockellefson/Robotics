#!/usr/bin/env python
#Brock Ellefson Trent Baker
import sys
import socket
import gui_programming
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
        s.bind(("10.200.1.118", self.port))
        while 1:
            s.listen(5)
            conn, addr = s.accept()
            print("Android connected to server")
            data = conn.recv(1024)
            data = data.decode('ascii')
            print('Android Message: {}'.format(data))
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
            s.send(self.ttsmsg.encode('ascii')) #post to server
            print('Sent message: ' + self.ttsmsg)
            s.close() #close connection

    def run(self):
        print ('Client Thread Starting\n')
        while True:
            if self.ttsmsg is not '': #if we have a message to send to Android
                self.runClient()
                self.ttsmsg = ''

class Listener:
    def __init__(self, server, client, game):
        self.server = server
        self.client = client
        self.gui = gui

    def run(self):
        while True:

            #TODO use vec_control
            if self.server.data is not '':
                data = self.server.data
                data = data.lower(
                print('Driver data: ' + data)
                if 'forward' in data:
                    self.gui.add_forward()
                    self.client.ttsmsg = 'moving north my dude'

                elif 'reverse' in data:
                    self.gui.add_reverse()
                    self.client.ttsmsg = 'moving south my dude'

                elif 'left' in data:
                    self.gui.add_left()
                    self.client.ttsmsg = 'moving east my dude'

                elif 'center' in data:
                    self.gui.add_center()
                    self.client.ttsmsg = 'im straight as an arrow'

                elif 'delete' in data:
                    self.gui.clear_program()
                    self.client.ttsmsg = 'kill myself l m a o'

                elif 'right' in data:
                    self.gui.add_right()
                    self.client.ttsmsg = 'moving west my dude'

                elif 'start' in data:
                    self.gui.submit()


                self.server.resetData()
