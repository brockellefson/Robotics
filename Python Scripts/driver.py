import gui_programming
import Network
import threading

if __name__ == '__main__':
    object_L = [] #keeps track of objects, so we can kill their threads at the end

    #create network
    client = Network.Client('localhost', 4040)
    object_L.append(client)

    server = Network.Server(3030)
    object_L.append(server)

    #start all the objects
    thread_L = []
    for obj in object_L:
        thread_L.append(threading.Thread(target=obj.run))

    #start threads
    for t in thread_L:
        t.start()
        
    gui = gui_programming.GUI()
    gui.run()
