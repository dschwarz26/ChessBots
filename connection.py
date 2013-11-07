# Template from Ryan Chiu. See https://code.google.com/p/ics-bot-maker/

import socket

class Connection:

    # Pretty self-explanatory - simply connects to the ICS,
    # enter username/password combo precisely when prompted
    def connect(self):
        self.sock.connect((self.server_host, self.server_port))

        # Print data until server prompts for a username, in which case it
        # will be entered.
        self.read_until('login: ')
        self.connecting = True
        self.write_line(self.username)

        # Ditto for the password
        self.read_until('password: ')
        self.write_line(self.password)

        #self.read_until(self.username)
        self.connecting = False
        self.connected = True
        
        while self.connected:
            self.read_line()

    def __init__(self, server_host, server_port, server_prompt,
                 username, password, buffer_size):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.buffer_size = buffer_size        
        self.server_host = server_host
        self.server_port = server_port
        self.server_prompt = server_prompt
        self.username = username
        self.password = password

        # Some status booleans for ease of error handling
        self.connected = False
        self.connecting = False

    def read_line(self):
        recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
        print recv

    def read_until(self, end_str):
        recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
        while end_str not in str(recv):
            print recv

    def write_line(self, str):
        str += "\n"
        self.sock.send(str)

    # Some getter/setter methods that I thought might be necessary
    def get_server_host(self): return self.server_host
    def get_server_prompt(self): return self.server_prompt
    def get_server_port(self): return self.server_port

    def is_connected(self): return self.connected
    def is_connecting(self): return self.connecting
    
    def set_server_host(self, host): self.server_host = host
    def set_server_prompt(self, prompt): self.server_prompt = prompt
    def set_server_port(self, port): self.server_port = port
