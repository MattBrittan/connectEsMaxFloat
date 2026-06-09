import struct
from google.protobuf.json_format import MessageToJson
from pb.pyt import test_pb2

max_float32 = struct.unpack('>f', b'\x7f\x7f\xff\xff')[0]
message = test_pb2.exampleMessage(exampleFloat=max_float32)
json_data = MessageToJson(message)

print(json_data)
