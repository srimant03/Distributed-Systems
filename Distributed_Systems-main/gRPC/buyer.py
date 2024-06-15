import grpc
from concurrent import futures
import market_pb2_grpc
import market_pb2
import buyer_pb2
import buyer_pb2_grpc
import sys
import uuid
import threading

ip_address = sys.argv[1]
user_id = str(uuid.uuid4())

class buyer(buyer_pb2_grpc.buyer):
    def __init__(self):
        pass

    def ReceiveNotification_buyer(self, request, context):
        print("Received Notification")
        print("Product Name: ", request.product_name)
        print("Category: ", request.category)
        print("Quantity: ", request.quantity)
        print("Price: ", request.price)
        #print("Rating: ", request.rating)
        #print("Description: ", request.description)
        #print("Seller Address: ", request.seller_address)
        return buyer_pb2.ReceiveNotificationResponse_buyer(success=True)

def menu():
    with grpc.insecure_channel('localhost:5050') as channel: #replace localhost with the external ip address of the VM instance running the market server
        stub = market_pb2_grpc.marketStub(channel)
        while True:
            print("Choose an option")
            print("1. Search for an item")
            print("2. Buy an item")
            print("3. Add to Wishlist")
            print("4. Rate Item")
            print("5. Exit")
            option = int(input())
            if option == 1:
                print("Enter Product Name")
                product_name = input()
                print("Enter Product Category")
                product_category = input()
                response = stub.SearchItem(market_pb2.SearchItemRequest(product_name=product_name, category=product_category))
                for item in response.items:
                    print("Product Name: ", item.product_name)
                    print("Category: ", item.category)
                    print("Quantity: ", item.quantity)
                    print("Price: ", item.price)
                    print("Description: ", item.description)
                    print("Seller Address: ", item.seller_address)
                    print("Seller UUID: ", item.seller_uuid)
                    print("Rating: ", item.rating)
            elif option == 2:
                print("Enter Product Name")
                product_name = input()
                print("Enter Product Quantity")
                product_quantity = int(input())
                print("Enter Seller Address")
                seller_address = input()
                response = stub.BuyItem(market_pb2.BuyItemRequest(product_name=product_name, quantity=product_quantity, buyer_address=ip_address, seller_address=seller_address))
                print(response.message)
            elif option == 3:
                print("Enter Product Name")
                product_name = input()
                print("Enter Seller Address")
                seller_address = input()
                response = stub.AddToWishList(market_pb2.AddToWishListRequest(product_name=product_name, buyer_address=ip_address, seller_address=seller_address))
                print(response.message)
            elif option == 4:
                print("Enter Product Name")
                product_name = input()
                print("Enter Seller Address")
                seller_address = input()
                print("Enter Rating")
                rating = int(input())
                response = stub.RateItem(market_pb2.RateItemRequest(product_name=product_name, rating=rating, seller_address=seller_address))
                print(response.message)
            elif option == 5:
                break

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buyer_pb2_grpc.add_buyerServicer_to_server(buyer(), server)
    server.add_insecure_port('[::]:5052')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    thread = threading.Thread(target=serve)
    thread.start()
    menu()





        
    