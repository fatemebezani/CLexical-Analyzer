class Token:
    Type = None
    Literal = None
    Row = None
    Col = None
    BlockNo = None

    def __init__(self, token_type, literal, col, row, block_no):
        self.Type = token_type
        self.Literal = literal
        self.Row = row
        self.Col = col
        self.BlockNo = block_no

    def __repr__(self):
        return "Type: {}   Literal: {}   Row: {}   Column: {}   Block-Number: {}".format(self.Type, self.Literal,
                                                                                         self.Row,
                                                                                         self.Col, self.BlockNo)