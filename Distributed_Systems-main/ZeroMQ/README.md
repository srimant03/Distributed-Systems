# Low-Level Group Messaging Application
This part of the assignment involves creating a Low-Level Group Messaging Application using ZeroMQ. The application consists of 3 types of Nodes or files:-
1) A Messaging App Server 
2) A Group Server 
3) User 
 
`message_server.py`
Sets up the main messaging server. Maintains a list of groups by their unique identifier(IP ADDRESS : PORT). Provides the yser with a list of all available groups.

`group.py` 
Interacts with the user and the main server. Maintains a list of participants of the group by a UUID. Stores all messages sent in the group with appropriate timestamps

`user.py`
Performs the following operations; Joining/leaving groups, Request group lists from the server, Send Messages, Request all messages of a group.

## Running the Code

1) Run the 3 files in the following order; `message_server.py`, `group.py`, `user.py` on different VM Instances.  

2) `group.py` takes in the following arguments; IP Address of the VM Instance on which it is being run, Port no. & a group name.  
