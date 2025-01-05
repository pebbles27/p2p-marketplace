# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: bazaar.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'bazaar.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62\x61zaar.proto\x12\x06\x62\x61zaar\"6\n\nCacheState\x12\x0c\n\x04\x62oar\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ish\x18\x02 \x01(\x05\x12\x0c\n\x04salt\x18\x03 \x01(\x05\"9\n\x13\x46\x61iledTraderMessage\x12\x11\n\ttrader_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1d\n\nAckMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0bPingMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"x\n\nWCBMessage\x12\x10\n\x08\x62uyer_id\x18\x01 \x01(\x05\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x12\n\nrequest_no\x18\x04 \x01(\x05\x12\x11\n\ttrader_id\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x06 \x01(\t\"n\n\nWCSMessage\x12\x11\n\tseller_id\x18\x01 \x01(\x05\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x17\n\x0fregistration_no\x18\x04 \x01(\x05\x12\x11\n\ttrader_id\x18\x05 \x01(\x05\"#\n\x0c\x43lockMessage\x12\x13\n\x0b\x63lock_value\x18\x01 \x01(\x05\"&\n\x13\x43lockUpdateResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"k\n\x11\x42uyRequestMessage\x12\x10\n\x08\x62uyer_id\x18\x01 \x01(\x05\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\r\n\x05\x63lock\x18\x04 \x01(\x05\x12\x12\n\nrequest_no\x18\x05 \x01(\x05\"$\n\x11\x42uyReturnResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"k\n\x0fPurchaseMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08\x62uyer_id\x18\x02 \x01(\x05\x12\x0f\n\x07product\x18\x03 \x01(\t\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x12\x12\n\nrequest_no\x18\x05 \x01(\x05\"#\n\x10PurchaseResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x8c\x01\n\x12TransactionMessage\x12\x10\n\x08\x62uyer_id\x18\x01 \x01(\x05\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x17\n\x0f\x61mount_credited\x18\x04 \x01(\x02\x12\x14\n\x0cout_of_stock\x18\x05 \x01(\t\x12\x12\n\nrequest_no\x18\x06 \x01(\x05\"&\n\x13TransactionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x0f\x45lectionRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x11\n\tsender_id\x18\x02 \x01(\x05\"*\n\x10\x45lectionResponse\x12\x16\n\x0e\x61\x63knowledgment\x18\x01 \x01(\x08\"\'\n\x12LeaderAnnouncement\x12\x11\n\tleader_id\x18\x01 \x01(\x05\"!\n\x0eLeaderResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"n\n\x0eProductDetails\x12\x11\n\tseller_id\x18\x01 \x01(\x05\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x17\n\x0fregistration_no\x18\x04 \x01(\x05\x12\r\n\x05\x63lock\x18\x05 \x01(\x05\"\x8b\x01\n\x10RegisterResponse\x12\x11\n\tseller_id\x18\x01 \x01(\x05\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x17\n\x0fregistration_no\x18\x04 \x01(\x05\x12\x17\n\x0f\x61mount_credited\x18\x05 \x01(\x02\x12\x0f\n\x07message\x18\x06 \x01(\t2\xbd\x06\n\rBazaarService\x12\x44\n\x0f\x45lectionMessage\x12\x17.bazaar.ElectionRequest\x1a\x18.bazaar.ElectionResponse\x12\x44\n\x0e\x41nnounceLeader\x12\x1a.bazaar.LeaderAnnouncement\x1a\x16.bazaar.LeaderResponse\x12\x43\n\x0fRegisterProduct\x12\x16.bazaar.ProductDetails\x1a\x18.bazaar.RegisterResponse\x12\x42\n\nBuyRequest\x12\x19.bazaar.BuyRequestMessage\x1a\x19.bazaar.BuyReturnResponse\x12@\n\x0b\x43lockUpdate\x12\x14.bazaar.ClockMessage\x1a\x1b.bazaar.ClockUpdateResponse\x12\x46\n\x11PurchaseProcessed\x12\x17.bazaar.PurchaseMessage\x1a\x18.bazaar.PurchaseResponse\x12\x45\n\x15RegistrationProcessed\x12\x18.bazaar.RegisterResponse\x1a\x12.bazaar.AckMessage\x12J\n\x1bWarehouseCommunicationBuyer\x12\x12.bazaar.WCBMessage\x1a\x17.bazaar.PurchaseMessage\x12L\n\x1cWarehouseCommunicationSeller\x12\x12.bazaar.WCSMessage\x1a\x18.bazaar.RegisterResponse\x12\x35\n\tHeartBeat\x12\x13.bazaar.PingMessage\x1a\x13.bazaar.PingMessage\x12@\n\rTraderFailure\x12\x1b.bazaar.FailedTraderMessage\x1a\x12.bazaar.AckMessage\x12\x33\n\tSyncCache\x12\x12.bazaar.CacheState\x1a\x12.bazaar.AckMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bazaar_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CACHESTATE']._serialized_start=24
  _globals['_CACHESTATE']._serialized_end=78
  _globals['_FAILEDTRADERMESSAGE']._serialized_start=80
  _globals['_FAILEDTRADERMESSAGE']._serialized_end=137
  _globals['_ACKMESSAGE']._serialized_start=139
  _globals['_ACKMESSAGE']._serialized_end=168
  _globals['_PINGMESSAGE']._serialized_start=170
  _globals['_PINGMESSAGE']._serialized_end=200
  _globals['_WCBMESSAGE']._serialized_start=202
  _globals['_WCBMESSAGE']._serialized_end=322
  _globals['_WCSMESSAGE']._serialized_start=324
  _globals['_WCSMESSAGE']._serialized_end=434
  _globals['_CLOCKMESSAGE']._serialized_start=436
  _globals['_CLOCKMESSAGE']._serialized_end=471
  _globals['_CLOCKUPDATERESPONSE']._serialized_start=473
  _globals['_CLOCKUPDATERESPONSE']._serialized_end=511
  _globals['_BUYREQUESTMESSAGE']._serialized_start=513
  _globals['_BUYREQUESTMESSAGE']._serialized_end=620
  _globals['_BUYRETURNRESPONSE']._serialized_start=622
  _globals['_BUYRETURNRESPONSE']._serialized_end=658
  _globals['_PURCHASEMESSAGE']._serialized_start=660
  _globals['_PURCHASEMESSAGE']._serialized_end=767
  _globals['_PURCHASERESPONSE']._serialized_start=769
  _globals['_PURCHASERESPONSE']._serialized_end=804
  _globals['_TRANSACTIONMESSAGE']._serialized_start=807
  _globals['_TRANSACTIONMESSAGE']._serialized_end=947
  _globals['_TRANSACTIONRESPONSE']._serialized_start=949
  _globals['_TRANSACTIONRESPONSE']._serialized_end=987
  _globals['_ELECTIONREQUEST']._serialized_start=989
  _globals['_ELECTIONREQUEST']._serialized_end=1042
  _globals['_ELECTIONRESPONSE']._serialized_start=1044
  _globals['_ELECTIONRESPONSE']._serialized_end=1086
  _globals['_LEADERANNOUNCEMENT']._serialized_start=1088
  _globals['_LEADERANNOUNCEMENT']._serialized_end=1127
  _globals['_LEADERRESPONSE']._serialized_start=1129
  _globals['_LEADERRESPONSE']._serialized_end=1162
  _globals['_PRODUCTDETAILS']._serialized_start=1164
  _globals['_PRODUCTDETAILS']._serialized_end=1274
  _globals['_REGISTERRESPONSE']._serialized_start=1277
  _globals['_REGISTERRESPONSE']._serialized_end=1416
  _globals['_BAZAARSERVICE']._serialized_start=1419
  _globals['_BAZAARSERVICE']._serialized_end=2248
# @@protoc_insertion_point(module_scope)
