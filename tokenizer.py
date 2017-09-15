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

            if c == ' ':
                if i < len(code):
                    i += 1
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
                    if temp[-1] == '_':
                        raise ValueError('Invalid identifier name')
                    res = Identifier(temp.lower())

                tokens.append(res)

            elif c.isdigit():
                temp = 0
                i = 0
                while c.isdigit() or c == '.' or c == '_':
                    if c == '_':
                        continue
                    elif c == '.':
                        i = 1
                    else:
                        if i > 0:
                            temp = temp + int(c) / 10
                        else:
                            temp = temp * 10 + int(c)

                    if i < len(code):
                        i += 1
                        c = code[i]
                    else:
                        break

                if temp > int(temp):
                    floatLiteral = Literal('float')
                else:
                    integerLiteral = Literal('Integer')

            elif c == "'":
                if i < len(code):
                    i += 1
                    c = code[i]

                temp = c

                if i < len(code):
                    i += 1
                    c = code[i]
                else:
                    raise ValueError('Unterminated Character Literal')

                
                
