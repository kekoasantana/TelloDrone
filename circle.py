#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time


host = ''
port = 3939
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nCircle\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:  
        with open('circle.txt', 'r') as fp:
            for line in fp:
                # if line.has
                msg = line[:-1]
                print("this is msg:",msg)
                msg = msg.encode(encoding="utf-8")
                sent = sock.sendto(msg, tello_address)
                time.sleep(6)
        
        sock.close()  
        break        
        
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
