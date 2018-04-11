class Pose():
    # the pose class allows us to have many predefined poses and be able to access them intuitively
    def __init__(self):
        self.pose = [6000] * 17

    def __str__(self):
        out = ''
        for target in self.pose:
            out += str(target) + ' '
        return out

    # this lets us use percentages for range of motion because they are more intuitive
    def head_up(self, amount=2000):
        if amount != 2000:
            amount *= 40
        self.pose[4] += amount

    def head_down(self, amount=2000):
        if amount != 2000:
            amount *= 40
        self.pose[4] += amount

    def head_left(self, amount=1000):
        if amount != 1000:
            amount *= 40
        self.pose[3] += 1000

    def head_right(self, amount=1000):
        if amount != 1000:
            amount *= 40
        self.pose[3] -= 1000


def main():
    a = Pose()

    print(a)
    a.head_left()
    print(a)
    a.head_right()
    a.head_right()
    print(a)


if __name__ == '__main__':
    main()

'''
channels
0 - waist
1 - wheels together
2 - wheels opposite
3 - head horizontal
4 - head vertical
5 - 
6 -
7 -
8 -
9 -
10 -
11 -
12 -
13 -
14 -
15 -
16 -
17 -
'''
