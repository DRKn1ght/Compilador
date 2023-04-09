import ply.lex as lex

class Lexer:
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE',
        'return': 'RETURN',
        'int': 'INT',
        'str' : 'STR',
        'float' : 'FLOAT',
        'bool' : 'BOOL',
        'True' : 'TRUE',
        'False' : 'FALSE',
        'print' : 'PRINT',
    }

    # Define a lista de Tokens
    tokens = [
        'ID',
        'NUM',
        'STRING',
        'EQUALS',
        'DOUBLE_EQUALS',
        'TIMES',
        'PLUS',
        'MINUS',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'LBRACE',
        'RBRACE',
        'COMMA',
        'SEMICOLON',
        'NEWLINE',
        'NOT_EQUALS',
        'LESS_THAN',
        'LESS_THAN_OR_EQUALS',
        'GREATER_THAN',
        'GREATER_THAN_OR_EQUALS',
    ]+ list(reserved.values())

    # Define o Regex de cada token
    t_NUM = r'\d+(\.\d+)?'
    t_EQUALS = r'='
    t_DOUBLE_EQUALS = r'=='
    t_TIMES = r'\*'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_COMMA = r','
    t_SEMICOLON = r';'
    t_RBRACE = r'\}'
    t_NOT_EQUALS = r'!='
    t_LESS_THAN = r'<'
    t_LESS_THAN_OR_EQUALS = r'<='
    t_GREATER_THAN = r'>'
    t_GREATER_THAN_OR_EQUALS = r'>='

    # Define caracteres ignorados
    t_ignore = ' \t'

    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Define regra para diferenciar token de palavra reservada    
    def t_reserved(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    # Define regra para strings
    def t_STRING(self, t):
        r'"([^\\\n]|(\\.))*?"'
        t.value = t.value[1:-1] # Remove aspas
        return t

    # Define regra para quebra de linha
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Define tratamento de erro
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)