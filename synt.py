import ply.yacc as yacc
from lex import lexer

# Define the start symbol for the grammar
start = 'program'

# Define the grammar rules
def p_program(p):
    '''program : statement
               | program statement'''
    pass

def p_statement(p):
    '''statement : declaration NEWLINE
                 | assignment NEWLINE
                 | function NEWLINE'''
    pass

def p_declaration(p):
    '''declaration : type ID EQUALS expression'''
    pass

def p_assignment(p):
    '''assignment : ID EQUALS expression'''
    pass

def p_expression(p):
    '''expression : ID
                  | NUM
                  | STRING'''
    pass

def p_function(p):
    '''function : type ID LPAREN params RPAREN LBRACK statement RBRACK'''
    pass

def p_params(p):
    '''params :
              | params_list'''

def p_params_list(p):
    '''params_list : type ID
                   | params_list COMMA type ID'''

def p_type(p):
    '''type : INT
            | FLOAT
            | STR
            | BOOL'''

tokens = lexer.token
# Define the lexer
lexer = lexer

# Define the parser
parser = yacc.yacc()

# Define the input
data = "bool z = true\nint a = 45\nfloat b = 34.5\nstr b = \"essa é uma string\"\nint func1(int a, int b) {\nint c = 5\nreturn c\n}"

# Parse the input
lexer.input(data)  # update this line to use your lexer
parser.parse(data, lexer = lexer)
