# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarket.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/descriptor.proto\"6\n\x15RegisterSellerRequest\x12\x0f\n\x07ip_port\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"k\n\x16RegisterSellerResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.RegisterSellerResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"\xa7\x01\n\x0fSellItemRequest\x12\x14\n\x0cproduct_name\x18\x01 \x01(\t\x12\x1b\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\t.Category\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x16\n\x0eseller_address\x18\x05 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x06 \x01(\t\x12\r\n\x05price\x18\x07 \x01(\x01\"p\n\x10SellItemResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.SellItemResponse.Status\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"z\n\x11UpdateItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x11\n\tnew_price\x18\x02 \x01(\x01\x12\x14\n\x0cnew_quantity\x18\x03 \x01(\x05\x12\x16\n\x0eseller_address\x18\x04 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x05 \x01(\t\"c\n\x12UpdateItemResponse\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.UpdateItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"Q\n\x11\x44\x65leteItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x16\n\x0eseller_address\x18\x02 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x03 \x01(\t\"c\n\x12\x44\x65leteItemResponse\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.DeleteItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"H\n\x19\x44isplaySellerItemsRequest\x12\x16\n\x0eseller_address\x18\x01 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x02 \x01(\t\"\x9b\x02\n\x1a\x44isplaySellerItemsResponse\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.DisplaySellerItemsResponse.ItemDetails\x1a\xc4\x01\n\x0bItemDetails\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\x14\n\x0cproduct_name\x18\x02 \x01(\t\x12\x1b\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\t.Category\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x16\n\x0eseller_address\x18\x06 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x07 \x01(\t\x12\r\n\x05price\x18\x08 \x01(\x01\x12\x0e\n\x06rating\x18\t \x01(\x01\"C\n\x11SearchItemRequest\x12\x11\n\titem_name\x18\x01 \x01(\t\x12\x1b\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\t.Category\"\xf4\x01\n\x12SearchItemResponse\x12\x31\n\x07results\x18\x01 \x03(\x0b\x32 .SearchItemResponse.SearchResult\x1a\xaa\x01\n\x0cSearchResult\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1b\n\x08\x63\x61tegory\x18\x04 \x01(\x0e\x32\t.Category\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x1a\n\x12quantity_remaining\x18\x06 \x01(\x05\x12\x0e\n\x06rating\x18\x07 \x01(\x01\x12\x0e\n\x06seller\x18\x08 \x01(\t\"J\n\x0e\x42uyItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x15\n\rbuyer_address\x18\x03 \x01(\t\"]\n\x0f\x42uyItemResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.BuyItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\">\n\x14\x41\x64\x64ToWishListRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x15\n\rbuyer_address\x18\x02 \x01(\t\"i\n\x15\x41\x64\x64ToWishListResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.AddToWishListResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"I\n\x0fRateItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x15\n\rbuyer_address\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"_\n\x10RateItemResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.RateItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01*=\n\x08\x43\x61tegory\x12\x0f\n\x0b\x45LECTRONICS\x10\x00\x12\x0b\n\x07\x46\x41SHION\x10\x01\x12\n\n\x06OTHERS\x10\x02\x12\x07\n\x03\x41NY\x10\x03\x32\xc0\x02\n\rSellerService\x12\x41\n\x0eRegisterSeller\x12\x16.RegisterSellerRequest\x1a\x17.RegisterSellerResponse\x12/\n\x08SellItem\x12\x10.SellItemRequest\x1a\x11.SellItemResponse\x12\x35\n\nUpdateItem\x12\x12.UpdateItemRequest\x1a\x13.UpdateItemResponse\x12\x35\n\nDeleteItem\x12\x12.DeleteItemRequest\x1a\x13.DeleteItemResponse\x12M\n\x12\x44isplaySellerItems\x12\x1a.DisplaySellerItemsRequest\x1a\x1b.DisplaySellerItemsResponse2\xe4\x01\n\x0c\x42uyerService\x12\x35\n\nSearchItem\x12\x12.SearchItemRequest\x1a\x13.SearchItemResponse\x12,\n\x07\x42uyItem\x12\x0f.BuyItemRequest\x1a\x10.BuyItemResponse\x12>\n\rAddToWishList\x12\x15.AddToWishListRequest\x1a\x16.AddToWishListResponse\x12/\n\x08RateItem\x12\x10.RateItemRequest\x1a\x11.RateItemResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CATEGORY']._serialized_start=2127
  _globals['_CATEGORY']._serialized_end=2188
  _globals['_REGISTERSELLERREQUEST']._serialized_start=79
  _globals['_REGISTERSELLERREQUEST']._serialized_end=133
  _globals['_REGISTERSELLERRESPONSE']._serialized_start=135
  _globals['_REGISTERSELLERRESPONSE']._serialized_end=242
  _globals['_REGISTERSELLERRESPONSE_STATUS']._serialized_start=209
  _globals['_REGISTERSELLERRESPONSE_STATUS']._serialized_end=242
  _globals['_SELLITEMREQUEST']._serialized_start=245
  _globals['_SELLITEMREQUEST']._serialized_end=412
  _globals['_SELLITEMRESPONSE']._serialized_start=414
  _globals['_SELLITEMRESPONSE']._serialized_end=526
  _globals['_SELLITEMRESPONSE_STATUS']._serialized_start=209
  _globals['_SELLITEMRESPONSE_STATUS']._serialized_end=242
  _globals['_UPDATEITEMREQUEST']._serialized_start=528
  _globals['_UPDATEITEMREQUEST']._serialized_end=650
  _globals['_UPDATEITEMRESPONSE']._serialized_start=652
  _globals['_UPDATEITEMRESPONSE']._serialized_end=751
  _globals['_UPDATEITEMRESPONSE_STATUS']._serialized_start=209
  _globals['_UPDATEITEMRESPONSE_STATUS']._serialized_end=242
  _globals['_DELETEITEMREQUEST']._serialized_start=753
  _globals['_DELETEITEMREQUEST']._serialized_end=834
  _globals['_DELETEITEMRESPONSE']._serialized_start=836
  _globals['_DELETEITEMRESPONSE']._serialized_end=935
  _globals['_DELETEITEMRESPONSE_STATUS']._serialized_start=209
  _globals['_DELETEITEMRESPONSE_STATUS']._serialized_end=242
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_start=937
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_end=1009
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_start=1012
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_end=1295
  _globals['_DISPLAYSELLERITEMSRESPONSE_ITEMDETAILS']._serialized_start=1099
  _globals['_DISPLAYSELLERITEMSRESPONSE_ITEMDETAILS']._serialized_end=1295
  _globals['_SEARCHITEMREQUEST']._serialized_start=1297
  _globals['_SEARCHITEMREQUEST']._serialized_end=1364
  _globals['_SEARCHITEMRESPONSE']._serialized_start=1367
  _globals['_SEARCHITEMRESPONSE']._serialized_end=1611
  _globals['_SEARCHITEMRESPONSE_SEARCHRESULT']._serialized_start=1441
  _globals['_SEARCHITEMRESPONSE_SEARCHRESULT']._serialized_end=1611
  _globals['_BUYITEMREQUEST']._serialized_start=1613
  _globals['_BUYITEMREQUEST']._serialized_end=1687
  _globals['_BUYITEMRESPONSE']._serialized_start=1689
  _globals['_BUYITEMRESPONSE']._serialized_end=1782
  _globals['_BUYITEMRESPONSE_STATUS']._serialized_start=209
  _globals['_BUYITEMRESPONSE_STATUS']._serialized_end=242
  _globals['_ADDTOWISHLISTREQUEST']._serialized_start=1784
  _globals['_ADDTOWISHLISTREQUEST']._serialized_end=1846
  _globals['_ADDTOWISHLISTRESPONSE']._serialized_start=1848
  _globals['_ADDTOWISHLISTRESPONSE']._serialized_end=1953
  _globals['_ADDTOWISHLISTRESPONSE_STATUS']._serialized_start=209
  _globals['_ADDTOWISHLISTRESPONSE_STATUS']._serialized_end=242
  _globals['_RATEITEMREQUEST']._serialized_start=1955
  _globals['_RATEITEMREQUEST']._serialized_end=2028
  _globals['_RATEITEMRESPONSE']._serialized_start=2030
  _globals['_RATEITEMRESPONSE']._serialized_end=2125
  _globals['_RATEITEMRESPONSE_STATUS']._serialized_start=209
  _globals['_RATEITEMRESPONSE_STATUS']._serialized_end=242
  _globals['_SELLERSERVICE']._serialized_start=2191
  _globals['_SELLERSERVICE']._serialized_end=2511
  _globals['_BUYERSERVICE']._serialized_start=2514
  _globals['_BUYERSERVICE']._serialized_end=2742
# @@protoc_insertion_point(module_scope)
