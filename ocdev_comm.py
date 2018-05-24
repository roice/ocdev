import socket
import time

# IP address of multicast group
MCAST_IP = "224.1.1.1"
MCAST_PORT = 5005

def ocdev_comm(lock, data, len_daq, num_chs):
    sock = socket.socket(socket.AF_INET, # internet
                        socket.SOCK_DGRAM,
                        socket.IPPROTO_UDP) # UDP
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    while(True):
        lock.acquire()
        msg = ','.join(["%.4f" % data[i] for i in range(len_daq*num_chs)])
        msg = msg+','
        lock.release()
        #print msg
        sock.sendto(msg, (MCAST_IP, MCAST_PORT))
        time.sleep(0.05) # 50 ms
