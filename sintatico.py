import ply.lex as lex
import ply.yacc as yacc
# Define um dict com as palavras reservadas
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
    'then' : 'THEN'
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
t_DOUBLE_EQUALS = r'=='
t_TIMES = r'\*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_COMMA = r','
t_RBRACE = r'\}'
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

def p_factor_id(p):
    'factor : ID'
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

# ================= ATIVIDAS QUE FALTAM --> WHILE/FOR/IF ======================================

def p_comparison(p):
    '''comparison : DOUBLE_EQUALS
                  | NOT_EQUALS
                  | LESS_THAN
                  | LESS_THAN_OR_EQUALS
                  | GREATER_THAN
                  | GREATER_THAN_OR_EQUALS'''
    # Aqui você pode implementar a lógica para processar os diferentes operadores de comparação
    p[0] = p[1]

def p_condition(p):
    '''
        condition : expression comparison expression
                  | expression
    '''
    # p[0] = {'type': 'condition', 'left_expr': p[1], 'comparison': p[2], 'right_expr': p[3]}
    if (len(p) == 4):
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_expression_if(p):
    '''expression : IF LPAREN condition RPAREN LBRACE expression RBRACE '''
    p[0] = (p[1], p[3], p[6])

# ==============================================================================================

# Define como o programa começa
def p_start(p):
    """start : expression
             | declaration
             | function_declaration
             | return_statement
             | condition"""
    p[0] = p[1]

# Define o tipo da variável
def p_type_specifier(p):
    '''type : INT
            | FLOAT
            | STR
            | BOOL'''
    p[0] = p[1]

# Define a declaração de uma variável
def p_declaration(p):
    'declaration : type ID expression_opt'
    if len(p) == 4:
        if p[3] is not None:
            p[0] = (p[1], p[2], p[3])
        else:
            p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], p[2], p[3])

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

def p_function_declaration(p):
    '''function_declaration : type ID LPAREN parameter_list RPAREN LBRACE declaration_list NEWLINE return_statement NEWLINE RBRACE '''
    p[0] = ("function", p[1], p[2], p[4], p[7], p[9])

# define the parameter_list rule
def p_parameter_list(p):
    '''
    parameter_list : parameter_list COMMA parameter
                   | parameter
                   | empty
    '''
    if (len(p) == 4):
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

# define the parameter rule
def p_parameter(p):
    '''
    parameter : type ID
    '''
    p[0] = (p[1], p[2])

def p_return_statement(p):
    '''return_statement : RETURN expression'''
    p[0] = (p[1], p[2])

def p_declaration_list(p):
    '''declaration_list : declaration_list NEWLINE declaration
                        | declaration
                        | empty'''
    if (len(p) == 4):
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

parser = yacc.yacc(start='start')

def ast(expression):
    return parser.parse(expression)

"""
print(ast('''int func1 (int a, int b) {
                int a 
                int b = 34
                float c = 3.14
                return a
                }'''))
"""
print(ast("if(2<=3){\"iuashgdiuasd\"}"))