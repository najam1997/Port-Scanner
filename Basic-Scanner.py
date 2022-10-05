import optparse
from socket import *
from threading import *

scrn_lock = Semaphore(value=1)
def Scan(Host_IP, Port):
 try:
  connect_socket = socket(AF_INET, SOCK_STREAM)
  connect_socket.connect((Host_IP, Port))
  scrn_lock.acquire()
  print ('Port %d is open'% Port)
  
 except:
  scrn_lock.acquire()
  print ('Port %d is closed'% int(Port))
 
 finally:
  scrn_lock.release()
  connect_socket.close()

def portScan(Host, Ports):
 try:
  IP = gethostbyname(Host)
 except:
  print ("Unable to resolve host '%s'" %Host)
  return
 try:
  Name = gethostbyaddr(IP)
  print ('\nResults for the scan of Host: ' + Name[0])
 except:
  print ('\nResults for the scan of IP: ' + Host)
 setdefaulttimeout(1)
 
 for Port in Ports:
  print(Port)
  thread1 = Thread(target = Scan, args = (Host, int(Port)))  
  thread1.start()
  #print ("Scanning port " + Port)
  #Scan(Host, int(Port))

def main():
 psr = optparse.OptionParser()
 psr.add_option('-u', dest='Host_IP', type='string')
 psr.add_option('-p', dest='Port', type='string')
 (options, args) = psr.parse_args()
 Host_IP = options.Host_IP
 Ports = str(options.Port).split(',')
 if (Host_IP == None) | (Ports[0] == None):
  print ('No port specified')
  exit(0)
 portScan(Host_IP, Ports)
 
if __name__ == '__main__':
 main() 
