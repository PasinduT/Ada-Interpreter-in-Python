class Literal:
    def __init__(self, typ, value):
        self.typ, self.value = typ, value

class Identifier:
    def __init__(self, nam):
        self.nam = nam

class Operators:
    def __init__(self, typ):
        self.typ = typ

class Keywords:
    def __init__(self, typ):
        self.typ = typ

keywords = ['procedure', 'is', 'begin', 'end', 'with', 'use', 'and', 'or', 'integer', 'string', 'natural', 'positive', 'char', 'boolean']
class Tokens:
    def __init__(self, code):
        self.code = code

    def make_tokens(self):
        code = self.code
        tokens = []

        i = 0
        while(i < len(code)):
            c = code[i]
            
            if c == '"':
                if i < len(code):
                    i += 1
                    c = code[i]

                else:
                    raise ValueError('Unterminated string literal')

                temp = ''

                while(c != '"'):
                    temp += c
                    if i < len(code):
                        i += 1
                        c = code[i]
                    else:
                        raise ValueError('Unterminated string literal')

                StringLiteral = Literal('string', temp)
                tokens.append(StringLiteral)

            elif c.isalpha():
                temp = ''
                while c.isalum() or c == '_':
                    temp += c
                    if i < len(code):
                        i += 1
                        c = code[i]
                    else:
                        break

                if temp.lower() in keywords:
                    res = Keywords(temp.lower())
                else:
                    res = Identifier(temp.lower())

                tokens.append(res)
