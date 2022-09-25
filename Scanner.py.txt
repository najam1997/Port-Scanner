import pyfiglet
import sys
import socket

banner = pyfiglet.figlet_format("SCANNER")
print(banner)

target = str(0)

if len(sys.argv) == 3:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Argument(less)")

# Add Banner
print("\n")
print("Scanning Target: " + target)
print("\n")

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	port = int(sys.argv[2])
	result = s.connect_ex((target,port))
	if result == 0:
		print ('[+] %d/tcp open'% port)
	s.close()
		
except KeyboardInterrupt:
		print("\n Ctrl - C(ed)")
		sys.exit()
except socket.gaierror:
		print("\n Unable to resolve host")
		sys.exit()
except socket.error:
		print("\ Server Down")
		sys.exit()
