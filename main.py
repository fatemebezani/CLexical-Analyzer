from Token import Token
import pandas as pd

Tokens = []
keywords = ['typedef', 'extern', 'static', 'auto', 'register', 'void', 'char', 'short', 'int', 'long', 'float',
            'double', 'signed', 'unsigned', 'goto', 'continue', 'break', 'return', 'case', 'default', 'switch',
            'struct', 'union', 'enum', 'while', 'do', 'for', 'const', 'volatile', 'if', 'else', 'sizeof'
            ]


def add_token(token_type, token_literal, token_column, token_row, token_block):
    Tokens.append(Token(token_type, token_literal, token_column, token_row, token_block))


code = open("Input.txt", mode='r').read()

col = 1
row = 1
block_no = 0
index = -1

while index < len(code) - 1:
    index += 1
    current_char = code[index]
    if current_char.isspace():
        match current_char:
            case '\t':
                col += 4
            case ' ':
                col += 1
            case '\n':
                col = 1
                row += 1
        continue

    match current_char:

        case '+':
            if code[index + 1] == '=':
                col += 2
                add_token('operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '+':
                col += 2
                add_token('operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('operator', code[index], col - 1, row, block_no)

        case '-':
            if code[index + 1] == '=':
                col += 2
                add_token('operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '-':
                col += 2
                add_token('operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '>':
                col += 2
                add_token('arrow', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('operator', code[index], col - 1, row, block_no)

        case '*':
            if code[index + 1] == '=':
                col += 2
                add_token('operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('asterisk', code[index], col - 1, row, block_no)

        case '/':
            if code[index + 1] == '=':
                col += 2
                add_token('operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '/':
                while code[index] != '\n':
                    index += 1
                row += 1

            elif code[index + 1] == '*':
                while code[index:index + 2] != '*/':
                    index += 1
                    if code[index] == '\n':
                        row += 1
                index += 1
            else:
                col += 1
                add_token('operator', code[index], col - 1, row, block_no)

        case '%':
            if code[index + 1] == '=':
                col += 2
                add_token('operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('percent', code[index], col - 1, row, block_no)

        case '!':
            if code[index + 1] == '=':
                col += 2
                add_token('boolean operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('bit-wise operator', code[index], col - 1, row, block_no)

        case '|':
            if code[index + 1] == '=':
                col += 2
                add_token('bit-wise operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '|':
                col += 2
                add_token('boolean operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('operator', code[index], col - 1, row, block_no)

        case '&':
            if code[index + 1] == '=':
                col += 2
                add_token('bit-and assign', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '&':
                col += 2
                add_token('boolean operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('ampersand', code[index], col - 1, row, block_no)

        case '^':
            if code[index + 1] == '=':
                col += 2
                add_token('xor assign', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('xor', code[index], col - 1, row, block_no)

        case '{':
            col += 1
            block_no += 1
            add_token('left curly-brace', code[index], col - 1, row, block_no)

        case '}':
            col += 1
            block_no -= 1
            add_token('right curly-brace', code[index], col - 1, row, block_no)

        case '#':
            continue

        case '~':
            if code[index + 1] == '=':
                col += 2
                add_token('bit-not assign', code[index:index + 2], col - 2, row, block_no)
                index += 1
            else:
                col += 1
                add_token('tilda', code[index], col - 1, row, block_no)

        case '?':
            col += 1
            add_token('question', code[index], col - 1, row, block_no)

        case ':':
            col += 1
            add_token('colon', code[index], col - 1, row, block_no)

        case '.':
            if code[index: index + 3] == '...':
                col += 3
                add_token('ellipsis', code[index:index + 3], col - 3, row, block_no)
                index += 2
            else:
                col += 1
                add_token('dot', code[index], col - 1, row, block_no)

        case '[':
            col += 1
            add_token('left bracket', code[index], col - 1, row, block_no)

        case ']':
            col += 1
            add_token('right bracket', code[index], col - 1, row, block_no)

        case ':':
            col += 1
            add_token('colon', code[index], col - 1, row, block_no)

        case "'":
            if code[index + 1] == '\'':
                col += 2
                add_token('empty-quote', code[index:index + 2], col - 2, row, block_no)
                index += 1
            else:
                col += 3
                add_token('quote', code[index:index + 3], col - 3, row, block_no)
                index += 3

        case '(':
            col += 1
            add_token('left parentheses', code[index], col - 1, row, block_no)

        case ')':
            col += 1
            add_token('right parentheses', code[index], col - 1, row, block_no)

        case ';':
            col += 1
            add_token('semi-colon', code[index], col - 1, row, block_no)

        case '=':
            if code[index + 1] == '=':
                col += 2
                add_token('boolean operator', code[index], col - 2, row, block_no)
                index += 1
            else:
                col += 1
                add_token('operator', code[index], col - 1, row, block_no)

        case current_char if current_char.isnumeric():
            c_index = index
            current_col = col
            while code[index].isnumeric() or (code[index] == '.' and code[index + 1].isnumeric()):
                index += 1
                col += 1
            if '.' in code[c_index:index]:
                add_token('float', code[c_index:index], current_col, row, block_no)
            else:
                add_token('integer', code[c_index:index], current_col, row, block_no)
            index -= 1

        case '"':
            c_index = index
            current_col = col
            index += 1
            col += 1
            while code[index] != '"':
                index += 1
                col += 1
            add_token('string', code[c_index:index + 1], current_col, row, block_no)

        case ',':
            col += 1
            add_token('comma', code[index], col - 1, row, block_no)

        case '<':
            if code[index: index + 3] == '<<=':
                col += 3
                add_token('left-shift assign', code[index:index + 3], col - 3, row, block_no)
                index += 2
            elif code[index + 1] == '<':
                col += 2
                add_token('left shift', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '=':
                col += 2
                add_token('relational operator', code[index:index + 2], col - 2, row, block_no)
                index += 1

            else:
                col += 1
                add_token('relational operator', code[index], col - 1, row, block_no)

        case '>':
            if code[index: index + 3] == '>>=':
                col += 3
                add_token('right-shift assign', code[index:index + 3], col - 3, row, block_no)
                index += 2

            elif code[index + 1] == '>':
                col += 2
                add_token('right shift', code[index:index + 2], col - 2, row, block_no)
                index += 1

            elif code[index + 1] == '=':
                col += 2
                add_token('relational operator', code[index:index + 2], col - 2, row, block_no)
                index += 1
            else:
                col += 1
                add_token('relational operator', code[index], col - 1, row, block_no)

        case current_char if code[index].isalpha() or code[index] == '_':
            c_index = index
            current_col = col
            while code[index].isalnum() or code[index] == '_':
                index += 1
                col += 1

            if code[c_index:index] in keywords:
                add_token('keyword', code[c_index:index], current_col, row, block_no)
            else:
                add_token('identifier', code[c_index:index], current_col, row, block_no)
            index -= 1

        case _:
            raise Exception('Error! Unknown character is used at row:{} and column:{}'.format(row, col))

output = pd.DataFrame(
    {"Type": [x.Type for x in Tokens], "Literal": [str(x.Literal) for x in Tokens], "Row": [x.Row for x in Tokens],
     "Col": [x.Col for x in Tokens], "Block No.": [x.BlockNo for x in Tokens], })

print("Output Excel file Created.")
output.to_csv("Output.csv")
