#ServerChat.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",8558))
s.listen(2)
while(True):
	cs,ca=s.accept()
	csdata=cs.recv(1024).decode()
	print("Student-->{}".format(csdata))
	sdata=input("KVR-->")
	cs.send(sdata.encode())
