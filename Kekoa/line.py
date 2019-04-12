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


print ('\r\n\r\nStraight Line\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:  
        msg = "commmand"
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
        time.sleep(3)
        print("1")
        msg = "takeoff"
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
        time.sleep(5)
        print("2")
        msg = "go 0 50 0 20"
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
        time.sleep(10)
        print("3")
        msg = "land"
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
        time.sleep(3)
        print("4")
        msg = "end"
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
        print("5")
        
        sock.close()  
        break        
        
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
