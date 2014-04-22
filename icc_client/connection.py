# Template from Ryan Chiu. See https://code.google.com/p/ics-bot-maker/

from select import select
import socket
import sms
import sys
import datetime

class Connection:

    def __init__(self, server_host, server_port, server_prompt,
                 username, password, buffer_size, preferences):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.buffer_size = buffer_size        
        self.server_host = server_host
        self.server_port = server_port
        self.server_prompt = server_prompt
        self.username = username
        self.password = password
        self.sock.connect((self.server_host, self.server_port))
        self.sms = sms.SMS()
        self.min_5, self.min_3, self.min_blitz = (preferences.min_5, preferences.min_3, preferences.min_blitz)
	#self.send_message('Started up!')

    def connect(self, listening=False):
        # Print data until server prompts for a username, in which case it
        # will be entered.
        self.read_until('login: ')
        self.write_line(self.username)

        # Ditto for the password
        self.read_until('password: ')
        self.write_line(self.password)

	curr_time = datetime.datetime.utcnow()
        
	#If 59 minutes have passed, close the connection.
        while (datetime.datetime.utcnow() - curr_time).seconds < 3540:
            line = self.read_line()
	    if line and listening:
		self.process_line(line.strip())

	print("59 minutes have passed, connection closed")
	self.sock.close()

    def process_line(self, line):
	if line.startswith('Game notification:'):
	    self.handle_game_notification(line)

    #If the game notification is of high enough interest, send an SMS.
    def handle_game_notification(self, notification):
	tokens = notification.rsplit(' ')
	player1 = tokens[2]
	try:
		player1_rating = int(tokens[3].strip('()'))
	except ValueError:
		player1_rating = 0
	player2 = tokens[5]
	try:
		player2_rating = int(tokens[6].strip('()'))
	except ValueError:
		player2_rating = 0
	time_control = tokens[8]
	players = [player1.lower(), player2.lower()]
	key_players = ['capilanobridge', 'adaptation', 'depressnyak',
		'velimirovich', 'rafaello', 'dsquared', 'azerichess',
		'mlraka', 'egor-geroev2', 'andreagassi']

	for player in key_players:
		if player in players:
			self.send_message('%s is playing!' % player)
			return

	if time_control == '3-minute':
		if (player1_rating + player2_rating > self.min_3 or
				max(player1_rating, player2_rating) > 2600):
			self.send_message('%s(%d) vs. %s(%d) 3min' % (
				player1, player1_rating, player2, player2_rating))

	elif time_control == '5-minute':
		if (player1_rating + player2_rating > self.min_5 or
				max(player1_rating, player2_rating) > 2700):			
			self.send_message('%s(%d) vs. %s(%d) 5min' % (
				player1, player1_rating, player2, player2_rating))

	elif time_control == 'blitz':
		if player1_rating + player2_rating > self.min_blitz:
			self.send_message('%s(%d) vs %s(%d) blitz' % (
				player1, player1_rating, player2, player2_rating))

    def is_online(self, player):
	self.write_line('finger ' + player)
	lines = []
	for _ in range(3):
		lines.append(self.read_line())
	for line in lines:
		if line:
			if 'Statistics' in line:
				return True
	return False

    def send_message(self, message):
	#If danieldelpaso is online, don't send the message.
	if self.is_online('danieldelpaso'):
		return
	self.sms.send_sms(message)

    def read_line(self):
	readlist, _, _ = select([self.sock, sys.stdin], [], [])
	for sock in readlist:
		if sock == sys.stdin:
			command = sys.stdin.readline()
			self.write_line(command)
			#print('Sending command: %s' % command)
		if sock == self.sock:
        		recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
        		print recv
			return recv

    def read_until(self, end_str):
        recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
        while end_str not in str(recv):
        	print recv

    def write_line(self, str):
    	str += "\n"
        self.sock.send(str)

