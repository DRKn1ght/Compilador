import ply.yacc as yacc
from lex import Lexer

class Parser:
    def __init__(self):
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)
        
    def p_program(self, p):
        '''program : declaration
                   | function_declaration
                     '''
        p[0] = p[1]
         
    # Regras para pegar as expressões matemáticas
    def p_expression_plus(self, p):
        'expression : expression PLUS term'
        p[0] = ('+', p[1], p[3])

    def p_expression_minus(self, p):
        'expression : expression MINUS term'
        p[0] = ('-', p[1], p[3])

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_term_times(self, p):
        'term : term TIMES factor'
        p[0] = ('*', p[1], p[3])

    def p_term_div(self, p):
        'term : term DIVIDE factor'
        p[0] = ('/', p[1], p[3])

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]

    def p_factor_num(self, p):
        'factor : NUM'
        p[0] = p[1]

    def p_factor_id(self, p):
        'factor : ID'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]


    def p_expression_string(self, p):
        '''expression : STRING'''
        p[0] = p[1]

    def p_expression_boolean(self, p):
        '''expression : TRUE
                    | FALSE'''
        p[0] = p[1]

    def p_print_statement(self, p):
        '''print_statement : PRINT LPAREN expression RPAREN SEMICOLON'''
        p[0] = ("PRINT", p[3])

    def p_statement(self, p):
        '''statement : expression
                    | if_statement
                    | while_statement
                    | declaration
                    | print_statement
                    | return_statement'''
        p[0] = p[1]

    def p_comparison(self, p):
        '''comparison : DOUBLE_EQUALS
                    | NOT_EQUALS
                    | LESS_THAN
                    | LESS_THAN_OR_EQUALS
                    | GREATER_THAN
                    | GREATER_THAN_OR_EQUALS'''
        p[0] = p[1]

    def p_condition(self, p):
        '''
            condition : expression comparison expression
                    | expression
        '''
        if (len(p) == 4):
            p[0] = (p[2], p[1], p[3])
        else:
            p[0] = p[1]

    def p_if_statement(self, p):
        '''if_statement : IF LPAREN condition RPAREN LBRACE declaration_list RBRACE'''
        p[0] = ("IF", p[3], p[6])

    def p_while_statement(self, p):
        '''while_statement : WHILE LPAREN condition RPAREN LBRACE declaration_list RBRACE'''
        p[0] = ("WHILE", p[3], p[6])

    # Define o tipo da variável
    def p_type_specifier(self, p):
        '''type : INT
                | FLOAT
                | STR
                | BOOL'''
        p[0] = p[1]

    # Define a declaração de uma variável
    def p_declaration(self, p):
        'declaration : type ID expression_opt SEMICOLON'
        if len(p) == 4:
            if p[3] is not None:
                p[0] = ("DECLARATION", p[1], p[2], p[3])
            else:
                p[0] = ("DECLARATION", p[1], p[2])
        else:
            p[0] = ("DECLARATION", p[1], p[2], p[3])

    def p_expression_opt(self, p):
        '''expression_opt : EQUALS expression
                        | empty'''
        if len(p) == 3:
            p[0] = p[2]
        else:
            p[0] = None

    def p_empty(self, p):
        '''empty :'''
        pass

    def p_function_declaration(self, p):
        '''function_declaration : type ID LPAREN parameter_list RPAREN LBRACE declaration_list RBRACE '''
        p[0] = ("FUNCTION", p[1], p[2], p[4], p[7])

    # define the parameter_list rule
    def p_parameter_list(self, p):
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
    def p_parameter(self, p):
        '''
        parameter : type ID
        '''
        p[0] = ("PARAMETER", p[1], p[2])

    def p_return_statement(self, p):
        '''return_statement : RETURN expression SEMICOLON'''
        p[0] = ("RETURN", p[2])

    def p_declaration_list(self, p):
        '''declaration_list : declaration_list statement
                            | statement
                            | empty'''
        if (len(p) == 3):
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def ast_node_list(self, expression):
        return self.parser.parse(expression, lexer = self.lexer.lexer)
    
    def print_ast(self, node_list, indent=0):
        if isinstance(node_list, list):
            for n in node_list:
                self.print_ast(n, indent + 2)
        else:
            print(" " * indent, end="")
            print(node_list[0])
            for i in range(1, len(node_list)):
                if isinstance(node_list[i], list):
                    self.print_ast(node_list[i], indent + 2)
                elif node_list[i] is not None:
                    print(" " * (indent + 2) + str(node_list[i]))
                else:
                    print(" " * (indent + 2) + "None")