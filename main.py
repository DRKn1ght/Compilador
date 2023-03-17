import ply.lex as lex

# Define a lista de Tokens
tokens = (
    'ID',
    'NUM',
    'EQUALS',
)

# Define o Regex de cada token
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUM = r'\d+'
t_EQUALS = r'='

# Define caracteres ignorados
t_ignore = ' \t'

# Define tratamento de erro
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = "foo = 42"
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
