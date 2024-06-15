import zmq
import signal
import time
import sys
import threading

signal.signal(signal.SIGINT, signal.SIG_DFL)

context = zmq.Context()
socket_request = context.socket(zmq.REQ)
socket_request.connect("tcp://localhost:5555")  #replace localhost with external IP of VM Instance on which message_server is running

group_members = [] #stores uuid of the group members
messages = {} #{timestamp: (uuid, message)}

ip = sys.argv[1]
port = sys.argv[2]
ip_address = ip + ":" + port
group_name = sys.argv[3]

#based on the ip and port number creates a socket
socket_reply = context.socket(zmq.REP)
socket_reply.bind("tcp://*:" + port)

def join_request(group_id, ip_address):
    socket_request.send_multipart([b'JOIN', b'REQUEST', b'FROM', group_id.encode('utf-8'), ip_address.encode('utf-8')])
    message = socket_request.recv()
    print(f"Received: {message}")
    print(f"SUCCESS")

def user_join_request(uuid):
    group_members.append(uuid)

def user_leave_request(uuid):
    group_members.remove(uuid)

def process_request(request):
    if request[0] == b'JOIN':
        uuid = request[3].decode('utf-8')
        print(f'JOIN REQUEST FROM {uuid}')
        user_join_request(uuid)
        socket_reply.send(b'User joined successfully')
    elif request[0] == b'LEAVE':
        uuid = request[3].decode('utf-8')
        print(f'LEAVE REQUEST FROM {uuid}')
        user_leave_request(uuid)
        socket_reply.send(b'User left successfully')
    elif request[1] == b'SEND':
        uuid = request[3].decode('utf-8')
        message = request[4].decode('utf-8')
        print(f'MESSAGE SEND FROM {uuid} {message}')
        timestamp = time.strftime("%H:%M:%S", time.localtime()) #HH:MM:SS format
        messages[timestamp] = (uuid, message) #{timestamp: (uuid, message)}
        print(messages)
        socket_reply.send(b'Message sent successfully')
    elif request[1] == b'REQUEST':
        uuid = request[3].decode('utf-8')
        print(f'MESSAGE REQUEST FROM {uuid}')
        if request[4] == b'ALL':
            print(messages)
            socket_reply.send_multipart([b'Messages:', str(messages).encode('utf-8')])
        else:
            # display messages after a certain time
            timestamp = request[4].decode('utf-8')
            print(f"Messages after {timestamp}")
            new_messages = {}
            for key, value in messages.items():
                if key > timestamp:
                    new_messages[key] = value
            print(new_messages)
            socket_reply.send_multipart([b'Messages:', str(new_messages).encode('utf-8')])
    else:
        socket_reply.send(b'Invalid request')     
    time.sleep(1)

join_request(group_name, ip_address)

while True:
    message = socket_reply.recv_multipart()
    print(f"Received: {message}")
    req_thread = threading.Thread(target=process_request, args=(message,))
    req_thread.start()
    req_thread.join()
    time.sleep(1)


    



    
    
        
    




