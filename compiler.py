from lex import Lexer
from parsers import Parser
from semantic import Semantic
from codeGenerator import CodeGenerator

lexer = Lexer()
parser = Parser()
semantic = Semantic()
codeGenerator = CodeGenerator()

with open('codigo.txt', 'r') as file:
    input_str = file.read()

ast = parser.ast_node_list(input_str)

codeGenerator.visit_function(ast)
#parser.print_ast(ast)
print(ast)
#semantic.visit_function(ast)