from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReceiveNotificationRequest(_message.Message):
    __slots__ = ("notification_message", "product_name", "quantity", "buyer_address")
    NOTIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    notification_message: str
    product_name: str
    quantity: int
    buyer_address: str
    def __init__(self, notification_message: _Optional[str] = ..., product_name: _Optional[str] = ..., quantity: _Optional[int] = ..., buyer_address: _Optional[str] = ...) -> None: ...

class ReceiveNotificationResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
