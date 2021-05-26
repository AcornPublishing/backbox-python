
#cat > scan.py

#Python 2.7
#-*-coding:utf-8 -*-
import nmap

nm = nmap.PortScanner()
host = "127.0.0.1"
nm.scan(host, "22-23")
#nm.scan(host, "22-23", arguments="-sT -sV")

for host in nm.all_hosts():
	print "Host: %s (%s)" %(host, nm[host].hostname())
	print "State: %s" %nm[host].state()

for proto in nm[host].all_protocols():
	print "Protocol: %s" %proto

lport = nm[host]["tcp"].keys()
lport.sort()

for port in lport:
	print "port: %s state: %s" %(port, nm[host][proto][port]["state"])

#python scan.py
