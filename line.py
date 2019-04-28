#
# Flying a straight line with Tello EDU 
#
# Reads from text file line.txt
#

import threading 
import socket
import sys
import time

    
host = ''                                                       # local host
port = 3939                                                     # open port on my laptop
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # create socket

tello_address = ('192.168.10.1', 8889)                          # the IP and port of the drone

sock.bind(locaddr)                                              # binds socket to local address

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nStraight Line\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:  
 
        with open('line.txt', 'r') as fp:                       # opens file for reading
            for line in fp:                                     # for loop read through the lines
                msg = line[:-1]                                 # removes '\n' from each command
                print("this is msg:",msg)
                msg = msg.encode(encoding="utf-8")              # encodes message
                sent = sock.sendto(msg, tello_address)          # send message to drone
                time.sleep(5.5)                                 # delay between commands
        
        sock.close()                                            # close socket
        break        
        
    except KeyboardInterrupt:               
        print ('\n . . .\n')
        sock.close()
        break
