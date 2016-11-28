print ('Welcome to Hackmaster calculator...')

player_list = {}
player_number = 1

#Asks for the first players name and speed
def getplayerinfo():
	player_name = input('Enter Player ' + str(player_number) + ' Name (blank to end):')
	if player_name:
		player_speed = input('Enter Player ' + str(player_number) + ' Speed:')
		return player_name, int(player_speed)
	else:
		return False, False
#Loop to get all remaining players name and speed
player_name, player_speed = getplayerinfo()
while player_name:
	player_list[player_name] = player_speed
	player_number += 1
	player_name, player_speed = getplayerinfo()
#outputs for players and their speeds
for name, speed in player_list.items():
    print (name + "'s", 'speed is', speed)
#loop to check each time in combat against the time intervals of all players
for time in range(1,101):
	combat_sequence = []
	for name, speed in player_list.items():
		if time % int(speed) == 0:
			 combat_sequence.append(name)
#when a time interval has a player turn, show what player(s) go in that time
	if combat_sequence:
		print ('On step', time, 'these players will go:', ', '.join(combat_sequence))
