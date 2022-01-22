from typing import Union

from excel_class.col_sheet import ColSheet
from value_class.simple_value import SimpleValue
from value_class.equality_type import EqualityType
from value_class.value_type import ValueType


class ComplexValue(SimpleValue):
    from_: Union[ColSheet, None] = None
    to_: Union[ColSheet, None] = None
    realVal: None
    equality = EqualityType

    def __init__(self,value: str, from_: str = None, equality:EqualityType=EqualityType.EQUAL):
        super().__init__(value)
        self.type = ValueType.COMPLEX
        self.equality = equality
        from_ = from_.split('=')
        self.from_ = ColSheet(from_[0])
        self.to_ = ColSheet(from_[1])


    def getAllValue(self):
        res = super().getAllValue()
        if self.from_ is not None:
            res.append(self.from_)
        if self.to_ is not None:
            res.append(self.to_)
        return res