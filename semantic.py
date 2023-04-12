symbol_table = {}

def visit_function(data):
  # data[0] = (function, tipo, id)
  # data[1] = (parameter_list)
  # data[2] = (command_list)
  for c in data[2]:
    visit(c) 

def evaluate_expression(expr, type):
    if (isinstance(expr, str)):
      if (expr in symbol_table):
        if (symbol_table[expr][0] == 'int'):
            return int(symbol_table[expr][1])
        elif (symbol_table[expr][0] == 'float'):
            return float(symbol_table[expr][1])
        else:
            raise ValueError(f"Variável é do tipo {symbol_table[expr]}, deveria ser int ou float")
      else:
         raise ValueError(f"A variável {expr} não existe")
          
    if (type == 'bool'):
       return expr
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
    symbol_table.update({data[1]: (data[2], evaluate_expression(data[3], data[1]))})
  else:
    symbol_table.update({data[1]: (data[2], None)})

def visit(data):
  if data[0] == 'DECLARATION':
    return visit_declaration(data)
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
  print(data[0], data[1])
  for c in data[2]:
    visit(c)

def visit_while(data):
  # data[0] = (WHILE)
  # data[1] = (condition)
  # data[2] = (command_list)
  visit_condition(data[1])
  print(data[0], data[1])
  for c in data[2]:
    visit(c)
def visit_condition(data):
  pass

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
  print(data[0], data[1])

data = (('FUNCTION', 'int', 'func1'), [('PARAMETER', 'int', 'a'), ('PARAMETER', 'int', 'b')], [('DECLARATION', 'int', 'a', None), ('DECLARATION', 'int', 'b', ('+', 4.0, ('*', 3.0, 2.0))), ('IF', ('<', 'a', 'b'), [('DECLARATION', 'int', 'c', 5.0), ('DECLARATION', 'bool', 'd', False), ('PRINT', 'Primeiro if')]), ('WHILE', ('<', 'a', 5.0), [('DECLARATION', 'float', 'e', ('+', 3.14, 'c'))]), ('FUNCTION_CALL', 'func1', None), ('RETURN', ('+', ('+', ('+', 4.0, ('*', 3.0, 3.0)), 3.0), 2.0))])
visit_function(data)
#print(evaluate_expression(5.0, 'int'))