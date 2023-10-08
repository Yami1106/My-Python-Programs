#TCP Client
import socket
ip = "127.0.0.1"
port = 1234
server = socket.socket()
server.connect((ip,port))
string = input("Enter String: ")
server.send(bytes(string, "utf-8"))
print("Data has been sent to the server... ")
print("Data received from the server")
string = server.recv(1024)
string = string.decode("utf-8")
print(string)
server.close()
