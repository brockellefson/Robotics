import random
from copy import deepcopy

import level2


class Node:
    def __init__(self, player, node_type=None, connections={}, index='ERROR'):
        self.index = index
        self.connections = connections
        self.node_type = node_type
        self.cleared = False
        self.key_node = False
        self.player = player

        if self.node_type == 'weak':
            self.enemy = deepcopy(level2.weak_enemy)
        elif self.node_type == 'strong':
            self.enemy = deepcopy(level2.strong_enemy)

    def __str__(self):
        return '{} node with connections: {}'.format(self.node_type, self.connections)

    def format_connections(self):
        out = ''
        for direction in self.connections:
            out += direction + ' or '
        return out[0:-4]

    def begin_scenario(self):
        if self.node_type == 'start':
            print('this is the start')
            # level2.start_scenario()
        elif self.node_type == 'end':
            print('this is the end')
            if self.player.has_key:
                print('you have a key')
                level2.end_scenario()
                return True
            else:
                print('but you don\'t have the key')
        elif self.node_type == 'recharge':
            level2.recharge_scenario(self.player)
        elif self.node_type == 'weak':
            print('this is a weak')
            level2.combat_scenario(self)
        elif self.node_type == 'strong':
            print('this is a strong')
            level2.combat_scenario(self)
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
        elif direction == 'quit':
            print('FORCE QUITTING')
            quit()
        else:
            print('invalid move')
            return self.index


class Player:
    def __init__(self, current_node=Node(''), health=100, gameover=False):
        self.current_node = current_node
        self.hp = health
        self.am = 100
        self.has_key = False
        self.gameover = gameover


class Game:
    def __init__(self, client=''):
        self.board = level2.empty_board
        self.events = level2.tile_types
        self.corners = level2.corners
        self.available = list(range(0, 9))
        self.player = Player()
        self.client = client

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
            self.board[index] = Node(self.player, event, level2.connections[index], index)
            self.available.remove(index)

            if event == 'start':
                self.player.current_node = self.board[index]
                if debug:
                    print('found start node at {}'.format(index))
            if debug:
                print('added {} to index {}'.format(self.board[index], index))

        random.shuffle(self.available)
        random.shuffle(self.events)
        placed_key = False

        # place the rest of the nodes
        for i in self.available:
            event = self.events.pop()
            self.board[i] = Node(self.player, event, level2.connections[i], i)

            if debug:
                print('added {} to index {}'.format(self.board[i], i))

            if event == 'strong' and not placed_key:
                placed_key = True
                self.board[i].key_node = True
                if debug:
                    print('placed the key at node {}'.format(i))

    def __str__(self):
        out = 'Current board:\n'
        for node in self.board:
            out += str(node) + '\n'
        return out

    def get_status(self):
        out = '\nThe map looks like this:\n'
        out += level2.map_string
        out += '\nYou are at node {}, would you like to move {}?'.format(self.player.current_node.index,
                                                                         self.player.current_node.format_connections())
        print(out)

    def play_game(self):
        level2.welcome_message()
        while not self.player.gameover:
            # main game loop here
            self.get_status()

            dir_choice = input(level2.prompt).lower()
            self.player.current_node = self.board[self.player.current_node.move(
                dir_choice)]
            if not self.player.current_node.cleared:
                if self.player.current_node.begin_scenario():
                    self.player.gameover = True
            else:
                print('This is a {} node that you have already cleared'.format(
                    self.player.current_node.node_type))
        level2.goodbye_message()


class Enemy:
    def __init__(self, hp=100, am=0):
        self.hp = hp
        self.am = am

    def roll_attack(self):
        rand = random.random()
        damage = self.am * rand
        print(damage)


def main():
    a = Game()
    a.create_board(True)

    a.play_game()


if __name__ == '__main__':
    main()
