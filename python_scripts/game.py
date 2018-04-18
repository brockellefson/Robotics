import random
import tkinter as tk
import level2


class Game:
    def __init__(self):
        self.board = []
        # easy, medium, hard, start, end, bars, shop, fun
        # self.events = [6, 5, 3, 1, 1, 3, 2, 4]
        self.events = ['start', 'end', 'recharge', 'weak', 'weak', 'weak', 'weak', 'strong', 'strong']

    def create_board(self):
        # creates all necessary nodes
        for i in range(len(self.events)):
            random.shuffle(self.events)

            # if you are about to place a start or end node anywhere but a corner,
            # shuffle until you place a valid node there instead
            while (self.events[-1] == 'start' or self.events[-1] == 'end') and i not in [0, 2, 6, 8]:
                random.shuffle(self.events)
                print('retry')
            # THIS CAN FAIL AND INFINITE LOOP
            # WE SHOULD FIX THAT
            self.board.append(Node(self.events.pop()))

        # add predefined connections
        for i in range(len(self.board)):
            self.board[i].set_connections(level2.connections[i])

    def __str__(self):
        out = 'Current board:\n'
        for node in self.board:
            out += str(node) + '\n'
        return out


class Node:
    def __init__(self, node_type, connections={}):
        self.connections = connections
        self.node_type = node_type

        self.widget = None

    def __str__(self):
        return '{} node with connections: {}'.format(self.node_type, self.connections)

    def begin_scenario(self):
        if node_type == 'start':
            print('you called an unimplemented method')
        elif node_type == 'end':
            print('you called an unimplemented method')
        elif node_type == 'recharge':
            print('you called an unimplemented method')
        elif node_type == 'weak':
            print('you called an unimplemented method')
        elif node_type == 'strong':
            print('you called an unimplemented method')
        else:
            print('you called an unimplemented method')
            print('INVALID TYPE DETECTED')

    def set_connections(self, connections):
        self.connections = connections

    def move(self, direction):
        if direction in self.connections:
            print('valid move')
            return True
        else:
            print('invalid move')
            return False

    def combat_scenario(self, battle):
        enl = []
        enemies = random.randint(1, 3)
        for enemy in enemies:
            enemy = Enemy(battle)
            enl.append(enemy)

        self.combat(enl)

    def combat(self, enemies):
        print('you called an unimplemented method')

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
        return 20


def main():
    a = Game()
    a.create_board()
    print(str(a) + '\n\n')

    a.board[0].move('north')
    a.board[0].move('east')


if __name__ == '__main__':
    main()
