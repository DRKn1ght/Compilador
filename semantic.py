class Semantic:
  def __init__(self):
    # symbol_table = (id : (type, value))
    # function_table = (id : (type, has_return))
    self.symbol_table = {}
    self.function_table = {}

  def visit_tree(self, nodes):
     for functions in nodes:
        self.symbol_table = {}
        self.visit_function(functions)
      
     if(self.function_table.get('start')) == None:
        raise ValueError("É necessário uma função chamada 'start'.")
     else:
        self.function_table['start']
    
  def visit_function(self, data):
    # data[0] = (function, tipo, id)
    # data[1] = (parameter_list)
    # data[2] = (command_list)
    self.function_table.update({data[0][2]: (data[0][1], data[1], False)})
    if (data[1] is not None):
      if (data[0][2] == 'start'):
         raise ValueError("A função 'start' não pode ter parâmetros.")
      for params in data[1]:
        self.visit_params(params)
    for c in data[2]:
      self.visit(c, data)
    
    for functions in self.function_table:
       if (self.function_table[functions][1]) == False:
          raise ValueError(f"A função '{functions}' precisa de return.")

  def visit_params(self, data):
    # data[0] = PARAMETER
    # data[1] = TYPE
    # data[2] = ID
    print("DECLAROU_PARAM", data[1], data[2], '=', 0)
    self.symbol_table.update({data[2]: (data[1], 0)})

  def get_symbol_table_value(self, expr):
      if (expr in self.symbol_table):
        if (self.symbol_table[expr][1] == None):
          return None
        if (self.symbol_table[expr][0] == 'int'):
            return int(self.symbol_table[expr][1])
        elif (self.symbol_table[expr][0] == 'float'):
            return float(self.symbol_table[expr][1])
        elif (self.symbol_table[expr][0] == 'str'):
            return str(self.symbol_table[expr][1])
        else:
            return self.symbol_table[expr][1]
      raise ValueError(f"A variável '{expr}' não foi declarada.")

  def evaluate_expression(self, expr, type = None):
      if (type == 'bool' or isinstance(expr, bool)):
            return expr
      if isinstance(expr, tuple) and expr[0] == 'STRING':
        type, value = expr
        return '"' + value + '"'
      if (isinstance(expr, str)):
        value = self.get_symbol_table_value(expr)
        if (value == None):
          raise ValueError(f"A variável '{expr}', tem valor None.")
        else:
          expr = value
      
      if isinstance(expr, tuple):
          operator = expr[0]
          operand1 = self.evaluate_expression(expr[1], type)
          operand2 = self.evaluate_expression(expr[2], type)
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

  def visit_declaration(self, data):
    # data[0] = (DECLARATION)
    # data[1] = (tipo)
    # data[2] = (id)
    # data[3] = (exp)
    if data[2] in self.symbol_table:
      raise ValueError(f"Variável já declarada: {data[1], data[2]}")
    elif data[3] is not None:
      value = self.evaluate_expression(data[3], data[1])
      if (data[1] == 'bool'):
          if (isinstance(value, bool)):
              self.symbol_table.update({data[2]: (data[1], value)})
          else:
            raise ValueError(f"Variável {data[1], data[2]} tem que ser bool.")
      elif (data[1] == 'str'):
         if (isinstance(value, str)):
            self.symbol_table.update({data[2]: (data[1], value)})
         else:
            raise ValueError(f"Variável {data[1], data[2]} tem que ser str")
      else:
        self.symbol_table.update({data[2]: (data[1], value)})
      print("DECLAROU", data[1], data[2], '=', value)
    else:
      print("DECLAROU", data[1], data[2], '=', None)
      self.symbol_table.update({data[2]: (data[1], None)})

  def visit_assigment(self, data):
    # data[0] = (ASSIGMENT)
    # data[1] = ID
    # data[2] = (EXPRESSION)
    if (data[1] in self.symbol_table):
        type = self.symbol_table[data[1]][0]
        value = self.evaluate_expression(data[2], type)
        if (type == 'bool'):
              if (isinstance(value, bool)):
                  self.symbol_table[data[1]] = (type, value)
              else:
                  raise ValueError(f"Expressão {data[2]} tem que ser bool.")
        if (type == 'str'):
              if (isinstance(value, str)):
                 self.symbol_table[data[1]] = (type, value)
              else:
                 raise ValueError(f"Expressão {data[2]} tem que ser str.")
        self.symbol_table[data[1]] = (type, value)
        print("ASSIGMENT", data[1], '=', value)

  def visit(self, data, function = None):
    if data[0] == 'DECLARATION':
      return self.visit_declaration(data)
    if data[0] == 'ASSIGMENT':
      return self.visit_assigment(data)
    if data[0] == 'IF':
      return self.visit_if(data)
    if data[0] == 'PRINT':
      return self.visit_print(data)
    if data[0] == 'RETURN':
      return self.visit_return(data, function)
    if data[0] == 'WHILE':
      return self.visit_while(data)
    if data[0] == 'FUNCTION_CALL':
      return self.visit_function_call(data)

  def visit_if(self, data):
    # data[0] = (IF)
    # data[1] = (condition)
    # data[2] = (command_list)

    self.visit_condition(data[1]) # verificar se a expressao booleana ta certa
    condition = self.visit_condition(data[1])
    print(condition)
    for c in data[2]:
      self.visit(c)

  def visit_while(self, data):
    # data[0] = (WHILE)
    # data[1] = (condition)
    # data[2] = (command_list)
    condition = self.visit_condition(data[1])
    print(condition)
    for c in data[2]:
      self.visit(c)

  def visit_condition(self, data):
    # data[0] = (OP)
    # data[1] = left exp
    # data[2] = right exp
    leftExp = self.evaluate_expression(data[1])
    rightExp = self.evaluate_expression(data[2])
    if isinstance(leftExp, (int, float)) and isinstance(rightExp, (int, float)):
      return (data[0], leftExp, rightExp)
    elif isinstance(leftExp, bool) and isinstance(rightExp, bool):
      return (data[0], leftExp, rightExp)
    else:
      raise ValueError(f"As expressões {data[1]} e {data[2]} precisam ser do mesmo tipo.")

  def visit_function_call(self, data):
    # data[0] = (FUNCTION_CALL)
    # data[1] = (ID)
    # data[2] = (args)
    print(data[0], data[1], data[2])
    if (self.function_table[data[1]][1] == None):
       params_len = 0
    else:
       params_len = len(self.function_table[data[1]][1])
    
    if (data[2] == None):
       args_len = 0
    else:
       args_len = len(data[2])
    
    if (params_len != args_len):
       raise ValueError(f"A função '{data[1]}' precisa de {params_len} parâmetros, mas está recebendo {args_len}.")
       

  def visit_print(self, data):
    # data[0] = (PRINT)
    # data[1] = expression
    print(data[0], data[1])

  def visit_return(self, data, function):
    # data[0] = (RETURN)
    # data[1] = exp
    # function[0] = (FUNCTION)
    # function[1] = (type)
    # function[2] = (id)
    print(data[0], self.evaluate_expression(data[1]))
    self.symbol_table.update({data[0]: (data[1])})
    
    # Atualiza que a função tem return
    self.function_table[function[0][2]] = (function[0][1], function[1], True)