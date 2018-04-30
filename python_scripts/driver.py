import gui_programming
import Network
import game
import threading

if __name__ == '__main__':
    object_L = [] #keeps track of objects, so we can kill their threads at the end

    #create network
    client = Network.Client('10.200.54.59', 4040)
    object_L.append(client)

    server = Network.Server(3030)
    object_L.append(server)

    game = game.Game(client)
    object_L.append(game)

    listener = Network.Listener(server, game)
    object_L.append(listener)

    #start all the objects
    thread_L = []
    for obj in object_L:
        thread_L.append(threading.Thread(target=obj.run))

    #start threads
    for t in thread_L:
        t.start()


