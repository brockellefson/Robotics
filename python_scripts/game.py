import random
import tkinter as tk


class Game:
    def __init__(self):
        self.board = []
        # easy, medium, hard, start, end, bars, shop, fun
        self.events = [6, 5, 3, 1, 1, 3, 2, 4]

    def create_node(self):
        event_type = random.randint(0, len(self.events))
        type_s = ''
        if event_type is 0:
            type_s = 'easy'
        elif event_type is 1:
            type_s = 'medium'
        elif event_type is 2:
            type_s = 'hard'
        elif event_type is 3:
            type_s = 'start'
        elif event_type is 4:
            type_s = 'end'
        elif event_type is 5:
            type_s = 'bars'
        elif event_type is 6:
            type_s = 'shop'
        elif event_type is 7:
            type_s = 'fun'
        self.events[event_type] = self.events[event_type] - 1
        if self.events[event_type] is 0:
            self.events.pop(event_type)
        return Node(type_s)

    def create_board(self):
        for count in range(25):
            x = self.create_node()
            self.board.append(x)

        self.board[0].set_east(self.board[1])

        self.board[1].set_west(self.board[0])
        self.board[1].set_east(self.board[2])
        self.board[1].set_south(self.board[6])

        self.board[2].set_west(self.board[1])
        self.board[2].set_south(self.board[7])

        self.board[3].set_east(self.board[4])

        self.board[4].set_west(self.board[3])
        self.board[4].set_south(self.board[9])

        self.board[5].set_east(self.board[6])
        self.board[5].set_south(self.board[10])

        self.board[6].set_west(self.board[5])
        self.board[6].set_south(self.board[11])
        self.board[6].set_north(self.board[1])

        self.board[7].set_north(self.board[1])

        self.board[8].set_east(self.board[9])
        self.board[8].set_south(self.board[13])

        self.board[9].set_north(self.board[4])
        self.board[9].set_west(self.board[8])
        self.board[9].set_south(self.board[14])

        self.board[10].set_north(self.board[5])
        self.board[10].set_south(self.board[15])

        self.board[11].set_east(self.board[12])
        self.board[11].set_north(self.board[6])

        self.board[12].set_west(self.board[11])
        self.board[12].set_east(self.board[13])

        self.board[13].set_north(self.board[8])
        self.board[13].set_south(self.board[18])
        self.board[13].set_west(self.board[12])

        self.board[14].set_north(self.board[9])
        self.board[14].set_south(self.board[19])

        self.board[15].set_north(self.board[10])
        self.board[15].set_east(self.board[16])

        self.board[16].set_west(self.board[15])
        self.board[16].set_south(self.board[21])

        self.board[17].set_south(self.board[22])

        self.board[18].set_north(self.board[13])
        self.board[18].set_east(self.board[19])
        self.board[18].set_south(self.board[23])

        self.board[19].set_west(self.board[18])
        self.board[19].set_north(self.board[14])

        self.board[20].set_east(self.board[21])

        self.board[21].set_west(self.board[20])
        self.board[21].set_north(self.board[17])
        self.board[21].set_east(self.board[22])

        self.board[22].set_west(self.board[21])
        self.board[22].set_north(self.board[17])

        self.board[23].set_north(self.board[18])
        self.board[23].set_east(self.board[24])

        self.board[24].set_west(self.board[23])


class Node:
    def __init__(self, type):
        self.north = False
        self.south = False
        self.east = False
        self.west = False
        self.type = type

        self.widget = None

    def begin_scenario(self):
        if type is 'easy':
            self.combat_scenario(1)
        elif type is 'bar':
            # do bar
            print('you called an unimplemented method')
        elif type is 'fun':
            # do fun
            print('you called an unimplemented method')
        elif type is 'shop':
            # do bar
            print('you called an unimplemented method')
        elif type is 'medium':
            self.combat_scenario(2)
        elif type is 'hard':
            self.combat_scenario(3)
        elif type is 'start':
            # do start
            print('you called an unimplemented method')
        elif type is 'end':
            # do end
            print('you called an unimplemented method')

    def set_north(self, node):
        self.north = True
        self.n_node = node

    def set_south(self, node):
        self.south = True
        self.s_node = node

    def set_east(self, node):
        self.east = True
        self.e_node = node

    def set_west(self, node):
        self.west = True
        self.w_node = node

    def go_north(self):
        if self.north:
            return self.n_node
        return None

    def go_south(self):
        if self.south:
            return self.s_node
        return None

    def go_east(self):
        if self.east:
            return self.e_node
        return None

    def go_west(self):
        if self.west:
            return self.w_node
        return None

    def combat_scenario(battle):
        enl = []
        enemies = random.randint(1, 3)
        for enemy in enemies:
            enemy = Enemy(battle)
            enl.append(enemy)

        self.combat(enl)

    def combat(enemies):
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
