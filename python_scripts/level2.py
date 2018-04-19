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
