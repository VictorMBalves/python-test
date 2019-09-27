#!/usr/bin/python

import socket
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

def main():
    ip = raw_input("[*] Enter target IP:")
    for x in range(1,100):
        banner = retBanner(ip, x)
        print ("%s[+] %s" % (fg(6), str(x)))
        if banner:
            print ("%s[+] %s / %s : %s" % (fg(6), ip, str(x), banner))

main()