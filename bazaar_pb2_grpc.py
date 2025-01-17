# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import bazaar_pb2 as bazaar__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in bazaar_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BazaarServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ElectionMessage = channel.unary_unary(
                '/bazaar.BazaarService/ElectionMessage',
                request_serializer=bazaar__pb2.ElectionRequest.SerializeToString,
                response_deserializer=bazaar__pb2.ElectionResponse.FromString,
                _registered_method=True)
        self.AnnounceLeader = channel.unary_unary(
                '/bazaar.BazaarService/AnnounceLeader',
                request_serializer=bazaar__pb2.LeaderAnnouncement.SerializeToString,
                response_deserializer=bazaar__pb2.LeaderResponse.FromString,
                _registered_method=True)
        self.RegisterProduct = channel.unary_unary(
                '/bazaar.BazaarService/RegisterProduct',
                request_serializer=bazaar__pb2.ProductDetails.SerializeToString,
                response_deserializer=bazaar__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.BuyRequest = channel.unary_unary(
                '/bazaar.BazaarService/BuyRequest',
                request_serializer=bazaar__pb2.BuyRequestMessage.SerializeToString,
                response_deserializer=bazaar__pb2.BuyReturnResponse.FromString,
                _registered_method=True)
        self.ClockUpdate = channel.unary_unary(
                '/bazaar.BazaarService/ClockUpdate',
                request_serializer=bazaar__pb2.ClockMessage.SerializeToString,
                response_deserializer=bazaar__pb2.ClockUpdateResponse.FromString,
                _registered_method=True)
        self.PurchaseProcessed = channel.unary_unary(
                '/bazaar.BazaarService/PurchaseProcessed',
                request_serializer=bazaar__pb2.PurchaseMessage.SerializeToString,
                response_deserializer=bazaar__pb2.PurchaseResponse.FromString,
                _registered_method=True)
        self.RegistrationProcessed = channel.unary_unary(
                '/bazaar.BazaarService/RegistrationProcessed',
                request_serializer=bazaar__pb2.RegisterResponse.SerializeToString,
                response_deserializer=bazaar__pb2.AckMessage.FromString,
                _registered_method=True)
        self.WarehouseCommunicationBuyer = channel.unary_unary(
                '/bazaar.BazaarService/WarehouseCommunicationBuyer',
                request_serializer=bazaar__pb2.WCBMessage.SerializeToString,
                response_deserializer=bazaar__pb2.PurchaseMessage.FromString,
                _registered_method=True)
        self.WarehouseCommunicationSeller = channel.unary_unary(
                '/bazaar.BazaarService/WarehouseCommunicationSeller',
                request_serializer=bazaar__pb2.WCSMessage.SerializeToString,
                response_deserializer=bazaar__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.HeartBeat = channel.unary_unary(
                '/bazaar.BazaarService/HeartBeat',
                request_serializer=bazaar__pb2.PingMessage.SerializeToString,
                response_deserializer=bazaar__pb2.PingMessage.FromString,
                _registered_method=True)
        self.TraderFailure = channel.unary_unary(
                '/bazaar.BazaarService/TraderFailure',
                request_serializer=bazaar__pb2.FailedTraderMessage.SerializeToString,
                response_deserializer=bazaar__pb2.AckMessage.FromString,
                _registered_method=True)
        self.SyncCache = channel.unary_unary(
                '/bazaar.BazaarService/SyncCache',
                request_serializer=bazaar__pb2.CacheState.SerializeToString,
                response_deserializer=bazaar__pb2.AckMessage.FromString,
                _registered_method=True)


class BazaarServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ElectionMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnnounceLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuyRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClockUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PurchaseProcessed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegistrationProcessed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WarehouseCommunicationBuyer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WarehouseCommunicationSeller(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraderFailure(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyncCache(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BazaarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ElectionMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ElectionMessage,
                    request_deserializer=bazaar__pb2.ElectionRequest.FromString,
                    response_serializer=bazaar__pb2.ElectionResponse.SerializeToString,
            ),
            'AnnounceLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.AnnounceLeader,
                    request_deserializer=bazaar__pb2.LeaderAnnouncement.FromString,
                    response_serializer=bazaar__pb2.LeaderResponse.SerializeToString,
            ),
            'RegisterProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterProduct,
                    request_deserializer=bazaar__pb2.ProductDetails.FromString,
                    response_serializer=bazaar__pb2.RegisterResponse.SerializeToString,
            ),
            'BuyRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.BuyRequest,
                    request_deserializer=bazaar__pb2.BuyRequestMessage.FromString,
                    response_serializer=bazaar__pb2.BuyReturnResponse.SerializeToString,
            ),
            'ClockUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.ClockUpdate,
                    request_deserializer=bazaar__pb2.ClockMessage.FromString,
                    response_serializer=bazaar__pb2.ClockUpdateResponse.SerializeToString,
            ),
            'PurchaseProcessed': grpc.unary_unary_rpc_method_handler(
                    servicer.PurchaseProcessed,
                    request_deserializer=bazaar__pb2.PurchaseMessage.FromString,
                    response_serializer=bazaar__pb2.PurchaseResponse.SerializeToString,
            ),
            'RegistrationProcessed': grpc.unary_unary_rpc_method_handler(
                    servicer.RegistrationProcessed,
                    request_deserializer=bazaar__pb2.RegisterResponse.FromString,
                    response_serializer=bazaar__pb2.AckMessage.SerializeToString,
            ),
            'WarehouseCommunicationBuyer': grpc.unary_unary_rpc_method_handler(
                    servicer.WarehouseCommunicationBuyer,
                    request_deserializer=bazaar__pb2.WCBMessage.FromString,
                    response_serializer=bazaar__pb2.PurchaseMessage.SerializeToString,
            ),
            'WarehouseCommunicationSeller': grpc.unary_unary_rpc_method_handler(
                    servicer.WarehouseCommunicationSeller,
                    request_deserializer=bazaar__pb2.WCSMessage.FromString,
                    response_serializer=bazaar__pb2.RegisterResponse.SerializeToString,
            ),
            'HeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=bazaar__pb2.PingMessage.FromString,
                    response_serializer=bazaar__pb2.PingMessage.SerializeToString,
            ),
            'TraderFailure': grpc.unary_unary_rpc_method_handler(
                    servicer.TraderFailure,
                    request_deserializer=bazaar__pb2.FailedTraderMessage.FromString,
                    response_serializer=bazaar__pb2.AckMessage.SerializeToString,
            ),
            'SyncCache': grpc.unary_unary_rpc_method_handler(
                    servicer.SyncCache,
                    request_deserializer=bazaar__pb2.CacheState.FromString,
                    response_serializer=bazaar__pb2.AckMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bazaar.BazaarService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('bazaar.BazaarService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BazaarService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ElectionMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/ElectionMessage',
            bazaar__pb2.ElectionRequest.SerializeToString,
            bazaar__pb2.ElectionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AnnounceLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/AnnounceLeader',
            bazaar__pb2.LeaderAnnouncement.SerializeToString,
            bazaar__pb2.LeaderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/RegisterProduct',
            bazaar__pb2.ProductDetails.SerializeToString,
            bazaar__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BuyRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/BuyRequest',
            bazaar__pb2.BuyRequestMessage.SerializeToString,
            bazaar__pb2.BuyReturnResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClockUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/ClockUpdate',
            bazaar__pb2.ClockMessage.SerializeToString,
            bazaar__pb2.ClockUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PurchaseProcessed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/PurchaseProcessed',
            bazaar__pb2.PurchaseMessage.SerializeToString,
            bazaar__pb2.PurchaseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegistrationProcessed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/RegistrationProcessed',
            bazaar__pb2.RegisterResponse.SerializeToString,
            bazaar__pb2.AckMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WarehouseCommunicationBuyer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/WarehouseCommunicationBuyer',
            bazaar__pb2.WCBMessage.SerializeToString,
            bazaar__pb2.PurchaseMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WarehouseCommunicationSeller(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/WarehouseCommunicationSeller',
            bazaar__pb2.WCSMessage.SerializeToString,
            bazaar__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def HeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/HeartBeat',
            bazaar__pb2.PingMessage.SerializeToString,
            bazaar__pb2.PingMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TraderFailure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/TraderFailure',
            bazaar__pb2.FailedTraderMessage.SerializeToString,
            bazaar__pb2.AckMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SyncCache(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bazaar.BazaarService/SyncCache',
            bazaar__pb2.CacheState.SerializeToString,
            bazaar__pb2.AckMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
