from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RegisterSellerRequest(_message.Message):
    __slots__ = ("ip_address", "uuid")
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    uuid: str
    def __init__(self, ip_address: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class RegisterSellerResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SellItemRequest(_message.Message):
    __slots__ = ("product_name", "category", "quantity", "price", "description", "seller_address", "seller_uuid")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    category: str
    quantity: int
    price: float
    description: str
    seller_address: str
    seller_uuid: str
    def __init__(self, product_name: _Optional[str] = ..., category: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., description: _Optional[str] = ..., seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ...) -> None: ...

class SellItemResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateItemRequest(_message.Message):
    __slots__ = ("product_name", "price", "quantity", "seller_address", "seller_uuid")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    price: float
    quantity: int
    seller_address: str
    seller_uuid: str
    def __init__(self, product_name: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ...) -> None: ...

class UpdateItemResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DeleteItemRequest(_message.Message):
    __slots__ = ("product_name", "seller_address", "seller_uuid")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    seller_address: str
    seller_uuid: str
    def __init__(self, product_name: _Optional[str] = ..., seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ...) -> None: ...

class DeleteItemResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DisplaySellerItemsRequest(_message.Message):
    __slots__ = ("seller_uuid",)
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    seller_uuid: str
    def __init__(self, seller_uuid: _Optional[str] = ...) -> None: ...

class DisplaySellerItemsResponse(_message.Message):
    __slots__ = ("items",)
    class Item(_message.Message):
        __slots__ = ("product_name", "category", "quantity", "price", "description", "seller_address", "seller_uuid", "rating")
        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        product_name: str
        category: str
        quantity: int
        price: float
        description: str
        seller_address: str
        seller_uuid: str
        rating: int
        def __init__(self, product_name: _Optional[str] = ..., category: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., description: _Optional[str] = ..., seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ..., rating: _Optional[int] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DisplaySellerItemsResponse.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[DisplaySellerItemsResponse.Item, _Mapping]]] = ...) -> None: ...

class SearchItemRequest(_message.Message):
    __slots__ = ("product_name", "category")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    category: str
    def __init__(self, product_name: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...

class SearchItemResponse(_message.Message):
    __slots__ = ("items",)
    class Item(_message.Message):
        __slots__ = ("product_name", "category", "quantity", "price", "description", "seller_address", "seller_uuid", "rating")
        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        product_name: str
        category: str
        quantity: int
        price: float
        description: str
        seller_address: str
        seller_uuid: str
        rating: int
        def __init__(self, product_name: _Optional[str] = ..., category: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., description: _Optional[str] = ..., seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ..., rating: _Optional[int] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SearchItemResponse.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[SearchItemResponse.Item, _Mapping]]] = ...) -> None: ...

class BuyItemRequest(_message.Message):
    __slots__ = ("product_name", "quantity", "buyer_address", "seller_address")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    quantity: int
    buyer_address: str
    seller_address: str
    def __init__(self, product_name: _Optional[str] = ..., quantity: _Optional[int] = ..., buyer_address: _Optional[str] = ..., seller_address: _Optional[str] = ...) -> None: ...

class BuyItemResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AddToWishListRequest(_message.Message):
    __slots__ = ("product_name", "buyer_address", "seller_address")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    buyer_address: str
    seller_address: str
    def __init__(self, product_name: _Optional[str] = ..., buyer_address: _Optional[str] = ..., seller_address: _Optional[str] = ...) -> None: ...

class AddToWishListResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RateItemRequest(_message.Message):
    __slots__ = ("product_name", "rating", "seller_address")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    rating: int
    seller_address: str
    def __init__(self, product_name: _Optional[str] = ..., rating: _Optional[int] = ..., seller_address: _Optional[str] = ...) -> None: ...

class RateItemResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
