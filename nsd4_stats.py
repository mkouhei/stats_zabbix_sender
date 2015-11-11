#!/usr/bin/python
# coding: utf-8

import os
import subprocess
import time
import socket


if __name__ == "__main__":

	unixtime = time.time()
	prog_stats = "/usr/local/sbin/nsd-control stats"
	sender = "/usr/local/bin/zabbix_sender"
	hostname = socket.getfqdn()
	server = "10.0.0.1"
	ofile = "/tmp/nsd.txt"

	test = subprocess.check_output(prog_stats.split(" "))
	test2 = test.split("\n")
	f = open(ofile, 'w')
	for i in range(0, len(test2)-1):
		list = test2[i].split("=")
		args = hostname + " " + list[0] + " " + str(unixtime) + " " + list[1] + "\n"
		f.write(args)
	f.close()


	cmd = sender + " -z " + server + " -T " + " -i " + ofile
	subprocess.call(cmd.split(" "))
	os.remove(ofile)
