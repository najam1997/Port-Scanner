import optparse
from socket import *

def Scan(Host_IP, Port):
 try:
  connect_socket = socket(AF_INET, SOCK_STREAM)
  connect_socket.connect((Host_IP, Port))
  print ('Port %d is open'% Port)
  connect_socket.close()
 except:
  print ('Port %d is closed'% Port)

def portScan(Host, Ports):
 try:
  IP = gethostbyname(Host)
 except:
  print ("Unable to resolve host '%s'" %Host)
  return
 try:
  Name = gethostbyaddr(IP)
  print ('\n Results for the scan of Host: ' + Name[0])
 except:
  print ('\n Results for the scan of IP: ' + tgtIP)
 setdefaulttimeout(1)
 for Port in Ports:
  print ('Scanning port ' + Port)

Scan("10.10.11.180", int(90))
