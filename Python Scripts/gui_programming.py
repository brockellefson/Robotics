import tkinter as tk
#from Maestro import *
from time import sleep
import threading

class GUI:
	def __init__(self):
		self.main_window = tk.Tk()
		self.command_list = []
		self.row = 0
		self.column = 3

		self.commands_done = False

		self.window_width = self.main_window.winfo_screenwidth()
		self.window_height = self.main_window.winfo_screenheight()

		#self.ROB = Controller()
		#self.ROB.setup()

	def increment_coords(self):
		self.column += 1
		if self.column >= 8:
			self.column = 3
			self.row += 1


	# add_* adds a corresponding command widget to the grid
	def add_forward(self):
		temp = tk.Scale(self.main_window, from_ = 0, to = 10, orient = 'horizontal', label = 'Forward (seconds)', length = 105)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('w')
		self.increment_coords()


	def add_left(self):
		temp = tk.Scale(self.main_window, from_ = 0, to = 10, orient = 'horizontal', label = 'Left (seconds)', length = 105)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('a')
		self.increment_coords()


	def add_reverse(self):
		temp = tk.Scale(self.main_window, from_ = 0, to = 10, orient = 'horizontal', label = 'Reverse (seconds)', length = 105)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('s')
		self.increment_coords()


	def add_right(self):
		temp = tk.Scale(self.main_window, from_ = 0, to = 10, orient = 'horizontal', label = 'Right (seconds)', length = 105)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('d')
		self.increment_coords()


	def add_center(self):
		temp = tk.Scale(self.main_window, from_ = 0, to = 0, orient = 'horizontal', label = 'Center (seconds)', length = 105)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('c')
		self.increment_coords()


	def add_head_vert(self):
		temp = tk.Scale(self.main_window, from_ = -2, to = 2, orient = 'horizontal', label = 'Head vert', length = 105)
		temp.set(0)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('head_vert')
		self.increment_coords()


	def add_head_horz(self):
		temp = tk.Scale(self.main_window, from_ = -2, to = 2, orient = 'horizontal', label = 'Head horz', length = 105)
		temp.set(0)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('head_horz')
		self.increment_coords()


	def add_waist(self):
		temp = tk.Scale(self.main_window, from_ = -1, to = 1, orient = 'horizontal', label = 'Waist', length = 105)
		temp.set(0)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('waist')
		self.increment_coords()


	def add_noop(self):
		temp = tk.Scale(self.main_window, from_ = 0.0, to = 5.0, bigincrement = 0.2, orient = 'horizontal', label = 'Wait tenth seconds', length = 105)
		temp.set(0)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('noop')
		self.increment_coords()


	def set_speed(self):
		temp = tk.Scale(self.main_window, from_ = 1, to = 3, orient = 'horizontal', label = 'Speed', length = 105)
		temp.set(1)
		temp.grid(row = self.row, column = self.column)
		self.command_list.append('speed')
		self.increment_coords()


	# commands will be returned in output_list in the form
	# [[key_1, duration_1], [key_2, duration_2]]
	def submit(self):
		output_list = []
		next_command = 0

		children = self.main_window.winfo_children()

		# scrape the grid for durations
		for i in range(len(children)):
			if type(children[i]) == tk.Scale:
				output_list.append([self.command_list[next_command], children[i].get()])
				next_command += 1
		print(output_list)

		print('translating commands')
		self.translate_commands(output_list)
		self.commands_done = True

		return output_list


	def clear_program(self):
		# sets the global variables to their default values
		self.command_list = []
		next_command = 0

		# reset self.row and self.column position of new actions
		self.row = 0
		self.column = 3

		# removes all command widgets
		children = self.main_window.winfo_children()
		for child in children:
			if type(child) == tk.Scale:
				child.destroy()


	def stop_wheels(self):
		self.ROB.setTarget(1, 6000)
		self.ROB.setTarget(2, 6000)
		self.ROB.center()



	# takes in a list of commands from submit and calls actually turns the motors
	def translate_commands(self, program):
		wheel_speed = 1000
		head_speed = 800
		waist_speed = 2000

		for command in program:
			input = command[0]
			duration = command[1]
			try:
				# wheel movement
				if 'w' == input:
					self.ROB.setTarget(1, 6000 - wheel_speed)
					sleep(duration)
					self.stop_wheels()
				if 'a' == input:
					self.ROB.setTarget(2, 6000 + wheel_speed)
					sleep(duration)
					self.stop_wheels()
				if 's' == input:
					self.ROB.setTarget(1, 6000 + wheel_speed)
					sleep(duration)
					self.stop_wheels()
				if 'd' == input:
					self.ROB.setTarget(2, 6000 - wheel_speed)
					sleep(duration)
					self.stop_wheels()
				if ' ' == input:
					sleep(duration)
					self.stop_wheels()

				# head movement
				if 'head_vert' == input:
					self.ROB.setTarget(4, 6000 + (duration * head_speed))
				if 'head_horz' == input:
					self.ROB.setTarget(3, 6000 + (duration * head_speed))

				# waist movement
				if 'waist' == input:
					self.ROB.setTarget(0, 6000 + (waist_speed * duration))

				# speed selection
				# TODO: change these to accept input from the self.command_list
				if '1' == input:
					print('setting speed to granny')
					speed = 50
					wheel_speed = 700
				if '2' == input:
					print('setting speed to regular')
					speed = 100
					wheel_speed = 900
				if '3' == input:
					print('setting speed to speedy quick')
					speed = 200
					wheel_speed = 2000

				# utility
				if 'c' == input:
					self.ROB.center()
				if 'noop' == input:
					sleep(duration / 10)
			except Exception as e:
				print('Caught error: {}'.format(e))


	def main(self):
		# calculating scaling factors
		old_width = 32
		old_height = 32
		new_width = 64
		new_height = 64

		scale_w = int(new_width / old_width)
		scale_h = int(new_height / old_height)

		# create images for buttons
		up = tk.PhotoImage(file = "image_pngs/up.png").zoom(scale_w, scale_h)
		left = tk.PhotoImage(file = "image_pngs/left.png").zoom(scale_w, scale_h)
		right = tk.PhotoImage(file = "image_pngs/right.png").zoom(scale_w, scale_h)
		down = tk.PhotoImage(file = "image_pngs/down.png").zoom(scale_w, scale_h)
		center = tk.PhotoImage(file = "image_pngs/center.png").zoom(scale_w, scale_h)
		headh = tk.PhotoImage(file = "image_pngs/headh.png").zoom(scale_w, scale_h)
		headv = tk.PhotoImage(file = "image_pngs/headv.png").zoom(scale_w, scale_h)
		speed = tk.PhotoImage(file = "image_pngs/speed.png").zoom(scale_w, scale_h)
		play = tk.PhotoImage(file = "image_pngs/play.png").zoom(scale_w, scale_h)
		stop = tk.PhotoImage(file = "image_pngs/stop.png").zoom(scale_w, scale_h)
		trash = tk.PhotoImage(file = "image_pngs/trash.png").zoom(scale_w, scale_h)
		waist = tk.PhotoImage(file = "image_pngs/waist.png").zoom(scale_w, scale_h)
		wait = tk.PhotoImage(file = "image_pngs/wait.png").zoom(scale_w, scale_h)

		# movement buttons
		forward_button = tk.Button(self.main_window, text = 'Forward',image = up, command = self.add_forward)
		left_button = tk.Button(self.main_window, text = 'Left',image = left, command = self.add_left)
		reverse_button = tk.Button(self.main_window, text = 'Reverse',image = down, command = self.add_reverse)
		right_button = tk.Button(self.main_window, text = 'Right',image = right , command = self.add_right)

		forward_button.grid(column = 1, row = 0)
		left_button.grid(column = 0, row = 1)
		reverse_button.grid(column = 1, row = 2)
		right_button.grid(column = 2, row = 1)

		# head buttons
		head_vert = tk.Button(self.main_window, text = 'Head\nvert', image = headv, command = self.add_head_vert)
		head_horz = tk.Button(self.main_window, text = 'Head\nhorz',image = headh, command = self.add_head_horz)

		head_vert.grid(column = 0, row = 2)
		head_horz.grid(column = 2, row = 2)

		# waist button
		waist_button = tk.Button(self.main_window, text = 'Waist', image = waist, command = self.add_waist)
		waist_button.grid(column = 1, row = 3)

		# utility buttons
		center_button = tk.Button(self.main_window, text = 'Center', image = center, command = self.add_center)
		submit_button = tk.Button(self.main_window, text = 'Submit', image = play, command = self.submit)
		clear_button = tk.Button(self.main_window, text = 'Clear', image = trash, command = self.clear_program)
		speed_button = tk.Button(self.main_window, text = 'Speed', image = speed, command = self.set_speed)
		noop_button = tk.Button(self.main_window, text = 'No op',image = wait, command = self.add_noop)

		center_button.grid(column = 1, row = 1)
		submit_button.grid(column = 0, row = 0)
		clear_button.grid(column = 2, row = 0)
		speed_button.grid(column = 0, row = 3)
		noop_button.grid(column = 2, row = 3)

		self.main_window.geometry("%dx%d%+d%+d" % (self.window_width, self.window_height, 0, 0))

		self.main_window.mainloop()


	def run(self):
		print("GUI Starting")
		self.main()
