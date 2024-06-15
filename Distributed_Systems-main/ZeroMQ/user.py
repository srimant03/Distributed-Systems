import zmq
import signal
import time
import socket
import sys
import uuid

signal.signal(signal.SIGINT, signal.SIG_DFL)

context = zmq.Context()
socket1 = context.socket(zmq.REQ)
socket1.connect("tcp://localhost:5555") #replace localhost with external IP of VM Instance on which message_server is running

groups = {} # {group_name: [(ip_address, socket_number)]}
sockets = []

#uuid of the user
uu = str(uuid.uuid1())

def see_all_groups():
    socket1.send_multipart([b'GROUP', b'LIST', b'REQUEST', b'FROM', uu.encode('utf-8')])
    message = socket1.recv_multipart()
    print(f"Available Groups:")
    group_list = message[1].decode('utf-8')
    group_list = group_list.replace("{", "")
    group_list = group_list.replace("}", "")
    group_list = group_list.replace("'", "")
    group_list = group_list.split(", ")
    for i in range(len(group_list)):
        print(f"{i+1}) {group_list[i]}")
        print("\n")

def join_group(group_name, ip_address):
    try:
        socket = context.socket(zmq.REQ)
        socket.connect(f"tcp://{ip_address}")
    except:
        print(f"ERROR: Invalid IP Address")
        return
    sockets.append(socket)
    if group_name not in groups:
        groups[group_name] = (ip_address, socket)
    else:
        print(f"Group {group_name} already exists")
    try:    
        socket.send_multipart([b'JOIN', b'REQUEST', b'FROM', uu.encode('utf-8')])
    except:
        print(f"ERROR: Invalid Join Request")
        return
    message = socket.recv()
    print(f"Received: {message}")
    print(f"SUCCESS")

def leave_group(group_name):
    if group_name not in groups:
        print(f"ERROR: Group {group_name} does not exist")
        return
    socket = groups[group_name][1] #get the socket corresponding to said group from the dictionary
    socket.send_multipart([b'LEAVE', b'REQUEST', b'FROM', uu.encode('utf-8')])
    message = socket.recv()
    print(f"Received: {message}")
    print(f"SUCCESS")
    # remove the socket from the dictionary
    del groups[group_name]
    socket.close()  

def send_message(group_name):
    if group_name not in groups:
        print(f"ERROR: Group {group_name} does not exist")
        return
    msg = input("Enter the message: ")
    socket = groups[group_name][1]
    socket.send_multipart([b'MESSAGE', b'SEND', b'FROM', uu.encode('utf-8'), msg.encode('utf-8')])
    message = socket.recv()
    print(f"Received: {message}")
    print(f"SUCCESS")

def display_messages(group_name):
    if group_name not in groups:
        print(f"ERROR: Group {group_name} does not exist")
        return
    print("1) Display all messages")
    print("2) Display messages after ..")
    choice = input("Enter your choice: ")
    if choice == "1":
        socket = groups[group_name][1]
        socket.send_multipart([b'MESSAGE', b'REQUEST', b'FROM', uu.encode('utf-8'), b'ALL'])
    elif choice == "2":
        date = input("Enter the time (in HH:MM:SS format): ")
        socket = groups[group_name][1]
        socket.send_multipart([b'MESSAGE', b'REQUEST', b'FROM', uu.encode('utf-8'), date.encode('utf-8')])
    msg = socket.recv_multipart()
    print("Groupe Messages:")
    message = msg[1].decode('utf-8')
    print(message)

while True:
    print("1. Show all available groups")
    print("2. Join a group")
    print("3. Leave a group")
    print("4. Send a message")
    print("5. Display messages")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        see_all_groups()
    elif choice == "2":
        group_name = input("Enter the group name: ")
        ip_address = input("Enter the ip address: ")
        join_group(group_name, ip_address)
    elif choice == "3":
        group_name = input("Enter the group name: ")
        leave_group(group_name)
    elif choice == "4":
        group_name = input("Enter the group name: ")
        send_message(group_name)
    elif choice == "5":
        group_name = input("Enter the group name: ")
        display_messages(group_name)
    elif choice == "6":
        break
    else:
        print("Invalid choice")



        
    


        


    


