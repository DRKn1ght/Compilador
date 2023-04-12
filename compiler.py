from lex import Lexer
from parsers import Parser
lexer = Lexer()
parser = Parser()

with open('codigo.txt', 'r') as file:
    input_str = file.read()

ast = parser.ast_node_list(input_str)
parser.print_ast(ast)
print(ast)

symbol_table = {}

def visit_function(data):
  # data[0] = (function, tipo, id)
  # data[1] = (parameter_list)
  # data[2] = (command_list)
  symbol_table.update({data[0][2]: (data[0][1], data[0][0])})
  for params in data[1]:
     visit_params(params)
  for c in data[2]:
    visit(c)

def visit_params(data):
   # data[0] = PARAMETER
   # data[1] = TYPE
   # data[2] = ID
   print("DECLAROU_PARAM", data[1], data[2], '=', 'None')
   symbol_table.update({data[2]: (data[1], None)})

def get_symbol_table_value(expr):
    if (expr in symbol_table):
      if (symbol_table[expr][1] == None):
         return None
      if (symbol_table[expr][0] == 'int'):
          return int(symbol_table[expr][1])
      elif (symbol_table[expr][0] == 'float'):
          return float(symbol_table[expr][1])
      else:
          return symbol_table[expr][1]
    raise ValueError(f"A variável '{expr}' não foi declarada.")

def evaluate_expression(expr, type = None):
    if (type == 'bool' or isinstance(expr, bool)):
          return expr
    
    if (isinstance(expr, str)):
      value = get_symbol_table_value(expr)
      if (value == None):
        raise ValueError(f"A variável '{expr}', tem valor None.")
      else:
         expr = value
    
    if isinstance(expr, tuple):
        operator = expr[0]
        operand1 = evaluate_expression(expr[1], type)
        operand2 = evaluate_expression(expr[2], type)
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
    else:
        if (type == 'int'):
           return int(expr)
        else:
           return float(expr)

def visit_declaration(data):
  # data[0] = (DECLARATION)
  # data[1] = (tipo)
  # data[2] = (id)
  # data[3] = (exp)
  if data[2] in symbol_table:
    raise ValueError(f"Variável já declarada: {data[1], data[2]}")
  elif data[3] is not None:
    value = evaluate_expression(data[3], data[1])
    if (data[1] == 'bool'):
        if (isinstance(value, bool)):
            symbol_table.update({data[2]: (data[1], value)})
        else:
           raise ValueError(f"Variável {data[1], data[2]} tem que ser bool.")
    else:
       symbol_table.update({data[2]: (data[1], value)})
    print("DECLAROU", data[1], data[2], '=', value)
  else:
    print("DECLAROU", data[1], data[2], '=', None)
    symbol_table.update({data[2]: (data[1], None)})

def visit_assigment(data):
   # data[0] = (ASSIGMENT)
   # data[1] = ID
   # data[2] = (EXPRESSION)
   if (data[1] in symbol_table):
      type = symbol_table[data[1]][0]
      value = evaluate_expression(data[2], type)
      if (type == 'bool'):
            if (isinstance(value, bool)):
                symbol_table[data[1]] = (type, value)
            else:
                raise ValueError(f"Expressão {data[2]} tem que ser bool.")
     
      symbol_table[data[1]] = (type, value)
      print("ASSIGMENT", data[1], '=', value)

def visit(data):
  if data[0] == 'DECLARATION':
    return visit_declaration(data)
  if data[0] == 'ASSIGMENT':
     return visit_assigment(data)
  if data[0] == 'IF':
    return visit_if(data)
  if data[0] == 'PRINT':
    return visit_print(data)
  if data[0] == 'RETURN':
    return visit_return(data)
  if data[0] == 'WHILE':
    return visit_while(data)
  if data[0] == 'FUNCTION_CALL':
    return visit_function_call(data)

def visit_if(data):
  # data[0] = (IF)
  # data[1] = (condition)
  # data[2] = (command_list)

  visit_condition(data[1]) # verificar se a expressao booleana ta certa
  condition = visit_condition(data[1])
  print(condition)
  for c in data[2]:
    visit(c)

def visit_while(data):
  # data[0] = (WHILE)
  # data[1] = (condition)
  # data[2] = (command_list)
  condition = visit_condition(data[1])
  print(condition)
  for c in data[2]:
    visit(c)

def visit_condition(data):
  # data[0] = (OP)
  # data[1] = left exp
  # data[2] = right exp
  leftExp = evaluate_expression(data[1])
  rightExp = evaluate_expression(data[2])
  if isinstance(leftExp, (int, float)) and isinstance(rightExp, (int, float)):
    return (data[0], leftExp, rightExp)
  elif isinstance(leftExp, bool) and isinstance(rightExp, bool):
    return (data[0], leftExp, rightExp)
  else:
    raise ValueError(f"As expressões {data[1]} e {data[2]} precisam ser do mesmo tipo.")

def visit_function_call(data):
  # data[0] = (FUNCTION_CALL)
  # data[1] = (ID)
  # data[2] = (args)
  print(data[0], data[1], data[2])

def visit_print(data):
  # data[0] = (PRINT)
  # data[1] = expression
  print(data[0], data[1])

def visit_return(data):
  # data[0] = (RETURN)
  # data[1] = exp
  print(data[0], evaluate_expression(data[1]))

visit_function(ast)
#print(evaluate_expression(5.0, 'int'))