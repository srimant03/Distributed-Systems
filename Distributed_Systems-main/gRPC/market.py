import grpc
from concurrent import futures
import market_pb2_grpc
import market_pb2
import seller_pb2
import seller_pb2_grpc
import buyer_pb2
import buyer_pb2_grpc
import threading

class market(market_pb2_grpc.market):
    def __init__(self):
        self.sellers = {} #{uuid: ip_address}
        self.items = {} #{product_name: [category, price, quantity, seller_uuid, seller_address, description, rating]}
        self.wishlist = {} #{buyer_address: [product_name]}
    
    def notifySeller(self, ip_address,product_name,quantity, buyer_address):
        with grpc.insecure_channel(ip_address) as channel:
            stub = seller_pb2_grpc.sellerStub(channel)
            response = stub.ReceiveNotification(seller_pb2.ReceiveNotificationRequest(product_name=product_name, quantity=quantity, buyer_address=buyer_address))
            return 
        
    def notifyBuyer(self,product_name, category, quantity, price, rating, description, seller_address):
        #send notification to all buyers who have added the item to their wishlist
        for buyer in self.wishlist:
            if product_name in self.wishlist[buyer]:
                print("Sending Notification to: ", buyer)
                with grpc.insecure_channel(buyer) as channel:
                    stub = buyer_pb2_grpc.buyerStub(channel)
                    response = stub.ReceiveNotification_buyer(buyer_pb2.ReceiveNotificationRequest_buyer(product_name=product_name, category=category, price = price, quantity=quantity))
                    #response = stub.ReceiveNotification_buyer(buyer_pb2.ReceiveNotificationRequest_buyer(product_name=product_name, category=category, price=price,quantity=quantity, description=description, seller_address=seller_address,rating=rating))
        return

    def SayHello(self, request, context):
        return market_pb2.HelloReply(message="Hello, %s!" % request.name)

    def RegisterSeller(self, request, context):
        print("Seller join Request from", request.ip_address, "with uuid", request.uuid)
        if request.uuid in self.sellers:
            return market_pb2.RegisterSellerResponse(message="FAIL, Seller already registered")
        else:
            self.sellers[request.uuid] = request.ip_address
            return market_pb2.RegisterSellerResponse(message="SUCCESS, Seller registered")
    
    def SellItem(self, request, context):
        print("Sell Item Request from", request.seller_uuid)
        if request.seller_uuid not in self.sellers:
            return market_pb2.SellItemResponse(message="FAIL, Seller not registered")
        else:
            if request.product_name in self.items:
                return market_pb2.SellItemResponse(message="FAIL, Item already exists")
            else:
                self.items[request.product_name] = [request.category, request.price, request.quantity, request.seller_uuid, self.sellers[request.seller_uuid], request.description, 0]
                return market_pb2.SellItemResponse(message="SUCCESS, Item added")
    
    def UpdateItem(self, request, context):
        print("Update Item Request from", request.seller_uuid, "for", request.product_name)
        if request.product_name not in self.items:
            return market_pb2.UpdateItemResponse(message="FAIL, Item does not exist")
        else:
            self.items[request.product_name][2] = request.quantity
            self.items[request.product_name][1] = request.price
            X = threading.Thread(target=self.notifyBuyer, args=(request.product_name,self.items[request.product_name][0],request.quantity,request.price,self.items[request.product_name][6],self.items[request.product_name][5],self.items[request.product_name][3]))
            X.start()
            X.join()
            return market_pb2.UpdateItemResponse(message="SUCCESS, Item updated")
    
    def DeleteItem(self, request, context):
        print("Delete Item Request from", request.seller_uuid, "for", request.product_name)
        if request.product_name not in self.items:
            return market_pb2.DeleteItemResponse(message="FAIL, Item does not exist")
        else:
            del self.items[request.product_name]
            return market_pb2.DeleteItemResponse(message="SUCCESS, Item deleted")
    
    def DisplaySellerItems(self, request, context):
        print("Display Seller Items Request from", request.seller_uuid)
        seller_items = []
        for item in self.items:
            if self.items[item][3] == request.seller_uuid:
                seller_items.append(market_pb2.DisplaySellerItemsResponse.Item(product_name=item, category=self.items[item][0], quantity=self.items[item][2], price=self.items[item][1], description=self.items[item][5], seller_address=self.items[item][4], seller_uuid=self.items[item][3], rating=self.items[item][6]))
        return market_pb2.DisplaySellerItemsResponse(items=seller_items) 
    
    def SearchItem(self, request, context):
        print("Search Item Request for", request.product_name, "in category", request.category)
        if request.product_name == "":
            search_items = []
            for item in self.items:
                if request.category in self.items[item]:
                    search_items.append(market_pb2.SearchItemResponse.Item(product_name=item, category=self.items[item][0], quantity=self.items[item][2], price=self.items[item][1], description=self.items[item][5], seller_address=self.items[item][4], seller_uuid=self.items[item][3], rating=self.items[item][6]))
            return market_pb2.SearchItemResponse(items=search_items)
        else:
            search_items = []
            for item in self.items:
                if request.product_name in item:
                    search_items.append(market_pb2.SearchItemResponse.Item(product_name=item, category=self.items[item][0], quantity=self.items[item][2], price=self.items[item][1], description=self.items[item][5], seller_address=self.items[item][4], seller_uuid=self.items[item][3], rating=self.items[item][6]))
            return market_pb2.SearchItemResponse(items=search_items)
    
    def BuyItem(self, request, context):
        print("Buy Item Request for", request.product_name, "from", request.buyer_address, "for", request.quantity, "from seller", request.seller_address)
        if request.product_name not in self.items:
            return market_pb2.BuyItemResponse(message="FAIL, Item does not exist")
        else:
            for item in self.items:
                if request.product_name in item and request.seller_address in self.items[item]:
                    if self.items[item][2] < request.quantity:
                        return market_pb2.BuyItemResponse(message="FAIL, Insufficient quantity")
                    else:
                        self.items[item][2] -= request.quantity
                        x = threading.Thread(target=self.notifySeller, args=(self.items[item][4],request.product_name,request.quantity, request.buyer_address))
                        x.start()
                        x.join()
                        return market_pb2.BuyItemResponse(message="SUCCESS, Item bought")
            return market_pb2.BuyItemResponse(message="FAIL, Item not found")
    def AddToWishList(self, request, context):
        print("Add to Wishlist Request for", request.product_name, "from", request.buyer_address)
        for item in self.items:
            if request.product_name in item:
                if request.buyer_address in self.wishlist:
                    self.wishlist[request.buyer_address].append(request.product_name)
                else:
                    self.wishlist[request.buyer_address] = [request.product_name]
                return market_pb2.AddToWishListResponse(message="SUCCESS, Item added to wishlist")
        return market_pb2.AddToWishListResponse(message="FAIL, Item not found")
    
    def RateItem(self, request, context):
        print("Rate Item Request for", request.product_name, "with rating", request.rating)
        for item in self.items:
            if request.product_name in item:
                if self.items[item][6] == 0:
                    self.items[item][6] = request.rating
                else:
                    self.items[item][6] = (self.items[item][6] + request.rating)/2
                return market_pb2.RateItemResponse(message="SUCCESS, Item rated")
        return market_pb2.RateItemResponse(message="FAIL, Item not found")
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_marketServicer_to_server(market(), server)
    server.add_insecure_port("[::]:5050")
    server.start()
    print("Server started, listening on 5050")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
    

    



    
