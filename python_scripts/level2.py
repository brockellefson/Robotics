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

corners = [0, 2, 6, 8]

tile_types = ['start', 'end', 'recharge', 'weak', 'weak', 'weak', 'weak', 'strong', 'strong']

def start_scenario():
    print('you called an unimplemented method')
    pass

def end_scenario():
    print('end not implemented, letting you win for now cowboy')
    pass

def recharge_scenario():
    print('you called an unimplemented method')
    pass

def combat_scenario(type):
    enemy = game.Enemy(type)
    while enemy.alive:


def combat_speech(num_enemies):
    speech = 'there are {} enimies around me, what should i do?'.format(num_enemies)
    return return speech

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
    speech_choice = random.randint(0,3)
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
    speech_choice = random.randint(0,3)
    if speech_choice is 0:
        return 'im taking heat'
    elif speech_choice is 1:
        return 'ow that hurts'
    elif speech_choice is 2:
        return 'jesus that stings'
    elif speech_choice is 3:
        return 'tis but a flesh wound'
    return 'INVALID HIT OPTION'
