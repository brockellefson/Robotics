import time


class Pose():
    # the pose class allows us to have many predefined poses and be able to access them intuitively
    def __init__(self, pose=[6000] * 18):
        self.pose = pose

    def __str__(self):
        out = ''
        for target in self.pose:
            out += str(target) + ' '
        return out

    @staticmethod
    def translate_to_servo(percent):
        return int((percent / 100) * 2000)
        # this lets us use percentages for range of motion because they are more intuitive

    def center(self):
        self.pose = [6000] * 17

    # head controls
    def head_up(self, amount=50):
        self.pose[4] += self.translate_to_servo(amount)

    def head_down(self, amount=50):
        self.pose[4] -= self.translate_to_servo(amount)

    def head_left(self, amount=50):
        self.pose[3] += self.translate_to_servo(amount)

    def head_right(self, amount=50):
        self.pose[3] -= self.translate_to_servo(amount)

    # waist controls
    def waist_left(self, amount=50):
        self.pose[0] -= self.translate_to_servo(amount)

    def waist_right(self, amount=50):
        self.pose[0] -= self.translate_to_servo(amount)

    # right arm
    def right_shoulder_inline_up(self, amount=50):
        self.pose[6] += self.translate_to_servo(amount)

    def right_shoulder_inline_down(self, amount=50):
        self.pose[6] -= self.translate_to_servo(amount)

    def right_shoulder_lateral_in(self, amount=50):
        self.pose[7] -= self.translate_to_servo(amount)

    def right_shoulder_lateral_out(self, amount=50):
        self.pose[7] += self.translate_to_servo(amount)

    def right_elbow_up(self, amount=50):
        self.pose[8] += self.translate_to_servo(amount)

    def right_elbow_down(self, amount=50):
        self.pose[8] -= self.translate_to_servo(amount)

    def right_wrist_bend_up(self, amount=50):
        self.pose[9] += self.translate_to_servo(amount)

    def right_wrist_bend_down(self, amount=50):
        self.pose[9] -= self.translate_to_servo(amount)

    def right_wrist_twist_cw(self, amount=50):
        self.pose[10] -= self.translate_to_servo(amount)

    def right_wrist_twist_ccw(self, amount=50):
        self.pose[10] += self.translate_to_servo(amount)

    def right_hand_open(self, amount=50):
        self.pose[11] -= self.translate_to_servo(amount)

    def right_hand_close(self, amount=50):
        self.pose[11] += self.translate_to_servo(amount)

    # left arm
    def left_shoulder_inline_up(self, amount=50):
        self.pose[12] -= self.translate_to_servo(amount)

    def left_shoulder_inline_down(self, amount=50):
        self.pose[12] += self.translate_to_servo(amount)

    def left_shoulder_lateral_in(self, amount=50):
        self.pose[13] -= self.translate_to_servo(amount)

    def left_shoulder_lateral_out(self, amount=50):
        self.pose[13] += self.translate_to_servo(amount)

    def left_elbow_up(self, amount=50):
        self.pose[14] += self.translate_to_servo(amount)

    def left_elbow_down(self, amount=50):
        self.pose[14] -= self.translate_to_servo(amount)

    def left_wrist_bend_up(self, amount=50):
        self.pose[15] += self.translate_to_servo(amount)

    def left_wrist_bend_down(self, amount=50):
        self.pose[15] -= self.translate_to_servo(amount)

    def left_wrist_twist_cw(self, amount=50):
        self.pose[16] -= self.translate_to_servo(amount)

    def left_wrist_twist_ccw(self, amount=50):
        self.pose[16] += self.translate_to_servo(amount)

    def left_hand_open(self, amount=50):
        self.pose[17] -= self.translate_to_servo(amount)

    def left_hand_close(self, amount=50):
        self.pose[17] += self.translate_to_servo(amount)


def spin_move(twists=10):
    a = Pose()
    a_con = Controller()
    delay = 0.35

    a.right_shoulder_lateral_out(200)
    a.left_shoulder_lateral_out(200)
    a_con.strike(a)

    while twists > 0:
        a.waist_left(200)
        a_con.strike(a)
        time.sleep(delay)
        a.waist_right(200)
        a_con.strike(a)
        time.sleep(delay)
        twists -= 1
        print(twists)

    a_con.release()


def attack_animation(chops=2):
    a = Pose()
    a_con = Controller()

    a.right_shoulder_lateral_out(100)
    a.right_elbow_up(100)
    a.left_shoulder_lateral_out(100)
    a.left_shoulder_inline_up(100)
    a.left_elbow_down(100)
    a_con.strike(a)

    while chops > 0:
        a.right_shoulder_inline_up(100)
        a.left_shoulder_inline_down(100)
        a_con.strike(a)
        time.sleep(1)

        a.right_shoulder_inline_down(100)
        a.left_shoulder_inline_up(100)
        a_con.strike(a)
        time.sleep(1)
        chops -= 1

    a_con.release()


def main():
    a = Controller()
    attack_animation(a)
    spin_move(a)


if __name__ == '__main__':
    from Maestro import Controller
    import time

    main()

'''
channels:
0 - waist
1 - wheels together
2 - wheels opposite
3 - head horizontal
4 - head vertical
5 -
6 - right_shoulder_inline
7 - right_shoulder_lateral
8 - right_elbow
9 - right_wrist_bend
10 -right_wrist_twist
11 - right_hand
12 - left_shoulder_inline
13 - left_shoulder_lateral
14 - left_elbow
15 - left_wrist_bend
16 - left_wrist_twist
17 -left_hand
'''
