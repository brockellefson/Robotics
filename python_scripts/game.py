import random
import tkinter as tk
import level2
# import Network


class Game:
    def __init__(self, client=''):
        self.board = level2.empty_board
        self.events = level2.tile_types
        self.corners = level2.corners
        self.available = list(range(0, 9))
        self.current_node = Node()
        self.rob_health = 100
        self.client = client
        self.hasKey = True
        self.gameover = False
        self.player_prompt = '> '

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
            event = self.events.pop(0)
            self.board[index] = Node(event, level2.connections[index], index)
            self.available.remove(index)

            if event == 'start':
                self.current_node = self.board[index]
                if debug:
                    print('found start node at {}'.format(index))
            if debug:
                print('added {} to index {}'.format(self.board[index], index))

        random.shuffle(self.available)
        random.shuffle(self.events)

        # place the rest of the nodes
        for i in self.available:
            self.board[i] = Node(self.events.pop(), level2.connections[i], i)

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
            if not self.current_node.visited:
                if self.current_node.begin_scenario(self.hasKey):
                    self.gameover = True
            else:
                print('This is a {} node that you have already visited'.format(self.current_node.node_type))


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
    def __init__(self, node_type=None, connections={}, index='ERROR'):
        self.index = index
        self.connections = connections
        self.node_type = node_type
        self.visited = False

    def __str__(self):
        return '{} node with connections: {}'.format(self.node_type, self.connections)

    def format_connections(self):
        out = ''
        for dir in self.connections:
            out += dir + ' or '
        return out[0:-4]

    def begin_scenario(self, hasKey=False):
        self.visited = True
        if self.node_type == 'start':
            print('this is the start')
            # level2.start_scenario()
        elif self.node_type == 'end':
            print('this is the end')
            if hasKey:
                print('you have a key')
                level2.end_scenario()
                return True
            else:
                print('but you don\'t have the key')
        elif self.node_type == 'recharge':
            print('this is a recharge')
            # level2.recharge_scenario()
        elif self.node_type == 'weak':
            print('this is a weak')
            # level2.combat_scenario(1)
        elif self.node_type == 'strong':
            print('this is a strong')
            # level2.combat_scenario(2)
        else:
            print('INVALID TYPE DETECTED')
        return False

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
