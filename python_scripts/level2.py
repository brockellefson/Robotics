import random
import Network
import game
import vec_control

connections = {
    0: {'east': 1},
    1: {'east': 2, 'south': 4, 'west': 0},
    2: {'south': 5, 'west': 1},
    3: {'east': 4, 'south': 6},
    4: {'north': 1, 'south': 7, 'west': 3},
    5: {'north': 2},
    6: {'north': 3},
    7: {'north': 4, 'east': 8},
    8: {'west': 7},

    # 0---1---2
    #     |   |
    # 3---4   5
    # |   |
    # 6   7---8

    # valid start/end nodes are 0, 2, 6, 8
}
choice = ''

map_string = '0---1---2\n    |   |\n3---4   5\n|   |\n6   7---8'

prompt = '>  '

corners = [0, 2, 6, 8]

nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]

empty_board = [
    game.Node(''),
    game.Node(''),
    game.Node(''),
    game.Node(''),
    game.Node(''),
    game.Node(''),
    game.Node(''),
    game.Node(''),
    game.Node('')
]

tile_types = ['start', 'end', 'recharge', 'weak',
              'weak', 'weak', 'weak', 'strong', 'strong']

weak_enemy = game.Enemy(30, 10)
strong_enemy = game.Enemy(100, 35)


def welcome_message(client):
    client.ttsmsg = 'Welcome to Lloydsville. Home of the wicked. Lets begin'


def goodbye_message(client):
    client.ttsmsg = 'The Game is over. Good\'day'




def end_scenario(client):
    client.ttsmsg = 'Atta boi, you brought the key to the end of the Lloydsville. This means you win.'

def recharge_scenario(player, client):
    out = 'Call up Liquor Locker (brrt brrt!), bring me apple vodka\n'
    out += 'your health has been refilled'
    player.hp = 100
    #TODO: get lit
    #vec_control.get_lit()
    #print(out)
    client.ttsmsg = out

def combat_scenario(node, client):
    # print('hey partner, there\'s an enemy here\nHP: {}\nAM: {}\n'.format(enemy.hp, enemy.am))
    out = 'hey partner, there\'s an enemy here\n'
    out += 'HP: {}\nAM: {}'.format(node.enemy.hp, node.enemy.am)
    client.ttsmsg = out
    #print(out)

    fight_again = True
    while fight_again:
        choice = get_choice()
        if choice is not '':
            if choice == 'run':
                out = 'you try to run you pussy'
                if random.random() > 0.25:
                    out += 'and are just fast enough to escape'
                    out += '\nthe enemy is still here and if you re-enter this node, you must face it again'
                    fight_again = False
                else:
                    out += 'but get caught because you\'re slow'
                    choice = 'fight'
                client.ttsmsg = out
                #print(out)
            if choice == 'fight':
                print('you choose to fight')
                vec_control.attack_animation()
                node.player.hp -= int(random.random() * node.enemy.am)
                node.enemy.hp -= int(random.random() * node.player.am)

                # if either fighter has died
                if node.player.hp <= 0:
                    node.player.hp = 0
                    node.player.gameover = True
                    fight_again = False

                if node.enemy.hp <= 0:
                    node.enemy.hp = 0
                    node.cleared = True
                    fight_again = False
                    if node.key_node:
                        node.player.has_key = True

                out = 'after the fight, you have {} health left\n'.format(node.player.hp)
                out += '\t\tand the enemy has {} health left'.format(node.enemy.hp)
                if node.player.has_key and node.key_node:
                    out += '\nyou found some weird old key on the ground'
                #print(out)
                client.ttsmsg = out

def get_choice():
    global choice
    return choice

def set_choice(responce):
    global choice
    choice = responce
