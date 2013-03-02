#!/user/bin/env python


import sys
import Server
import Client


def start_server(port):
	server = Server.Server(port)


def start_client(port):
	client = Client.Client(port)


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print "Usage: start server|client port"
	action = sys.argv[1]
	port = sys.argv[2]
	if action == 'server':
		start_server(port)
	if action == 'client':
		start_client(port)
	else
		print "Unknown action"
