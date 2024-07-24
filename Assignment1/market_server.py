# market_server.py
import grpc
from concurrent import futures
import market_pb2, market_pb2_grpc

class MarketServicer(market_pb2_grpc.SellerServiceServicer, market_pb2_grpc.BuyerServiceServicer):
    def __init__(self):
        self.seller_items = {}
        self.wishlists = {}

    def RegisterSeller(self, request, context):
        seller_address = request.ip_port
        seller_uuid = request.uuid

        if seller_address in self.seller_items:
            return market_pb2.RegisterSellerResponse(status=market_pb2.RegisterSellerResponse.FAILED)

        self.seller_items[seller_address] = []
        print(f"Market prints: Seller join request from {seller_address}, uuid = {seller_uuid}")
        return market_pb2.RegisterSellerResponse(status=market_pb2.RegisterSellerResponse.SUCCESS)

    def SellItem(self, request, context):
        seller_address = request.seller_address
        seller_uuid = request.seller_uuid

        if seller_address not in self.seller_items:
            return market_pb2.SellItemResponse(status=market_pb2.SellItemResponse.FAILED)

        item_id = len(self.seller_items[seller_address]) + 1
        self.seller_items[seller_address].append({
            'item_id': item_id,
            'product_name': request.product_name,
            'category': request.category,
            'quantity': request.quantity,
            'description': request.description,
            'price': request.price,
            'rating': 0.0
        })
        #print the seller_items
        #print(self.seller_items)
        print(f"Market prints: Sell Item request from {seller_address}")
        return market_pb2.SellItemResponse(status=market_pb2.SellItemResponse.SUCCESS, item_id=item_id)
    
    def DisplaySellerItems(self, request, context):
        seller_address = request.seller_address
        seller_uuid = request.seller_uuid

        if seller_address not in self.seller_items:
            return market_pb2.DisplaySellerItemsResponse(items=[])

        print(f"Market prints: Display Seller Items request from {seller_address}")
        #print(self.seller_items)
        return market_pb2.DisplaySellerItemsResponse(items=self.seller_items[seller_address])
    
    def UpdateItem(self, request, context):
        seller_address = request.seller_address
        seller_uuid = request.seller_uuid
        item_id = request.item_id
        new_price = request.new_price
        new_quantity = request.new_quantity

        if seller_address not in self.seller_items:
            return market_pb2.UpdateItemResponse(status=market_pb2.UpdateItemResponse.FAILED)

        seller_items = self.seller_items[seller_address]
        updated_item = None

        for item in seller_items:
            if item['item_id'] == item_id:
                item['price'] = new_price
                item['quantity'] = new_quantity
                updated_item = item
                break

        if updated_item is None:
            return market_pb2.UpdateItemResponse(status=market_pb2.UpdateItemResponse.FAILED)

        print(f"Market prints: Update Item request from {seller_address}")
        #print(self.seller_items)
        # Notify buyers who wish-listed the updated product
        #self.notify_buyers(item_id,updated_item)--> Not Working !!
        #check if buyer_address is in wishlist for the updated item:
        return market_pb2.UpdateItemResponse(status=market_pb2.UpdateItemResponse.SUCCESS)

    # Add the notify_buyers method to handle notifications
    def notify_buyers(self, item_id,item_details):
        for buyer_address, items in self.wishlists.items():
            if item_id in items:
                print(f"Market prints: Notifying {buyer_address} about the updated item {item_id}")
                buyer_stub = market_pb2_grpc.BuyerServiceStub(grpc.insecure_channel(buyer_address))
                notify_request = market_pb2.NotifyClientRequest(item_details=item_details)
                buyer_stub.NotifyClient(notify_request)
                #notify_client(buyer_stub, item_details)
                #send the item_details to the buyer:
                #notify_client(stub, item_details)


    def DeleteItem(self, request, context):
        seller_address = request.seller_address
        seller_uuid = request.seller_uuid
        item_id = request.item_id

        if seller_address not in self.seller_items:
            return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.FAILED)

        seller_items = self.seller_items[seller_address]
        deleted_item = None

        for index, item in enumerate(seller_items):
            if item['item_id'] == item_id:
                deleted_item = seller_items.pop(index)
                break

        if deleted_item is None:
            return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.FAILED)

        print(f"Market prints: Delete Item {item_id} request from {seller_address}")

        return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.SUCCESS)

    # Implement other seller functionalities (UpdateItem, DeleteItem, DisplaySellerItems) here

    # Buyer functionalities
    def SearchItem(self, request, context):
        #print(self.seller_items)
        item_name = request.item_name
        category = request.category

        results = []
        print(f"Market prints: Search Item request for {item_name}, category: {market_pb2.Category.Name(category)}")
        #print the seller_items
        for seller_address, items in self.seller_items.items():
            for item in items:
                #print(f"Checking item: {item}")
                #print(f"Item name condition: {not item_name or item_name in item['product_name']}")
                #print(f"Category condition: {category == market_pb2.Category.ANY or category == item['category']}")
                if(not item_name or item_name in item['product_name']) and (category == market_pb2.Category.ANY or category == item['category']):
                    results.append(market_pb2.SearchItemResponse.SearchResult(
                        item_id=item['item_id'],
                        price=item['price'],
                        name=item['product_name'],
                        category=item['category'],
                        description=item['description'],
                        quantity_remaining=item['quantity'],
                        rating=item['rating'],
                        seller=seller_address
                    ))

        print(f"Market prints: Search Item request for {item_name}, category: {market_pb2.Category.Name(category)}")
        print(f"Market prints: Found {len(results)} items matching the criteria.")
        print(f"Market prints: Items in results: {results}")
        print(f"Market prints: Search Item request for {item_name}, category: {market_pb2.Category.Name(category)}")
        return market_pb2.SearchItemResponse(results=results)
    
    def BuyItem(self, request, context):
        print("Buy request received")
        buyer_address = request.buyer_address
        item_id = request.item_id
        quantity = request.quantity

        #Below command to be added if Sir says that buyer should also be registered first like the seller
        '''if buyer_address not in self.seller_items:
            return market_pb2.BuyItemResponse(status=market_pb2.BuyItemResponse.FAILED)'''
        
        print(f"Market prints: Buy request {quantity} of item {item_id}, from {buyer_address}")
        for seller_address, items in self.seller_items.items():
            for item in items:
                if item['item_id'] == item_id:
                    if item['quantity'] >= quantity:
                        item['quantity'] -= quantity
                        print(f"Market prints: Buy request {quantity} of item {item_id}, from {buyer_address}")
                        # Notify the seller of the transaction---> to be checked
                        #self.notify_seller(item_id, quantity, buyer_address)
                        return market_pb2.BuyItemResponse(status=market_pb2.BuyItemResponse.SUCCESS)
                    else:
                        return market_pb2.BuyItemResponse(status=market_pb2.BuyItemResponse.FAILED)

        return market_pb2.BuyItemResponse(status=market_pb2.BuyItemResponse.FAILED)
    
    def AddToWishList(self, request, context):
        buyer_address = request.buyer_address
        item_id = request.item_id

        if buyer_address not in self.wishlists:
            self.wishlists[buyer_address] = set()

        self.wishlists[buyer_address].add(item_id)
        print(f"Market prints: Wishlist request of item {item_id}, from {buyer_address}")
        return market_pb2.AddToWishListResponse(status=market_pb2.AddToWishListResponse.SUCCESS)
    
    def RateItem(self, request, context):
        buyer_address = request.buyer_address
        item_id = request.item_id
        rating = request.rating

        # Assuming that each item has a 'rating' field
        for seller_address, items in self.seller_items.items():
            for item in items:
                if item['item_id'] == item_id:
                    #simply updating the rating of the item
                    item['rating'] = rating
                    #printing format should be: 120.13.188.178:50051 rated item 3[item id] with 4 stars:
                    print(f"Market prints: {buyer_address} rated item {item_id} with {rating} stars")
                    return market_pb2.RateItemResponse(status=market_pb2.RateItemResponse.SUCCESS)

        return market_pb2.RateItemResponse(status=market_pb2.RateItemResponse.FAIL)


    # Implement other buyer functionalities (BuyItem, AddToWishList, RateItem) 
    
    def NotifyClient(self, request, context):
        item_details = request.item_details

        print("#######")
        print("The Following Item has been updated:")
        print(f"Item ID: {item_details.item_id}, Price: ${item_details.price}, Name: {item_details.product_name}, "
              f"Category: {market_pb2.Category.Name(item_details.category)}, Description: {item_details.description}, "
              f"Quantity Remaining: {item_details.quantity}, Rating: {item_details.rating} / 5 | Seller: {item_details.seller}")
        print("#######")

        return market_pb2.NotifyClientResponse(status=market_pb2.NotifyClientResponse.SUCCESS)

# Create a global instance of MarketServicer
market_servicer_instance = MarketServicer()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_SellerServiceServicer_to_server(market_servicer_instance, server)
    market_pb2_grpc.add_BuyerServiceServicer_to_server(market_servicer_instance, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Market server is running on port 50051.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
