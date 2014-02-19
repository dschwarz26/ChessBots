ChessBots
=========

This project intends to connect to the ICC server (clients available at www.chessclub.com) in order to automate some
tasks.

Currently main.py connects to the server, listens for game notifications, parses them, and sends me an SMS conditioned
on what it finds. I have deployed this code to Amazon EC2 and set a cron such that it connects once an hour to look
for game notifications.

The second undertaking will be to search for game histories, store them in a database, and create replays of them
on a board.

