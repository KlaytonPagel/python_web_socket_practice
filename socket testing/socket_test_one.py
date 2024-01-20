import socket

# AF_INET refers to the ipv4 address family
# SOCK_STREAM means connection oriented TCP
web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# resolve an IP from a domain name
host_ip = socket.gethostbyname('kowantify.com')

# define a port
port = 80

# connect to the IP on the port
web_socket.connect((host_ip, port))
