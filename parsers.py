import ply.yacc as yacc
from lex import Lexer

# Sintático
class Parser:
    def __init__(self):
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)
    
    # Define regra de início de programa
    def p_program(self, p):
        '''
        program : function_declaration_list
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
        p[0] = float(p[1])

    def p_factor_id(self, p):
        'factor : ID'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    # Define regra para string
    def p_expression_string(self, p):
        '''expression : STRING'''
        p[0] = ("STRING", p[1])

    # Define regra para boolean
    def p_expression_boolean(self, p):
        '''expression : TRUE
                      | FALSE'''
        if (p[1] == 'True'):
            p[0] = True
        else:
            p[0] = False

    # Define regra para print
    def p_print_statement(self, p):
        '''print_statement : PRINT LPAREN expression RPAREN SEMICOLON
                           | PRINT LPAREN function_call RPAREN SEMICOLON'''
        p[0] = ("PRINT", p[3])

    # Define o que serão statement
    def p_statement(self, p):
        '''statement : expression
                     | if_statement
                     | while_statement
                     | declaration
                     | print_statement
                     | return_statement
                     | function_call
                     | assigment'''
        p[0] = p[1]

    # Define regra para uma comparação
    def p_comparison(self, p):
        '''comparison : DOUBLE_EQUALS
                      | NOT_EQUALS
                      | LESS_THAN
                      | LESS_THAN_OR_EQUALS
                      | GREATER_THAN
                      | GREATER_THAN_OR_EQUALS'''
        p[0] = p[1]

    # Define regra de uma condição
    def p_condition(self, p):
        '''
            condition : expression comparison expression
                    | expression
        '''
        if (len(p) == 4):
            p[0] = (p[2], p[1], p[3])
        else:
            p[0] = p[1]

    # Define regra de um if
    def p_if_statement(self, p):
        '''if_statement : IF LPAREN condition RPAREN LBRACE declaration_list RBRACE'''
        p[0] = ("IF", p[3], p[6])

    # Define regra de um while
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
        '''declaration : type ID EQUALS expression SEMICOLON
                       | type ID SEMICOLON
        '''
        if len(p) == 6:
            p[0] = ("DECLARATION", p[1], p[2], p[4])
        else:
            p[0] = ("DECLARATION", p[1], p[2], None)

    # Define regra para lista de declarações
    def p_declaration_list(self, p):
        '''declaration_list : declaration_list statement
                            | statement
                            | empty'''
        if (len(p) == 3):
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    # Define regra para alteração de valor de uma variável
    def p_assigment(self, p):
        '''assigment : ID EQUALS expression SEMICOLON'''
        p[0] = ("ASSIGMENT", p[1], p[3])

    # Define regra para lambda
    def p_empty(self, p):
        '''empty :'''
        pass

    # Define regra para chamada de função
    def p_function_call(self, p):
        '''function_call : ID LPAREN arg_list RPAREN SEMICOLON'''
        p[0] = ("FUNCTION_CALL", p[1], p[3])

    # Define regra de um argumento, usado em chamada de função
    def p_arg(self, p):
        '''arg : expression'''
        p[0] = ("ARG", p[1])

    def p_arg_list(self, p):
        '''arg_list : arg_list COMMA arg
                    | arg
                    | empty'''
        if (len(p) == 4):
            p[0] = p[1] + [p[3]]
        elif (p[1] is not None):
            p[0] = [p[1]]
        else:
            p[0] = p[1]

    # Define declaração de uma função
    def p_function_declaration(self, p):
        '''function_declaration : type ID LPAREN parameter_list RPAREN LBRACE declaration_list RBRACE '''
        p[0] = (("FUNCTION", p[1], p[2]), p[4], p[7])

    # Define regra de lista de declaração de função
    def p_function_declaration_list(self, p):
        '''
        function_declaration_list : function_declaration
                                | function_declaration_list function_declaration
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    # Define regra de um parâmetro
    def p_parameter(self, p):
        '''
        parameter : type ID
        '''
        p[0] = ("PARAMETER", p[1], p[2])

    # Define regra para lista de parâmetros
    def p_parameter_list(self, p):
        '''
        parameter_list : parameter_list COMMA parameter
                       | parameter
                       | empty
        '''
        if (len(p) == 4):
            p[0] = p[1] + [p[3]]
        elif (p[1] is not None):
            p[0] = [p[1]]
        else:
            p[0] = p[1]

    # Define regra de um return
    def p_return_statement(self, p):
        '''return_statement : RETURN expression SEMICOLON
                            | RETURN function_call SEMICOLON'''
        p[0] = ("RETURN", p[2])

    # Retorna lista de nós
    def ast_node_list(self, expression):
        return self.parser.parse(expression, lexer = self.lexer.lexer)
    
    # Imprime a lista de nós em forma de árvore
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