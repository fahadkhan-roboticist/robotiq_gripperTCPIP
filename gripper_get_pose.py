import socket 

HOST = "192.168.0.50"    # The remote host 
PORT = 30002              # The same port as used by the server 
PORTG = 63352
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.connect((HOST, PORTG))
s.sendall(b'GET POS\n')
data = s.recv(2**10)

print('Gripper finger position is: ', data)

s.close()
