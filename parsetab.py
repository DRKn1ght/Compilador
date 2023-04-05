
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startBOOL COMMA DIVIDE ELSE EQUALS FALSE FLOAT GREATER_THAN GREATER_THAN_OR_EQUALS ID IF INT LBRACE LESS_THAN LESS_THAN_OR_EQUALS LPAREN MINUS NEWLINE NOT_EQUALS NUM PLUS RBRACE RETURN RPAREN STR STRING THEN TIMES TRUE WHILEexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMfactor : IDfactor : LPAREN expression RPARENexpression : STRINGexpression : TRUE\n                  | FALSEstart : expression\n             | declaration\n             | function_declaration\n             | return_statementtype : INT\n            | FLOAT\n            | STR\n            | BOOLdeclaration : type ID expression_optexpression_opt : EQUALS expression\n                      | emptyempty :function_declaration : type ID LPAREN parameter_list RPAREN LBRACE declaration_list NEWLINE return_statement NEWLINE RBRACE \n    parameter_list : parameter_list COMMA parameter\n                   | parameter\n                   | empty\n    \n    parameter : type ID\n    return_statement : RETURN expressiondeclaration_list : declaration_list NEWLINE declaration\n                        | declaration\n                        | empty'
    
_lr_action_items = {'STRING':([0,12,13,33,],[7,7,7,7,]),'TRUE':([0,12,13,33,],[8,8,8,8,]),'FALSE':([0,12,13,33,],[9,9,9,9,]),'RETURN':([0,51,],[13,13,]),'INT':([0,32,43,44,51,],[15,15,15,15,15,]),'FLOAT':([0,32,43,44,51,],[16,16,16,16,16,]),'STR':([0,32,43,44,51,],[17,17,17,17,17,]),'BOOL':([0,32,43,44,51,],[18,18,18,18,18,]),'NUM':([0,12,13,20,21,22,23,33,],[19,19,19,19,19,19,19,19,]),'ID':([0,10,12,13,15,16,17,18,20,21,22,23,33,36,46,],[11,24,11,11,-17,-18,-19,-20,11,11,11,11,11,41,50,]),'LPAREN':([0,12,13,20,21,22,23,24,33,],[12,12,12,12,12,12,12,32,12,]),'$end':([1,2,3,4,5,6,7,8,9,11,14,19,24,26,27,28,29,30,31,34,35,40,55,],[0,-13,-14,-15,-16,-3,-10,-11,-12,-8,-6,-7,-24,-30,-1,-2,-4,-5,-21,-23,-9,-22,-25,]),'PLUS':([2,6,7,8,9,11,14,19,25,26,27,28,29,30,35,40,],[20,-3,-10,-11,-12,-8,-6,-7,20,20,-1,-2,-4,-5,-9,20,]),'MINUS':([2,6,7,8,9,11,14,19,25,26,27,28,29,30,35,40,],[21,-3,-10,-11,-12,-8,-6,-7,21,21,-1,-2,-4,-5,-9,21,]),'RPAREN':([6,7,8,9,11,14,19,25,27,28,29,30,32,35,37,38,39,41,45,],[-3,-10,-11,-12,-8,-6,-7,35,-1,-2,-4,-5,-24,-9,42,-27,-28,-29,-26,]),'NEWLINE':([6,7,8,9,11,14,19,26,27,28,29,30,31,34,35,40,44,47,48,49,50,52,53,],[-3,-10,-11,-12,-8,-6,-7,-30,-1,-2,-4,-5,-21,-23,-9,-22,-24,51,-32,-33,-24,54,-31,]),'TIMES':([6,11,14,19,27,28,29,30,35,],[22,-8,-6,-7,22,22,-4,-5,-9,]),'DIVIDE':([6,11,14,19,27,28,29,30,35,],[23,-8,-6,-7,23,23,-4,-5,-9,]),'EQUALS':([24,50,],[33,33,]),'COMMA':([32,37,38,39,41,45,],[-24,43,-27,-28,-29,-26,]),'LBRACE':([42,],[44,]),'RBRACE':([54,],[55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'expression':([0,12,13,33,],[2,25,26,40,]),'declaration':([0,44,51,],[3,48,53,]),'function_declaration':([0,],[4,]),'return_statement':([0,51,],[5,52,]),'term':([0,12,13,20,21,33,],[6,6,6,27,28,6,]),'type':([0,32,43,44,51,],[10,36,36,46,46,]),'factor':([0,12,13,20,21,22,23,33,],[14,14,14,14,14,29,30,14,]),'expression_opt':([24,50,],[31,31,]),'empty':([24,32,44,50,],[34,39,49,34,]),'parameter_list':([32,],[37,]),'parameter':([32,43,],[38,45,]),'declaration_list':([44,],[47,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintatico.py',89),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintatico.py',93),
  ('expression -> term','expression',1,'p_expression_term','sintatico.py',97),
  ('term -> term TIMES factor','term',3,'p_term_times','sintatico.py',101),
  ('term -> term DIVIDE factor','term',3,'p_term_div','sintatico.py',105),
  ('term -> factor','term',1,'p_term_factor','sintatico.py',109),
  ('factor -> NUM','factor',1,'p_factor_num','sintatico.py',113),
  ('factor -> ID','factor',1,'p_factor_id','sintatico.py',117),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintatico.py',121),
  ('expression -> STRING','expression',1,'p_expression_string','sintatico.py',126),
  ('expression -> TRUE','expression',1,'p_expression_boolean','sintatico.py',131),
  ('expression -> FALSE','expression',1,'p_expression_boolean','sintatico.py',132),
  ('start -> expression','start',1,'p_start','sintatico.py',159),
  ('start -> declaration','start',1,'p_start','sintatico.py',160),
  ('start -> function_declaration','start',1,'p_start','sintatico.py',161),
  ('start -> return_statement','start',1,'p_start','sintatico.py',162),
  ('type -> INT','type',1,'p_type_specifier','sintatico.py',167),
  ('type -> FLOAT','type',1,'p_type_specifier','sintatico.py',168),
  ('type -> STR','type',1,'p_type_specifier','sintatico.py',169),
  ('type -> BOOL','type',1,'p_type_specifier','sintatico.py',170),
  ('declaration -> type ID expression_opt','declaration',3,'p_declaration','sintatico.py',175),
  ('expression_opt -> EQUALS expression','expression_opt',2,'p_expression_opt','sintatico.py',185),
  ('expression_opt -> empty','expression_opt',1,'p_expression_opt','sintatico.py',186),
  ('empty -> <empty>','empty',0,'p_empty','sintatico.py',193),
  ('function_declaration -> type ID LPAREN parameter_list RPAREN LBRACE declaration_list NEWLINE return_statement NEWLINE RBRACE','function_declaration',11,'p_function_declaration','sintatico.py',197),
  ('parameter_list -> parameter_list COMMA parameter','parameter_list',3,'p_parameter_list','sintatico.py',203),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','sintatico.py',204),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','sintatico.py',205),
  ('parameter -> type ID','parameter',2,'p_parameter','sintatico.py',215),
  ('return_statement -> RETURN expression','return_statement',2,'p_return_statement','sintatico.py',220),
  ('declaration_list -> declaration_list NEWLINE declaration','declaration_list',3,'p_declaration_list','sintatico.py',224),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','sintatico.py',225),
  ('declaration_list -> empty','declaration_list',1,'p_declaration_list','sintatico.py',226),
]
