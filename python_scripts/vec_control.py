class Pose():
    # the pose class allows us to have many predefined poses and be able to access them intuitively
    def __init__(self):
        self.pose = [6000] * 17

    def __str__(self):
        out = ''
        for target in self.pose:
            out += str(target) + ' '
        return out

    @staticmethod
    def translate_to_servo(percent):
        return int((percent / 100) * 2000)
        # this lets us use percentages for range of motion because they are more intuitive

    def center_all(self):
        self.pose = [6000] * 17

    # we might want these to also make the robot move, but for now they just modify the pose
    # if we want them to move the robot, then we should call strike on some Controller
    # but then the Controller would need to be an instance/class variable

    def head_up(self, amount=50):
        self.pose[4] += self.translate_to_servo(amount)

    def head_down(self, amount=50):
        self.pose[4] -= self.translate_to_servo(amount)

    def head_left(self, amount=50):
        self.pose[3] += self.translate_to_servo(amount)

    def head_right(self, amount=50):
        self.pose[3] -= self.translate_to_servo(amount)

    def waist_left(self, amount=50):
        self.pose[0] -= self.translate_to_servo(amount)

    def waist_right(self, amount=50):
        self.pose[0] -= self.translate_to_servo(amount)


def main():
    a = Pose()

    print(a)
    a.head_left()
    print(a)
    a.head_right()
    a.head_right()
    print(str(a) + '\n')

    a.waist_left(100)
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
