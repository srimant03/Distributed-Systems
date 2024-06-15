from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReceiveNotificationRequest_buyer(_message.Message):
    __slots__ = ("product_name", "category", "price", "quantity")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    category: str
    price: float
    quantity: int
    def __init__(self, product_name: _Optional[str] = ..., category: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class ReceiveNotificationResponse_buyer(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
