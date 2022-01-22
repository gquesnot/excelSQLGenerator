class ColSheet:
    sheetName: str
    col: str

    def __init__(self, string):
        self.sheetName, self.col = string.split('.')

    def __repr__(self):
        return f"{self.sheetName}:{self.col}"

    def __eq__(self, other):
        return self.sheetName == other.sheetName and self.col == other.col
