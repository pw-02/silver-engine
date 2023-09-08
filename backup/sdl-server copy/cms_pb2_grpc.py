# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cms_pb2 as cms__pb2


class CacheManagementServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProcessJobEndedMessage = channel.unary_unary(
        '/cms.CacheManagementService/ProcessJobEndedMessage',
        request_serializer=cms__pb2.JobEndedMessage.SerializeToString,
        response_deserializer=cms__pb2.MessageResponse.FromString,
        )
    self.GetNextBatchForJob = channel.unary_unary(
        '/cms.CacheManagementService/GetNextBatchForJob',
        request_serializer=cms__pb2.GetNextBatchForJobMessage.SerializeToString,
        response_deserializer=cms__pb2.GetNextBatchForJobResponse.FromString,
        )
    self.RegisterNewTrainingJob = channel.unary_unary(
        '/cms.CacheManagementService/RegisterNewTrainingJob',
        request_serializer=cms__pb2.RegisterTrainingJobMessage.SerializeToString,
        response_deserializer=cms__pb2.RegisterTrainingJobResponse.FromString,
        )
    self.GetServerResponse = channel.unary_unary(
        '/cms.CacheManagementService/GetServerResponse',
        request_serializer=cms__pb2.Message.SerializeToString,
        response_deserializer=cms__pb2.MessageResponse.FromString,
        )


class CacheManagementServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ProcessJobEndedMessage(self, request, context):
    """A simple RPC.
    Obtains the MessageResponse at a given position.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNextBatchForJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterNewTrainingJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetServerResponse(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CacheManagementServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProcessJobEndedMessage': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessJobEndedMessage,
          request_deserializer=cms__pb2.JobEndedMessage.FromString,
          response_serializer=cms__pb2.MessageResponse.SerializeToString,
      ),
      'GetNextBatchForJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetNextBatchForJob,
          request_deserializer=cms__pb2.GetNextBatchForJobMessage.FromString,
          response_serializer=cms__pb2.GetNextBatchForJobResponse.SerializeToString,
      ),
      'RegisterNewTrainingJob': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterNewTrainingJob,
          request_deserializer=cms__pb2.RegisterTrainingJobMessage.FromString,
          response_serializer=cms__pb2.RegisterTrainingJobResponse.SerializeToString,
      ),
      'GetServerResponse': grpc.unary_unary_rpc_method_handler(
          servicer.GetServerResponse,
          request_deserializer=cms__pb2.Message.FromString,
          response_serializer=cms__pb2.MessageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cms.CacheManagementService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))