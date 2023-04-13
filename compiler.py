import sys
from lex import Lexer
from parsers import Parser
from semantic import Semantic
from codeGenerator import CodeGenerator

lexer = Lexer()
parser = Parser()
semantic = Semantic()
codeGenerator = CodeGenerator(optimize=True)

if len(sys.argv) < 2:
    print("Uso: python3 compiler.py <file_name>")
    sys.exit(1)
file_name = sys.argv[1]
with open(file_name, 'r') as file:
    input_str = file.read()

ast = parser.ast_node_list(input_str)
parser.print_ast(ast)
semantic.visit_tree(ast)

code_file_name = file_name.split('.txt')[0] + '.cpp'
code_file = open(code_file_name, "w")
sys.stdout = code_file
codeGenerator.visit_tree(ast)
sys.stdout = sys.__stdout__
code_file.close()