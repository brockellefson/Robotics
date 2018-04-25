import random

import game

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


def welcome_message():
    print('Welcome to Lloydsville. Home of the wicked. Lets begin')


def goodbye_message():
    print('The Game is over. Good\'day')


def start_scenario():
    print('you called an unimplemented method')
    pass


def end_scenario():
    print('Atta boi, you brought the key to the end of the Lloydsville. This means you win.')


def recharge_scenario(player):
    out = 'Call up Liquor Locker (brrt brrt!), bring me apple vodka\n'
    out += 'your health has been refilled'
    player.hp = 100
    print(out)

    pass


def combat_scenario(node):
    # print('hey partner, there\'s an enemy here\nHP: {}\nAM: {}\n'.format(enemy.hp, enemy.am))
    out = 'hey partner, there\'s an enemy here\n'
    out += 'HP: {}\nAM: {}'.format(node.enemy.hp, node.enemy.am)
    print(out)

    fight_again = True
    while fight_again:
        choice = input('are you going to run or fight?\n' + prompt)
        if choice == 'run':
            out = 'you try to run '
            if random.random() > 0.25:
                out += 'and are just fast enough to escape'
                out += '\nthe enemy is still here and if you re-enter this node, you must face it again'
                fight_again = False
            else:
                out += 'but get caught because you\'re slow'
                choice = 'fight'
            print(out)
        if choice == 'fight':
            print('you choose to fight')

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
            if node.player.has_key:
                out += '\nyou found some weird old key on the ground'
            print(out)


def strong_scenario():
    print('you called an unimplemented method')
    pass


def combat_speech(num_enemies):
    speech = 'there are {} enimies around me, what should i do?'.format(
        num_enemies)
    return speech


def recharge_speech():
    speech = 'recharging to full health. beep bop boop.'
    return speech


def key_speech():
    speech = 'i found a key, i wonder what it unlocks'
    return speech


def chest_speech_nokey():
    speech = 'i found a chest, i wonder where the key is'
    return speech


def chest_speech():
    speech = 'ive unlocked the chest, mission complete'
    return speech


def attack_speech():
    speech_choice = random.randint(0, 3)
    if speech_choice is 0:
        return 'im attacking'
    elif speech_choice is 1:
        return 'on, guard slime'
    elif speech_choice is 2:
        return 'im going to enjoy this'
    elif speech_choice is 3:
        return 'hello my name is inigo montoya. you killed my father. prepare to die'
    return 'INVALID ATTACK OPTION'


def hit_speech():
    speech_choice = random.randint(0, 3)
    if speech_choice is 0:
        return 'im taking heat'
    elif speech_choice is 1:
        return 'ow that hurts'
    elif speech_choice is 2:
        return 'jesus that stings'
    elif speech_choice is 3:
        return 'tis but a flesh wound'
    return 'INVALID HIT OPTION'
