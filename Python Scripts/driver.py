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

    while True:

        if server.data is not '':
            data = server.data
            data = data.lower()

            if data is 'rob go forward':
                gui.add_forward()
                client.ttsmsg = 'moving forward my dude'

            elif data is 'rob go backwards':
                gui.add_reverse()
                client.ttsmsg = 'moving backwards my dude'

            elif data is 'rob go left':
                gui.add_left()
                client.ttsmsg = 'moving left my dude'

            elif data is 'rob go right':
                gui.add_right()
                client.ttsmsg = 'moving right my dude'

            elif data is 'hit it my dude':
                gui.submit()
                client.ttsmsg = 'im gassing it'

            else:
                client.ttsmsg = 'fam what how can this even happen'

            server.resetData()
