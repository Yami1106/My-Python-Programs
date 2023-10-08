import socket 
ip = "127.0.0.1"
port = 1234
server = socket.socket()
server.bind((ip,port))
server.listen(5)
client,address = server.accept()
print("Got connection from",client)
string = client.recv(1024)
string = string.decode("utf-8")
print("Data received from the client ",string)
string = string.upper()
print("Sending data back to the client ",string)
client.send(bytes(string, "utf-8"))
client.close()