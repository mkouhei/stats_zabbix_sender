#!/usr/bin/python
# coding: utf-8

import time
import subprocess
import socket
import os


if __name__ == "__main__":

	unixtime = time.time()
	prog_stat = "/usr/local/sbin/unbound-control stats"
	sender = "/usr/local/bin/zabbix_sender"
	server = "10.0.0.1"
	hostname = socket.getfqdn()
	ofile = "/tmp/unbound.txt"

	test = subprocess.check_output(prog_stat.split(" "))
	test2 = test.split("\n")
	f = open(ofile, 'w')
	for i in range(0, len(test2)-1):
		list2 = test2[i].split("=")
		args = hostname + ' ' + list2[0] +' ' + str(unixtime) + ' ' + list2[1] +'\n'
		f.write(args)
	f.close()


	cmd = sender + " -z " + server + " -T " + " -i " + ofile
	subprocess.call(cmd.split(" "))
	os.remove(ofile)
