import ply.lex as lex
import ply.yacc as yacc
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
    'True' : 'TRUE',
    'False' : 'FALSE',
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

# Regras para pegar as expressões matemáticas
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('-', p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('*', p[1], p[3])

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUM'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_string(p):
    '''expression : STRING'''
    p[0] = p[1]

def p_expression_boolean(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = p[1]

# Define como o programa começa
def p_start(p):
    """start : expression
             | declaration"""
    p[0] = p[1]

# Define o tipo da variável
def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | STR
                      | BOOL'''
    p[0] = p[1]

# Define a declaração de uma variável
def p_declaration(p):
    'declaration : type_specifier ID expression_opt NEWLINE'
    if len(p) == 5:
        if p[3] is not None:
            p[0] = (p[1], p[2], p[3])
        else:
            p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], p[2], p[4])

def p_expression_opt(p):
    '''expression_opt : EQUALS expression
                      | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_empty(p):
    '''empty :'''
    pass

parser = yacc.yacc(start='start')

def ast(expression):
    return parser.parse(expression)

print(ast("bool teste = (4 + 3) * 5\n"))