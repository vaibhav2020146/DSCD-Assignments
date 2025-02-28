# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shopping_platform.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17shopping_platform.proto\x1a\x1bgoogle/protobuf/empty.proto\"6\n\x15RegisterSellerRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"i\n\x16RegisterSellerResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.RegisterSellerResponse.Status\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"\x11\n\x0fSellItemRequest\"n\n\x10SellItemResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.SellItemResponse.Status\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"$\n\x11UpdateItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\"a\n\x12UpdateItemResponse\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.UpdateItemResponse.Status\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"$\n\x11\x44\x65leteItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\"a\n\x12\x44\x65leteItemResponse\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.DeleteItemResponse.Status\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\":\n\x19\x44isplaySellerItemsRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\x1c\n\x1a\x44isplaySellerItemsResponse\"8\n\x11SearchItemRequest\x12\x11\n\titem_name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"m\n\x12SearchItemResponse\x12.\n\x05items\x18\x01 \x03(\x0b\x32\x1f.SearchItemResponse.ItemDetails\x1a\'\n\x0bItemDetails\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"J\n\x0e\x42uyItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x15\n\rbuyer_address\x18\x03 \x01(\t\"[\n\x0f\x42uyItemResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.BuyItemResponse.Status\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\">\n\x14\x41\x64\x64ToWishListRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x15\n\rbuyer_address\x18\x02 \x01(\t\"g\n\x15\x41\x64\x64ToWishListResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.AddToWishListResponse.Status\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"I\n\x0fRateItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x15\n\rbuyer_address\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"]\n\x10RateItemResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.RateItemResponse.Status\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"\x15\n\x13NotifyClientRequest\"e\n\x14NotifyClientResponse\x12,\n\x06status\x18\x01 \x01(\x0e\x32\x1c.NotifyClientResponse.Status\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"6\n\x0fsellItemRequest\x12\x11\n\titem_name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"H\n\x19\x64isplaySellerItemsRequest\x12\x16\n\x0eseller_address\x18\x01 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x02 \x01(\t2\xc0\x02\n\rSellerService\x12\x41\n\x0eregisterSeller\x12\x16.RegisterSellerRequest\x1a\x17.RegisterSellerResponse\x12/\n\x08sellItem\x12\x10.SellItemRequest\x1a\x11.SellItemResponse\x12\x35\n\nupdateItem\x12\x12.UpdateItemRequest\x1a\x13.UpdateItemResponse\x12\x35\n\ndeleteItem\x12\x12.DeleteItemRequest\x1a\x13.DeleteItemResponse\x12M\n\x12\x64isplaySellerItems\x12\x1a.DisplaySellerItemsRequest\x1a\x1b.DisplaySellerItemsResponse2\xe4\x01\n\x0c\x42uyerService\x12\x35\n\nsearchItem\x12\x12.SearchItemRequest\x1a\x13.SearchItemResponse\x12,\n\x07\x62uyItem\x12\x0f.BuyItemRequest\x1a\x10.BuyItemResponse\x12>\n\raddToWishList\x12\x15.AddToWishListRequest\x1a\x16.AddToWishListResponse\x12/\n\x08rateItem\x12\x10.RateItemRequest\x1a\x11.RateItemResponse2\xcc\x01\n\rMarketService\x12;\n\x0cnotifyClient\x12\x14.NotifyClientRequest\x1a\x15.NotifyClientResponse\x12/\n\x08sellItem\x12\x10.SellItemRequest\x1a\x11.SellItemResponse\x12M\n\x12\x64isplaySellerItems\x12\x1a.DisplaySellerItemsRequest\x1a\x1b.DisplaySellerItemsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'shopping_platform_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REGISTERSELLERREQUEST']._serialized_start=56
  _globals['_REGISTERSELLERREQUEST']._serialized_end=110
  _globals['_REGISTERSELLERRESPONSE']._serialized_start=112
  _globals['_REGISTERSELLERRESPONSE']._serialized_end=217
  _globals['_REGISTERSELLERRESPONSE_STATUS']._serialized_start=186
  _globals['_REGISTERSELLERRESPONSE_STATUS']._serialized_end=217
  _globals['_SELLITEMREQUEST']._serialized_start=219
  _globals['_SELLITEMREQUEST']._serialized_end=236
  _globals['_SELLITEMRESPONSE']._serialized_start=238
  _globals['_SELLITEMRESPONSE']._serialized_end=348
  _globals['_SELLITEMRESPONSE_STATUS']._serialized_start=186
  _globals['_SELLITEMRESPONSE_STATUS']._serialized_end=217
  _globals['_UPDATEITEMREQUEST']._serialized_start=350
  _globals['_UPDATEITEMREQUEST']._serialized_end=386
  _globals['_UPDATEITEMRESPONSE']._serialized_start=388
  _globals['_UPDATEITEMRESPONSE']._serialized_end=485
  _globals['_UPDATEITEMRESPONSE_STATUS']._serialized_start=186
  _globals['_UPDATEITEMRESPONSE_STATUS']._serialized_end=217
  _globals['_DELETEITEMREQUEST']._serialized_start=487
  _globals['_DELETEITEMREQUEST']._serialized_end=523
  _globals['_DELETEITEMRESPONSE']._serialized_start=525
  _globals['_DELETEITEMRESPONSE']._serialized_end=622
  _globals['_DELETEITEMRESPONSE_STATUS']._serialized_start=186
  _globals['_DELETEITEMRESPONSE_STATUS']._serialized_end=217
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_start=624
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_end=682
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_start=684
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_end=712
  _globals['_SEARCHITEMREQUEST']._serialized_start=714
  _globals['_SEARCHITEMREQUEST']._serialized_end=770
  _globals['_SEARCHITEMRESPONSE']._serialized_start=772
  _globals['_SEARCHITEMRESPONSE']._serialized_end=881
  _globals['_SEARCHITEMRESPONSE_ITEMDETAILS']._serialized_start=842
  _globals['_SEARCHITEMRESPONSE_ITEMDETAILS']._serialized_end=881
  _globals['_BUYITEMREQUEST']._serialized_start=883
  _globals['_BUYITEMREQUEST']._serialized_end=957
  _globals['_BUYITEMRESPONSE']._serialized_start=959
  _globals['_BUYITEMRESPONSE']._serialized_end=1050
  _globals['_BUYITEMRESPONSE_STATUS']._serialized_start=186
  _globals['_BUYITEMRESPONSE_STATUS']._serialized_end=217
  _globals['_ADDTOWISHLISTREQUEST']._serialized_start=1052
  _globals['_ADDTOWISHLISTREQUEST']._serialized_end=1114
  _globals['_ADDTOWISHLISTRESPONSE']._serialized_start=1116
  _globals['_ADDTOWISHLISTRESPONSE']._serialized_end=1219
  _globals['_ADDTOWISHLISTRESPONSE_STATUS']._serialized_start=186
  _globals['_ADDTOWISHLISTRESPONSE_STATUS']._serialized_end=217
  _globals['_RATEITEMREQUEST']._serialized_start=1221
  _globals['_RATEITEMREQUEST']._serialized_end=1294
  _globals['_RATEITEMRESPONSE']._serialized_start=1296
  _globals['_RATEITEMRESPONSE']._serialized_end=1389
  _globals['_RATEITEMRESPONSE_STATUS']._serialized_start=186
  _globals['_RATEITEMRESPONSE_STATUS']._serialized_end=217
  _globals['_NOTIFYCLIENTREQUEST']._serialized_start=1391
  _globals['_NOTIFYCLIENTREQUEST']._serialized_end=1412
  _globals['_NOTIFYCLIENTRESPONSE']._serialized_start=1414
  _globals['_NOTIFYCLIENTRESPONSE']._serialized_end=1515
  _globals['_NOTIFYCLIENTRESPONSE_STATUS']._serialized_start=186
  _globals['_NOTIFYCLIENTRESPONSE_STATUS']._serialized_end=217
  _globals['_SELLITEMREQUEST']._serialized_start=1517
  _globals['_SELLITEMREQUEST']._serialized_end=1571
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_start=1573
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_end=1645
  _globals['_SELLERSERVICE']._serialized_start=1648
  _globals['_SELLERSERVICE']._serialized_end=1968
  _globals['_BUYERSERVICE']._serialized_start=1971
  _globals['_BUYERSERVICE']._serialized_end=2199
  _globals['_MARKETSERVICE']._serialized_start=2202
  _globals['_MARKETSERVICE']._serialized_end=2406
# @@protoc_insertion_point(module_scope)
