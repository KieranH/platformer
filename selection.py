menu = ["Play", "Instructions"]

current_position = 0

def move_pos(num, list):
	global current_position
	if current_position + num < len(list) and current_position + num >= 0:
		current_position = current_position + num
	elif current_position + num == len(list):
		current_position = 0
	else: current_position = len(list) - 1
		
while True:
	input = raw_input("Direction: ")
	if input == "down":
		move_pos(1, menu)
	elif input == "up":
		move_pos(-1, menu)
	print menu[current_position]