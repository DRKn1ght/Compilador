import sys
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
semantic.visit_tree(ast)

code_file = open("codigo.cpp", "w")
sys.stdout = code_file
codeGenerator.visit_tree(ast)
sys.stdout = sys.__stdout__
code_file.close()