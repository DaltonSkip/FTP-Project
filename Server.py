

import socket
import sys
import getpass
import re
import os
cwd = os.getcwd()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#local
#server_address = ('localhost', 10000)

#hotspot
    #server_address = ('172.20.10.3', 5000)

#ethernet
server_address = ('169.254.229.20', 5000)
#Above are default modes for server based on our different modes of testing

correctID= input("Please choose a correct userID")
correctPassword= input("Please choose a server password")
correctToken= correctID+correctPassword
#Had an issue with an if statement and two strings, so I combined them into one for comparison
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
#Socket is bound and begins listening for an inbound connection
while True:
    print('connection pending')
    connection, client_address = sock.accept()
    try:
        print('connection detected from:', client_address)
        passwordloop = 1
        while (passwordloop == 1):
            id = connection.recv(1024).decode()
            password = connection.recv(1024).decode()
            print(id + " " + password)
            token = id+password
        #This loop is used so that the client cannot access the functions if they dont enter the right info
            if (token == correctToken):
                connection.send('1'.encode())
                passwordloop = 0
                print('Passed')
            else:
                connection.send('0'.encode())
                print('Failed')
        command = ""
        while command != "quit":
            command = connection.recv(1024).decode()
           #the command comes in and is decrypted for use in the many if or elif statements

            if command =="get":
                print('User chose get')
                fname = connection.recv(1024).decode()
                try:
                    file = open((cwd + "\\" + fname), 'rb')
                    #Uses os library and the filename to open the file at a specified path
                    connection.send('File found'.encode())
                    i = 0
                    while data:
                        print("sending packet ["+str(i)+"]")
                        connection.send(data)
                        i += 1
                        data = file.read(1024)
                        #Loop send data in kilobyte chunks (Something is messing up in loop occasionally)
                    print("Successfully Sent")
                    file.close()
                    #after data is sent the file closes and we reiterate
                except FileNotFoundError:
                    connection.send("File not found".encode())



            elif command == "put":
                print('User chose put')
                #Not currently working
                #plan:
                #reverse the send and recieve parts of get to make put
            elif command == "mget":
                print('User chose mget')
                #Not yet implemented
                #plan:
                #while loop that checks length of an array of the requested files
                #inside is get, but instead of filename, its filename[i]
                #where i is the count
                #GET INPUTS BEFORE ENTERING LOOP
            elif command == "mput":
                print('User Chose mput')
                #Not yet implemented
                #plan:
                #while loop for an array of the multiple files to be acquired
                #inside loop is put but with filename set as an array[i] instead of a static string
                #
            elif command == "dir":
                print('User chose dir')
                #Contents of the folder where Spencer's Server is NEED TO FIX LATER
                #plan:
                #Use chkdir and os.getcwd to get full filepath and current objects in directory
                connection.send("Directory Contents:\ntest.jpg\ntest.txt".encode())
            if command == "quit":
                connection.send("Exiting program".encode())
                break
    finally:
        connection.close()
        sock.close()
#Closes server, both sock and connection just in case something messes up
