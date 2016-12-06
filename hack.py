print ('Welcome to Hackmaster calculator...')

player_list = {}

#Function to request player information
def  getPlayerInfo(player_number):
	player_name = input('Enter Player ' + str(player_number) + ' Name:')
	if player_name:
		if player_name not in player_list:
			player_speed = input('Enter Player ' + str(player_number) + ' Speed:')
			return player_name, int(player_speed)
		else:
			print ('Please enter a unique Player name.')
			return player_name, False
	else:
		return False, False
#Loop to get all remaining players name and speed
def getPlayers():
	player_number = 1
	player_name, player_speed = getPlayerInfo(player_number)
	while player_name:
		if player_name not in player_list:
			player_list[player_name] = player_speed
			player_number += 1
		player_name, player_speed = getPlayerInfo(player_number)

#runs get player function
getPlayers()
#error handling for empty player name on first entry
if not player_list:
	print ('You did not enter a name, did you mean to leave this blank.')
	getPlayers()
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
