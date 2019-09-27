#!/usr/bin/python

import socket
import os
import sys
from colored import fg

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
    finally:
        s.close()

def checkVulns(banner, filename):
    f = open(filename, "r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("%s[-] Server is vulnerable: %s" % (fg(2), banner.strip("\n")))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('%s[-] File doesnt Exist!' % fg(1))
            exit(0)
        if not os.access(filename, os.R_OK):
            print('%s[-] Access Denied!' % fg(1))
            exit(0)
    else:
        print("%s[-] Usage: %s <vuln_filename>" % (fg(6), str(sys.argv[0])))
        exit(0)

    portList = [21,22,25,80,110,443,445]
    for x in range(1,20):
        ip = "192.168.1." + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            print ("%s[+] %s" % (fg(6), str(port)))
            if banner:
                print ("%s[+] %s / %s : %s" % (fg(6), ip, str(port), banner))
                checkVulns(banner, filename)

main()