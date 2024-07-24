# buyer_client.py

import grpc
import market_pb2, market_pb2_grpc
from market_server import market_servicer_instance


def search_item(stub, item_name="", category=market_pb2.Category.ANY):
    request = market_pb2.SearchItemRequest(item_name=item_name, category=category)
    response = stub.SearchItem(request)
    return response.results

def buy_item(stub, item_id, quantity, buyer_address):
    #print("Buyer prints: ", item_id, quantity, buyer_address)
    request = market_pb2.BuyItemRequest(item_id=item_id, quantity=quantity, buyer_address=buyer_address)
    response = stub.BuyItem(request)
    return response.status


def add_to_wishlist(stub, item_id, buyer_address):
    request = market_pb2.AddToWishListRequest(item_id=item_id, buyer_address=buyer_address)
    response = stub.AddToWishList(request)
    return response.status

def rate_item(stub, item_id, rating, buyer_address):
    request = market_pb2.RateItemRequest(item_id=item_id, rating=rating, buyer_address=buyer_address)
    response = stub.RateItem(request)
    return response.status

# Implement other buyer functionalities (BuyItem, AddToWishList, RateItem) here

def notify_client(stub, item_details):
    request = market_pb2.NotifyClientRequest(item_details=item_details)
    response = stub.NotifyClient(request)
    print("Buyer prints: ", item_details)
    return response.status


def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = market_pb2_grpc.BuyerServiceStub(channel)

        # Search item example
        results = search_item(stub, item_name="laptop", category=market_pb2.Category.ELECTRONICS)
        print("Buyer prints:")
        for result in results:
            print(f"Item ID: {result.item_id}, Price: ${result.price}, Name: {result.name}, "
                  f"Category: {market_pb2.Category.Name(result.category)}, "
                  f"Description: {result.description}, Quantity Remaining: {result.quantity_remaining}, "
                  f"Rating: {result.rating} / 5 | Seller: {result.seller}")
            
        # Buy item example
        status = buy_item(stub, 1, 2, "120.13.188.178:50051")
        print(f"Buyer prints: {'SUCCESS' if status == market_pb2.BuyItemResponse.SUCCESS else 'FAIL'}")

        # Add to wishlist example
        status = add_to_wishlist(stub, 1, "120.13.188.178:50051")
        print(f"Buyer prints: {'SUCCESS' if status == market_pb2.AddToWishListResponse.SUCCESS else 'FAIL'}")

        # Rate item example
        status = rate_item(stub, 1, 4, "120.13.188.178:50051")
        print(f"Buyer prints: {'SUCCESS' if status == market_pb2.RateItemResponse.SUCCESS else 'FAIL'}")

        #notify the buyer about the wishlist item when updated by the seller using notify_buyers function with buyer printing details of updated items that are wishlist by them:
        


        # Notify client example
        '''item_details = market_pb2.ItemDetails(
            item_id=1,
            price=500,
            product_name="iPhone",
            category=market_pb2.Category.ELECTRONICS,
            description="This is iPhone 15",
            quantity=5,
            rating=4.3,
            seller="192.13.188.178:50051"
        )
        status = notify_client(stub, item_details)
        print(f"Buyer prints: {'SUCCESS' if status == market_pb2.NotifyClientResponse.SUCCESS else 'FAIL'}")'''

if __name__ == '__main__':
    main()
