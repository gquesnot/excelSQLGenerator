from typing import Union

from excel_class.col_sheet import ColSheet
from value_class.value_type import ValueType


class SimpleValue:
    type: ValueType
    value: ColSheet
    realVal: None

    def __init__(self, value: str):
        """

        :param value: str like "sheetName.Col"
        """
        self.type = ValueType.SIMPLE
        self.value = ColSheet(value)

    def setRealVal(self, realVal):
        self.realVal = realVal

    def getVal(self):
        return self.realVal

    def getAllValue(self):
        res = []
        if self.value is not None:
            res.append(self.value)
        return res

    def isComplex(self):
        return self.type == ValueType.COMPLEX
