from optimizer import OptimizeCode
optimizer = OptimizeCode()

class CodeGenerator:
  def __init__(self, optimize = False):
    self.optimize = optimize
    
  def ident(self, level):
    return " " * level

  def evaluate_expression(self, expr, type = None):
    if isinstance(expr, bool):
      if (expr == True):
        return "true"
      else:
        return "false"
    if isinstance(expr, (float, int)):
        if (type == 'int'):
          return int(expr)
        else:
          return float(expr)
    if isinstance(expr, tuple) and expr[0] == 'STRING':
        type, value = expr
        return '"' + value + '"'

    if self.optimize == True and type is not 'STRING':
      return optimizer.optimize_expression(expr,type)

    if (isinstance(expr, tuple)):
      op, left, right = expr
    else:
      return str(expr)
    if isinstance(left, tuple):
        left = '(' + self.evaluate_expression(left, type) + ')'
    if isinstance(right, tuple):
        right = '(' + self.evaluate_expression(right, type) + ')'
    return f'{self.evaluate_expression(left, type)} {op} {self.evaluate_expression(right, type)}'

  def visit_function(self, data, ident_level = 0):
    # data[0] = (function, tipo, id)
    # data[1] = (parameter_list)
    # data[2] = (command_list)

    print("#include <iostream>\n#include <string>\nusing namespace std;\n")
    print(f"{self.ident(ident_level)}{data[0][1]} {data[0][2]}(", end="")
    if (data[1] is not None):
      for i, params in enumerate(data[1]):
        self.visit_params(params)
        if i < len(data[1]) - 1:
              print(", ", end="")
    print(") {")

    for c in data[2]:
      self.visit(c, ident_level+4)
    print(f"{self.ident(ident_level)}}}")
    self.print_main_function(data)
  
  def print_main_function(self, data):
    default_values = {'int': 0,
                      'float': 0.0,
                      'str': '""',
                      'bool': 'false'}
    args = "("
    if (data[1] is not None):
      for i, params in enumerate(data[1]):
        if (i < len(data[1]) -1):
          args += f"{default_values[params[1]]}, "
      args += f"{default_values[params[1]]})"
    else:
      args += ")"
    print(f"""
int main(){{
    {data[0][2]}{args};
    return 0;
}}""")

  def visit_params(self, data):
    # data[0] = PARAMETER
    # data[1] = TYPE
    # data[2] = ID
    print(f"{data[1]} {data[2]}", end="")

  def visit_declaration(self, data, ident_level=0):
    # data[0] = (DECLARATION)
    # data[1] = (tipo)
    # data[2] = (id)
    # data[3] = (exp)
    if (data[1] == 'str'):
      type = 'String'
    else:
      type = data[1]
    if data[3] is not None:
      value = self.evaluate_expression(data[3], type=data[1])
      print(f"{self.ident(ident_level)}{type} {data[2]} = {value};")
    else:
      print(f"{self.ident(ident_level)}{type} {data[2]};")

  def visit_assigment(self, data, ident_level=0):
    # data[0] = (ASSIGMENT)
    # data[1] = ID
    # data[2] = (EXPRESSION)
    value = self.evaluate_expression(data[2])
    print(f"{self.ident(ident_level)}{data[1]} = {value};")

  def visit(self, data, ident_level=0):
    if data[0] == 'DECLARATION':
      return self.visit_declaration(data, ident_level)
    if data[0] == 'ASSIGMENT':
      return self.visit_assigment(data, ident_level)
    if data[0] == 'IF':
      return self.visit_if(data, ident_level+4)
    if data[0] == 'PRINT':
      return self.visit_print(data, ident_level)
    if data[0] == 'RETURN':
      return self.visit_return(data, ident_level)
    if data[0] == 'WHILE':
      return self.visit_while(data, ident_level+4)
    if data[0] == 'FUNCTION_CALL':
      return self.visit_function_call(data, ident_level)

  def visit_if(self, data, ident_level=0):
    # data[0] = (IF)
    # data[1] = (condition)
    # data[2] = (command_list)

    condition = self.visit_condition(data[1]) # verificar se a expressao booleana ta certa
    print(f"{self.ident(ident_level-4)}if ({condition[0]} {condition[1]} {condition[2]})", end="")
    print("{")
    for c in data[2]:
      self.visit(c, ident_level)
    print(f"{self.ident(ident_level-4)}}}")

  def visit_while(self, data, ident_level=0):
    # data[0] = (WHILE)
    # data[1] = (condition)
    # data[2] = (command_list)
    condition = self.visit_condition(data[1])

    print(f"{self.ident(ident_level-4)}while ({condition[0]} {condition[1]} {condition[2]})", end="")
    print("{")
    for c in data[2]:
      self.visit(c, ident_level)
    print(f"{self.ident(ident_level-4)}}}")

  def visit_condition(self, data, ident_level=0):
    # data[0] = (OP)
    # data[1] = left exp
    # data[2] = right exp
    left_expr = self.evaluate_expression(data[1])
    right_expr = self.evaluate_expression(data[2])
    return (left_expr, data[0], right_expr)

  def visit_function_call(self, data, ident_level=0):
    # data[0] = (FUNCTION_CALL)
    # data[1] = (ID)
    # data[2] = (args)
    print(f"{self.ident(ident_level)}{data[1]}(", end="")
    if data[2] is not None:
      for i, args in enumerate(data[2]):
        print(f"{args[1]}", end = "")
        if i < len(data[2]) - 1:
          print(", ", end="")
    print(");")

  def visit_print(self, data, ident_level=0):
    # data[0] = (PRINT)
    # data[1] = expression
    value = self.evaluate_expression(data[1], type='STRING')
    print(f"{self.ident(ident_level)}cout << {value};")

  def visit_return(self, data, ident_level=0):
    # data[0] = (RETURN)
    # data[1] = exp
    value = self.evaluate_expression(data[1])
    print(f"{self.ident(ident_level)}return {value};")