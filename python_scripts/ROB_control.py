from Maestro import *

def main():
	# starting speed variables
	wheel_speed = 1000
	head_speed = 800
	waist_speed = 2000

	# initial setup
	ROB = Controller()
	ROB.setup()

	while True:
		# takes input from the keyboard
		input = getch()

		# wheel movement
		if 'w' in input:
			ROB.setTarget(1, 6000 - wheel_speed)
		if 'a' in input:
			ROB.setTarget(2, 6000 + wheel_speed)
		if 's' in input:
			ROB.setTarget(1, 6000 + wheel_speed)
		if 'd' in input:
			ROB.setTarget(2, 6000 - wheel_speed)
		if ' ' in input:
			ROB.setTarget(1, 6000)
			ROB.setTarget(2, 6000)

		# head movement
		if 'i' in input:
			ROB.setTarget(4, ROB.getPosition(4) + head_speed)
		if 'j' in input:
			ROB.setTarget(3, ROB.getPosition(3) + head_speed)
		if 'k' in input:
			ROB.setTarget(4, ROB.getPosition(4) - head_speed)
		if 'l' in input:
			ROB.setTarget(3, ROB.getPosition(3) - head_speed)

		# waist movement
		if 'n' in input:
			ROB.setTarget(8, ROB.getPosition(0) + waist_speed)
		if 'm' in input:
			ROB.setTarget(8, ROB.getPosition(0) - waist_speed)

		# speed selection
		if '1' in input:
			print('setting speed to granny')
			speed = 50
			wheel_speed = 700
		if '2' in input:
			print('setting speed to regular')
			speed = 100
			wheel_speed = 900
		if '3' in input:
			print('setting speed to speedy quick')
			speed = 200
			wheel_speed = 2000

		# utility
		if 'c' in input:
			ROB.center()
		if 'q' in input:
			ROB.center()
			print('later my dudes ;)')
			break

if __name__ == '__main__':
	main()
