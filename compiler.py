from lex import Lexer
from parsers import Parser
lexer = Lexer()
parser = Parser()

with open('codigo.txt', 'r') as file:
    input_str = file.read()

ast = parser.ast_node_list(input_str)
parser.print_ast(ast)
print(ast)