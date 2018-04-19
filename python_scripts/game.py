import random
import tkinter as tk
import level2


class Game:
    def __init__(self):
        self.board = []
        self.events = level2.tile_types
        self.current_node = Node()

    def create_board(self, debug=False):
        '''Generate the board from level2
        self.board = [Node]
        Nodes contain a type, a visited status,
        and a dictionary of connections
        '''
        fail_count = 0

        # creates all necessary nodes
        for i in range(len(self.events)):
            random.shuffle(self.events)
            # if you are about to pop a start or end node anywhere but a corner,
            # shuffle until you place a valid node there instead
            while (self.events[-1] == 'start' or self.events[-1] == 'end') and i not in level2.corners:
                random.shuffle(self.events)
                fail_count += 1
                if fail_count > 20:
                    swap_corner = random.choice(level2.corners[:-1])
                    if debug:
                        print('Reached an invalid state. Swapping for {} to resolve'.format(swap_corner))
                    temp = self.board[swap_corner]
                    self.board[swap_corner] = Node(self.events.pop())
                    self.events.append(temp.node_type)
            if debug:
                print('adding {} to the list at index {}'.format(self.events[-1], i))
            temp_node = Node(self.events.pop())
            self.board.append(temp_node)
            if temp_node.node_type == 'start':
                self.current_node = self.board[-1]
            fail_count = 0

        # add predefined connections
        for i in range(len(self.board)):
            self.board[i].set_connections(level2.connections[i])

    def __str__(self):
        out = 'Current board:\n'
        for node in self.board:
            out += str(node) + '\n'
        return out


class Node:
    def __init__(self, node_type=None, connections={}):
        self.connections = connections
        self.node_type = node_type
        self.visited = False
        self.game_completed = False

        self.widget = None

    def __str__(self):
        return '{} node with connections: {}'.format(self.node_type, self.connections)

    def start_scenario(self):
        print('you called an unimplemented method')
        pass

    def end_scenario(self):
        print('end not implemented, letting you win for now cowboy')
        self.game_completed = True
        pass

    def recharge_scenario(self):
        print('you called an unimplemented method')
        pass

    def weak_scenario(self):
        print('you called an unimplemented method')
        pass

    def strong_scenario(self):
        print('you called an unimplemented method')
        pass

    def begin_scenario(self):
        self.visited = True
        if self.node_type == 'start':
            self.start_scenario()
        elif self.node_type == 'end':
            self.end_scenario()
        elif self.node_type == 'recharge':
            self.recharge_scenario()
        elif self.node_type == 'weak':
            self.weak_scenario()
        elif self.node_type == 'strong':
            self.strong_scenario()
        else:
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
    # print(start_index)

    a.board[0].move('north')
    a.board[0].move('east')

    # while


if __name__ == '__main__':
    main()
