# ONLINE SHOPPING PLATFORM USING gRPC

## Steps to run the application
Commands to compile the proto files
```
$ python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. market.proto
$ python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. buyer.proto
$ python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. seller.proto
```

After compiling the proto files for market, buyer & seller; and generating the relevant files the application can be run from seperate VM instances in the following order:-
```
$ python3 market.py
$ python3 seller.py [IP:PORT]
$ python3 buyer.py [IP:PORT]
```
[IP:PORT] is the external ip addresses of the VM instances along with the chosen port number i.e 5050 for market, 5051 for seller & 5052 for buyer.


