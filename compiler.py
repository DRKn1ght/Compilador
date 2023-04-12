from lex import Lexer
from parsers import Parser
from semantic import Semantic
from codeGenerator import CodeGenerator

lexer = Lexer()
parser = Parser()
semantic = Semantic()
codeGenerator = CodeGenerator(optimize=True)

with open('codigo.txt', 'r') as file:
    input_str = file.read()

ast = parser.ast_node_list(input_str)


#parser.print_ast(ast)
print(ast)
semantic.visit_function(ast)
codeGenerator.visit_function(ast)