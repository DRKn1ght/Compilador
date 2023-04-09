symbol_table = [{}]

def visit_function(data):
  # data[0] = (function, tipo, id)
  # data[1] = (parameter_list)
  # data[2] = (command_list)
  for c in data[2]:
    visit(c) 

def visit_declaration(data):
  # data[0] = (DECLARATION)
  # data[1] = (tipo)
  # data[2] = (id)
  # data[3] = (exp)
  if data[2] in symbol_table:
    return 'variavel ja declarada'
  elif data[3] is not None:
    print(data[1], data[2], "=", data[3])
  else:
    print(data[1], data[2], "=", data[3])

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

data = (('FUNCTION', 'int', 'func1'), [('PARAMETER', 'int', 'a'), ('PARAMETER', 'int', 'b')], [('DECLARATION', 'int', 'a', None), ('DECLARATION', 'int', 'b', '34'), ('IF', ('<', 'a', 'b'), [('DECLARATION', 'int', 'a', '5'), ('DECLARATION', 'bool', 'b', 'False'), ('PRINT', 'Primeiro if')]), ('WHILE', ('<', 'a', '5'), [('DECLARATION', 'float', 'c', ('+', '3.14', 'c')), ('PRINT', 'c')]), ('FUNCTION_CALL', 'func1', None), ('RETURN', ('+', '4', '3'))])

visit_function(data)
