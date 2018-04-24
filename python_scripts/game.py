import random
import tkinter as tk
import level2
import Network


class Game:
    def __init__(self, client=''):
        self.board = level2.empty_board
        self.events = level2.tile_types
        self.corners = level2.corners
        self.available = list(range(0, 9))
        self.current_node = Node()
        self.rob_health = 100
        self.client = client
        self.gameover = False
        self.player_prompt = '>'

    def create_board(self, debug=False):
        '''Generate the board from level2
        self.board = [Node]
        Nodes contain a type, a visited status,
        and a dictionary of connections
        '''

        random.shuffle(self.corners)

        # place start and end first
        while len(self.corners) > 2:
            index = self.corners.pop()
            self.board[index] = Node(self.events.pop(0), level2.connections[index])
            if debug:
                print('added {} to index {}'.format(self.board[index], index))

        # update available
        for corner in [0, 2, 6, 8]:
            if corner not in self.corners:
                self.available.remove(corner)
                if debug:
                    print('need to remove {} because it already has an type'.format(corner))

        random.shuffle(self.available)
        random.shuffle(self.events)

        # place the rest of the nodes
        for i in self.available:
            self.board[i] = Node(self.events.pop(), level2.connections[i])


        # add predefined connections
        if debug:
            print('adding connections')
        for i in range(len(self.board)):
            self.board[i].set_connections(level2.connections[i])
            self.board[i].index = i
            if self.board[i].node_type == 'start':
                self.current_node = self.board[i]
            if debug:
                print('added {} to node {}'.format(level2.connections[i], i))

    def __str__(self):
        out = 'Current board:\n'
        for node in self.board:
            out += str(node) + '\n'
        return out

    def get_status(self):
        out = '\nThe map looks like this:\n'
        out += level2.map_string
        out += '\nYou are at node {}, would you like to move {}?'.format(self.current_node.index,
                                                                         self.current_node.format_connections())
        print(out)

    def play_game(self):
        while not self.gameover:
            # main game loop here
            self.get_status()
            dir_choice = input(self.player_prompt).lower()
            self.current_node = self.board[self.current_node.move(dir_choice)]

            # self.gameover = True

    def run(self):
        self.create_board()
        current_node = self.board[0]
        self.client.ttsmsg = 'Welcome to Lloydsville. Home of the wicked. Lets begin'
        while self.gameover is False:
            if self.rob_health <= 0:
                self.client.ttsmsg = 'My health has been depleted.'
                self.gameover = True
                break
        print('Current Health: {}'.format(self.rob_health))
        # self.client.ttsmsg = 'I am at {}'.format(current_node)

        self.client.ttsmsg = 'The Game is over. Goodday'


class Node:
    def __init__(self, node_type=None, connections={}):
        self.index = 'ERROR'
        self.connections = connections
        self.node_type = node_type
        self.visited = False
        self.widget = None

    def __str__(self):
        return '{} node with connections: {}'.format(self.node_type, self.connections)

    def format_connections(self):
        out = ''
        for dir in self.connections:
            out += dir + ' or '
        return out[0:-4]

    def begin_scenario(self):
        self.visited = True
        if self.node_type == 'start':
            level2.start_scenario()
        elif self.node_type == 'end':
            level2.end_scenario()
        elif self.node_type == 'recharge':
            level2.recharge_scenario()
        elif self.node_type == 'weak':
            level2.combat_scenario(1)
        elif self.node_type == 'strong':
            level2.combat_scenario(2)
        else:
            print('INVALID TYPE DETECTED')

    def set_connections(self, connections):
        self.connections = connections

    def move(self, direction):
        if direction in self.connections:
            print('valid move')
            return self.connections[direction]
        elif direction == 'yes' and len(self.connections) == 1:
            for connection in self.connections:
                return self.connections[connection]
        else:
            print('invalid move')
            return self.index

    def make_widget(self):
        # I dont know what type of widget to make this class
        # or if this function even needs to exist
        # we do need some way to put the map on the gui
        self.widget = tk.PhotoImage(file='image_pngs/headv.png')
        return self.widget


class Enemy:
    def __init__(self, type):
        self.type = type
        self.target = target
        self.alive = True

        self.hp = 0
        if self.type is 1:
            self.hp = 100
        elif self.type is 2:
            self.hp = 150
        elif self.type is 3:
            self.hp = 200

    def hit(damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.alive = False

    def attack():
        return 10


def main():
    a = Game()
    a.create_board(True)
    # print(start_index)

    a.play_game()
    # while


if __name__ == '__main__':
    main()
