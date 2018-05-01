#!/usr/bin/env python
#Brock Ellefson Trent Baker
import sys
import socket
# import gui_programming
import threading
import level2
import time
import vec_control as vc

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
        s.bind(("10.200.33.219", self.port))
        while 1:
            s.listen(5)
            conn, addr = s.accept()
            # print("Android connected to server")
            data = conn.recv(1024)
            data = data.decode('ascii')
            # print('Android Message: {}'.format(data))
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
            # print ("Client connected")
            s.send(self.ttsmsg.encode('ascii')) #post to server
            # print('Sent message: ' + self.ttsmsg)
            s.close() #close connection

    def run(self):
        print ('Client Thread Starting\n')
        while True:
            if self.ttsmsg is not '': #if we have a message to send to Android
                self.runClient()
                self.ttsmsg = ''
                time.sleep(1)

class Listener:
    def __init__(self, server, game):
        self.server = server
        self.game = game

    def run(self):
        while True:

            #TODO use vec_control
            if self.server.data is not '':
                data = self.server.data
                data = data.lower()
                # print('Driver data: ' + data)
                if 'north' in data:
                    self.game.set_direction('north')
                elif 'south' in data:
                    self.game.set_direction('south')
                elif 'east' in data:
                    self.game.set_direction('east')
                elif 'west' in data:
                    self.game.set_direction('west')
                elif 'run' in data:
                    level2.set_choice('run')

                elif 'fight' in data:
                    level2.set_choice('fight')

                elif 'yes' in data:
                    pass


                self.server.resetData()
