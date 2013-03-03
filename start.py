#!/user/bin/env python


import random
import sys
import Server
import Client


def start_server(port):
	server = Server.Server(port)
	print "Starting server. Listening on port " + str(port) + "."
	server.serve()
	print "Stopped server."
	del server


def start_client(host, port):
	print "Starting client. Connecting to " + str(host) + ":" + str(port) + "."
	client = Client.Client(host, port)
	print "Stopped client."
	del client


def print_usage():
	print "Usage: start server port"
	print "       start client host port"


if __name__ == '__main__':
	if len(sys.argv) < 2:
		action = "usage"
	elif sys.argv[1] == "server":
		action = "server"
	elif sys.argv[1] == "client":
		action = "client"
	else:
		print "Unknown action `" + sys.argv[1] + "'."
		action = "usage"

	if action == "server":
		if len(sys.argv) < 3:
			print "No port given"
			action = "usage"
		else:
			port = int(sys.argv[2])
			start_server(port)
	elif action == "client":
		if len(sys.argv) < 4:
			print "No host or port given"
			action = "usage"
		else:
			host = sys.argv[2]
			port = int(sys.argv[3])
			start_client(host, port)
	if action == "usage":
		print_usage()
