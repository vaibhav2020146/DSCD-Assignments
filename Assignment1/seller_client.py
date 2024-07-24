# seller_client.py

import grpc
import market_pb2, market_pb2_grpc
from market_server import market_servicer_instance

def register_seller(stub, ip_port, uuid):
    request = market_pb2.RegisterSellerRequest(ip_port=ip_port, uuid=uuid)
    response = stub.RegisterSeller(request)
    return response.status

def sell_item(stub, product_name, category, quantity, description, seller_address, seller_uuid, price):
    request = market_pb2.SellItemRequest(
        product_name=product_name,
        category=market_pb2.Category.Value(category),
        quantity=quantity,
        description=description,
        seller_address=seller_address,
        seller_uuid=seller_uuid,
        price=price
    )
    response = stub.SellItem(request)
    return response.status, response.item_id

def display_seller_items(stub, seller_address, seller_uuid):
    request = market_pb2.DisplaySellerItemsRequest(seller_address=seller_address, seller_uuid=seller_uuid)
    response = stub.DisplaySellerItems(request)
    return response.items

def update_item(stub, item_id, new_price, new_quantity, seller_address, seller_uuid):
    request = market_pb2.UpdateItemRequest(
        item_id=item_id,
        new_price=new_price,
        new_quantity=new_quantity,
        seller_address=seller_address,
        seller_uuid=seller_uuid
    )
    response = stub.UpdateItem(request)
    return response.status

def delete_item(stub, item_id, seller_address, seller_uuid):
    request = market_pb2.DeleteItemRequest(
        item_id=item_id,
        seller_address=seller_address,
        seller_uuid=seller_uuid
    )
    response = stub.DeleteItem(request)
    return response.status

# Implement other seller functionalities (UpdateItem, DeleteItem, DisplaySellerItems) here

def notify_client(stub, item_details):
    request = market_pb2.NotifyClientRequest(item_details=item_details)
    response = stub.NotifyClient(request)
    return response.status


def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = market_pb2_grpc.SellerServiceStub(channel)

        # Seller registration example
        status = register_seller(stub, "192.13.188.178:50051", "987a515c-a6e5-11ed-906b-76aef1e817c5")
        print(f"Seller prints: {'SUCCESS' if status == market_pb2.RegisterSellerResponse.SUCCESS else 'FAIL'}")

        # Sell item example
        status, item_id = sell_item(stub, "iPhone", "ELECTRONICS", 5, "This is iPhone 15",
                                     "192.13.188.178:50051", "987a515c-a6e5-11ed-906b-76aef1e817c5", 500)
        print(f"Seller prints: {'SUCCESS' if status == market_pb2.SellItemResponse.SUCCESS else 'FAIL'} "
              f"{'Item ID: ' + str(item_id) if status == market_pb2.SellItemResponse.SUCCESS else ''}")
        
        status, item_id = sell_item(stub, "laptop", "ELECTRONICS", 5, "This is HP Laptop",
                                     "192.13.188.178:50051", "987a515c-a6e5-11ed-906b-76aef1e817c5", 500)
        print(f"Seller prints: {'SUCCESS' if status == market_pb2.SellItemResponse.SUCCESS else 'FAIL'} "
              f"{'Item ID: ' + str(item_id) if status == market_pb2.SellItemResponse.SUCCESS else ''}")
        
        # Display seller items example
        items = display_seller_items(stub, "192.13.188.178:50051", "987a515c-a6e5-11ed-906b-76aef1e817c5")
        print(f"Seller prints: {items}")

        # Update item example
        status = update_item(stub, 1, 600, 10, "192.13.188.178:50051", "987a515c-a6e5-11ed-906b-76aef1e817c5")
        print(f"Seller prints: {'SUCCESS' if status == market_pb2.UpdateItemResponse.SUCCESS else 'FAIL'}")

        # Delete item example
        #status = delete_item(stub, 1, "192.13.188.178:50051", "987a515c-a6e5-11ed-906b-76aef1e817c5")
        #print(f"Seller prints: {'SUCCESS' if status == market_pb2.DeleteItemResponse.SUCCESS else 'FAIL'}")

        # Notify client example
        '''status = notify_client(stub, market_pb2.ItemDetails(
            item_id=1,
            price=500,
            product_name="iPhone",
            category=market_pb2.Category.ELECTRONICS,
            description="This is iPhone 15",
            quantity=5,
            rating=4.3,
            seller="192.13.188.178:50051"
        ))
        print(f"Seller prints: {'SUCCESS' if status == market_pb2.NotifyClientResponse.SUCCESS else 'FAIL'}")'''

if __name__ == '__main__':
    main()
