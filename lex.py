import ply.lex as lex

# Define um dict com as palavras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'int': 'INT',
    'str' : 'STR',
    'float' : 'FLOAT',
    'bool' : 'BOOL',
    'true' : 'TRUE',
    'false' : 'FALSE',
}

# Define a lista de Tokens
tokens = [
    'ID',
    'NUM',
    'STRING',
    'EQUALS',
    'TIMES',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'COMMA',
    'NEWLINE',
    'NOT_EQUALS',
    'LESS_THAN',
    'LESS_THAN_OR_EQUALS',
    'GREATER_THAN',
    'GREATER_THAN_OR_EQUALS'
]+ list(reserved.values())

# Define o Regex de cada token
t_NUM = r'\d+(\.\d+)?'
t_EQUALS = r'='
t_TIMES = r'\*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)' 
t_LBRACK = r'\{'
t_COMMA = r','
t_RBRACK = r'\}'
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_LESS_THAN_OR_EQUALS = r'<='
t_GREATER_THAN = r'>'
t_GREATER_THAN_OR_EQUALS = r'>='

# Define caracteres ignorados
t_ignore = ' \t'

# Define regra para diferenciar token de palavra reservada
def t_reserved(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define regra para strings
def t_STRING(t):
    r'"([^\\\n]|(\\.))*?"'
    t.value = t.value[1:-1] # Remove aspas
    return t

# Define regra para quebra de linha
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Define tratamento de erro
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = "bool z = true\nint a = 45\nfloat b = 34.5\nstr b = \"essa é uma string\"\nint func1(int a, int b) {\nint c = 5\nreturn c\n}"
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
