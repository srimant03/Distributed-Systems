import grpc
from concurrent import futures
import market_pb2_grpc
import market_pb2
import seller_pb2
import seller_pb2_grpc
import sys
import uuid
import threading

ip_address = sys.argv[1]
user_id = str(uuid.uuid4())
print(user_id)
print(ip_address)

class seller(seller_pb2_grpc.seller):
    def __init__(self):
        pass

    def ReceiveNotification(self, request, context):
        print("Received Notification")
        print("Product Name: ", request.product_name)
        print("Quantity: ", request.quantity)
        print("Buyer Address: ", request.buyer_address)
        return seller_pb2.ReceiveNotificationResponse(success=True)

def menu():
    with grpc.insecure_channel('localhost:5050') as channel:  #replace localhost with the external ip address of the VM instance running the market server
        stub = market_pb2_grpc.marketStub(channel)
        response = stub.SayHello(market_pb2.HelloRequest(name='you'))
        print(response.message)
        response = stub.SayHello(market_pb2.HelloRequest(name='you'))
        print(response.message)
        response = stub.RegisterSeller(market_pb2.RegisterSellerRequest(ip_address=ip_address, uuid=user_id))
        print(response.message)
        while True:
            print("Choose an option")
            print("1. Sell an item")
            print("2. Update an item")
            print("3. Delete an item")
            print("4. Display all items")
            print("5. Exit")
            option = int(input())
            if option == 1:
                print("Enter Product Name")
                product_name = input()
                print("Enter Product Category")
                product_category = input()
                print("Enter Product Price")
                product_price = float(input())
                print("Enter Product Quantity")
                product_quantity = int(input())
                print("Enter Product Description")
                product_description = input()
                response = stub.SellItem(market_pb2.SellItemRequest(product_name=product_name, category=product_category, quantity=product_quantity, price=product_price,description=product_description, seller_address=ip_address, seller_uuid=user_id))
                print(response.message)
            elif option == 2:
                print("Enter Product Name")
                product_name = input()
                print("Enter Price")
                product_price = float(input())
                print("Enter Quantity")
                product_quantity = int(input())
                response = stub.UpdateItem(market_pb2.UpdateItemRequest(product_name=product_name, price=product_price, quantity=product_quantity, seller_address=ip_address, seller_uuid=user_id))
                print(response.message)
            elif option == 3:
                print("Enter Product Name")
                product_name = input()
                response = stub.DeleteItem(market_pb2.DeleteItemRequest(product_name=product_name, seller_address=ip_address, seller_uuid=user_id))
                print(response.message)
            elif option == 4:
                response = stub.DisplaySellerItems(market_pb2.DisplaySellerItemsRequest(seller_uuid=user_id))
                for item in response.items:
                    print("Product Name: ", item.product_name)
                    print("Category: ", item.category)
                    print("Quantity: ", item.quantity)
                    print("Price: ", item.price)
                    print("Description: ", item.description)
                    print("Seller Address: ", item.seller_address)
                    print("Seller UUID: ", item.seller_uuid)
                    print("Rating: ", item.rating)
                    print("\n")
            elif option == 5:
                break

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    seller_pb2_grpc.add_sellerServicer_to_server(seller(), server)
    server.add_insecure_port('[::]:5051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    thread = threading.Thread(target=serve)
    thread.start()
    menu()

