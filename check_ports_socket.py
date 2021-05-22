import socket
import sys
import faker

def checkPortsSocket(ip,portlist):
    #print("IP",ip,type(ip)) #str
    try:
        for port in portlist:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)#tecnología, protocolo
            sock.settimeout(5)
            result = sock.connect_ex((ip,port)) #
            if result == 0:
                print ("Port {}: \t Open".format(port))
            else:
                print ("Port {}: \t Close".format(port))
            sock.close()
    except socket.error as error:
        print (str(error))
        print ("Error conecting")
        sys.exit()


