import zmq
import signal
import time

signal.signal(signal.SIGINT, signal.SIG_DFL)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

groups = {} # dictionary to store the groups with ip addresses/uuid

def register_group(group_id, ip_address):
    if group_id not in groups:
        groups[group_id] = [ip_address]
    else:
        groups[group_id].append(ip_address)

def getGroupList():
    return groups

while True:
    message = socket.recv_multipart()
    print(f"Received: {message}")
    if message[0] == b'JOIN':
        group_id = message[3].decode('utf-8')
        ip_address = message[4].decode('utf-8')
        print(f'JOIN REQUEST FROM {group_id} {ip_address}')
        register_group(group_id, ip_address)
        socket.send(b'Group registered successfully')
    elif message[0] == b'GROUP':
        group_list = getGroupList()
        print(f'GROUP LIST REQUEST FROM {message[3].decode("utf-8")}')
        socket.send_multipart([b'Group list:', str(group_list).encode('utf-8')])
    else:
        socket.send(b'Invalid request')
    time.sleep(1)
