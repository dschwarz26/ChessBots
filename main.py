# Template from Ryan Chiu.  See https://code.google.com/p/ics-bot-maker/

import Connection

# Will open password.txt on the local directory (contains the password) and
# returns the value. This makes it more secure and easy when sharing this code
# with others.
def get_password_from_file():
    password_file = open('password.txt', 'r')
    password = password_file.readline()
    return password

# Important configuration variables for bot. Change these to fit
# your bot's user information
LOGIN_CONFIG = {"server_host": "freechess.org",
                "server_port": 5000,
                "server_prompt": "fics%",
                "username": "foo",
                "password": get_password_from_file(),
                "buffer_size": 4096}

# Set up connection using LOGIN_CONFIG dictionary values
connection = Connection.Connection(LOGIN_CONFIG["server_host"],
                                   LOGIN_CONFIG["server_port"],
                                   LOGIN_CONFIG["server_prompt"],
                                   LOGIN_CONFIG["username"],
                                   LOGIN_CONFIG["password"],
                                   LOGIN_CONFIG["buffer_size"])
connection.connect()


