from typing import Union

from value_class.complex_value import ComplexValue
from value_class.simple_value import SimpleValue


class BaseFilter:
    type: str
    field: str
    equality: str = "="
    value: Union[ComplexValue, SimpleValue]
    isRequired: bool = False
    isOr: bool = False

    def __init__(self, type: str, field: str, value: Union[ComplexValue, SimpleValue], required: bool= False, equality:str= "=", isOr:bool = False):
        """

        :param type: where or set
        :param field: first param
        :param value: last param
        :param required: if last param = null dont show the request
        :param equality: not implemented
        :param isOr: or where  instead of and where
        """
        self.type = type
        self.field = field
        self.value = value
        self.required = required
        self.equality = equality
        self.isOr = isOr

