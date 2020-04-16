
import socket
import sys
import getpass
import os 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect the socket to the port where the server is listening
ip = input('Please input the ip you want to connect to(169.254.229.20 for ethernet)')
server_address = (ip, 5000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
passwordconfirmed = 0
#connects to the ip the user chooses, with a default port listed. Password hasnt been confirmed so the client has to wait
while (passwordconfirmed==0):
    id =(input("id: "))
    password = getpass.getpass(prompt = "password: ")
    sock.send(id.encode())
    sock.send(password.encode())
    #gets id and password and sends them encoded to the server for authentication
    passwordconfirmed = sock.recv(1024).decode()
    print(passwordconfirmed)
    #loop continues until the server sets passwordconfirmed to 1
try:
    
    # pulls up default menu for user that shows all standard options
    
    message = input("please issue a server command (get, put, mget, mput, dir, quit)")
    print('sending {!r}'.format(message))
    sock.send(message.encode())
    #the users choice is encoded and sent to the server for processing as a command

    if message == "get":
        fname = input("What file do you want")
        sock.send(fname.encode())
        message = sock.recv(1024).decode()
        #Chooses the file the client wants to recieve, and sends that to the server to be procecssed

        file = open(fname, 'wb')
        #A blank file of the same type and name is opened on the client and the data will stream in soon

        while data:
            print("Recieving")
            file.write(data)
            data = sock.recv(1024)
        print ("Transfer Complete")    
        file.close()
        #after all data is recieved, the loop exits and the file is closed.
    if message == "dir":
        data = sock.recv(1024).decode()
        print(data)
            


    sock.close
    sock = socket.socket()
    sock.connect(server_address)
    #reconnects to the socket in case of an error
   

finally:
    print('closing socket')
    sock.close()
    #officially closes the socket for good
