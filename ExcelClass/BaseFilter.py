from typing import Union

from valueClass.ComplexValue import ComplexValue
from valueClass.SimpleValue import SimpleValue


class BaseFilter:
    type: str
    field: str
    equality: str = "="
    value: Union[ComplexValue, SimpleValue]
    isRequired: bool = False
    isOr: bool = False

    def __init__(self, type: str, field: str, value: Union[ComplexValue, SimpleValue], required: bool= False, equality:str= "=", isOr:bool = False):
        self.type = type
        self.field = field
        self.value = value
        self.required = required
        self.equality = equality
        self.isOr = isOr

