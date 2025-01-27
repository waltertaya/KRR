
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIVIDE ELSE EQUAL GREATER ID IF LESS LPAREN MINUS NUMBER PLUS RPAREN TIMES WHILEprogram : statement_liststatement_list : statement\n                      | statement_list statementstatement : expression_statement\n                 | conditional_statement\n                 | loop_statementexpression_statement : ID ASSIGN expressionexpression : expression LESS term\n                  | expression GREATER term\n                  | expression EQUAL termexpression : expression PLUS term\n                  | expression MINUS termexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBERfactor : IDconditional_statement : IF expression statement ELSE statement\n                             | IF expression statementloop_statement : WHILE expression statement'
    
_lr_action_items = {'ID':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[7,7,-2,-4,-5,-6,16,16,-3,16,7,-13,-16,-17,-18,7,-7,-20,16,16,16,16,16,16,16,-21,7,-8,-9,-10,-11,-12,-14,-15,-19,]),'IF':([0,2,3,4,5,6,10,12,13,14,15,16,17,18,19,27,28,29,30,31,32,33,34,35,36,],[8,8,-2,-4,-5,-6,-3,8,-13,-16,-17,-18,8,-7,-20,-21,8,-8,-9,-10,-11,-12,-14,-15,-19,]),'WHILE':([0,2,3,4,5,6,10,12,13,14,15,16,17,18,19,27,28,29,30,31,32,33,34,35,36,],[9,9,-2,-4,-5,-6,-3,9,-13,-16,-17,-18,9,-7,-20,-21,9,-8,-9,-10,-11,-12,-14,-15,-19,]),'$end':([1,2,3,4,5,6,10,13,14,15,16,18,19,27,29,30,31,32,33,34,35,36,],[0,-1,-2,-4,-5,-6,-3,-13,-16,-17,-18,-7,-20,-21,-8,-9,-10,-11,-12,-14,-15,-19,]),'ELSE':([4,5,6,13,14,15,16,18,19,27,29,30,31,32,33,34,35,36,],[-4,-5,-6,-13,-16,-17,-18,-7,28,-21,-8,-9,-10,-11,-12,-14,-15,-19,]),'ASSIGN':([7,],[11,]),'NUMBER':([8,9,11,20,21,22,23,24,25,26,],[15,15,15,15,15,15,15,15,15,15,]),'LESS':([12,13,14,15,16,17,18,29,30,31,32,33,34,35,],[20,-13,-16,-17,-18,20,20,-8,-9,-10,-11,-12,-14,-15,]),'GREATER':([12,13,14,15,16,17,18,29,30,31,32,33,34,35,],[21,-13,-16,-17,-18,21,21,-8,-9,-10,-11,-12,-14,-15,]),'EQUAL':([12,13,14,15,16,17,18,29,30,31,32,33,34,35,],[22,-13,-16,-17,-18,22,22,-8,-9,-10,-11,-12,-14,-15,]),'PLUS':([12,13,14,15,16,17,18,29,30,31,32,33,34,35,],[23,-13,-16,-17,-18,23,23,-8,-9,-10,-11,-12,-14,-15,]),'MINUS':([12,13,14,15,16,17,18,29,30,31,32,33,34,35,],[24,-13,-16,-17,-18,24,24,-8,-9,-10,-11,-12,-14,-15,]),'TIMES':([13,14,15,16,29,30,31,32,33,34,35,],[25,-16,-17,-18,25,25,25,25,25,-14,-15,]),'DIVIDE':([13,14,15,16,29,30,31,32,33,34,35,],[26,-16,-17,-18,26,26,26,26,26,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,12,17,28,],[3,10,19,27,36,]),'expression_statement':([0,2,12,17,28,],[4,4,4,4,4,]),'conditional_statement':([0,2,12,17,28,],[5,5,5,5,5,]),'loop_statement':([0,2,12,17,28,],[6,6,6,6,6,]),'expression':([8,9,11,],[12,17,18,]),'term':([8,9,11,20,21,22,23,24,],[13,13,13,29,30,31,32,33,]),'factor':([8,9,11,20,21,22,23,24,25,26,],[14,14,14,14,14,14,14,14,34,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','zara_parser_with_translation.py',18),
  ('statement_list -> statement','statement_list',1,'p_statement_list','zara_parser_with_translation.py',22),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','zara_parser_with_translation.py',23),
  ('statement -> expression_statement','statement',1,'p_statement','zara_parser_with_translation.py',30),
  ('statement -> conditional_statement','statement',1,'p_statement','zara_parser_with_translation.py',31),
  ('statement -> loop_statement','statement',1,'p_statement','zara_parser_with_translation.py',32),
  ('expression_statement -> ID ASSIGN expression','expression_statement',3,'p_expression_statement','zara_parser_with_translation.py',36),
  ('expression -> expression LESS term','expression',3,'p_expression_relational','zara_parser_with_translation.py',44),
  ('expression -> expression GREATER term','expression',3,'p_expression_relational','zara_parser_with_translation.py',45),
  ('expression -> expression EQUAL term','expression',3,'p_expression_relational','zara_parser_with_translation.py',46),
  ('expression -> expression PLUS term','expression',3,'p_expression','zara_parser_with_translation.py',55),
  ('expression -> expression MINUS term','expression',3,'p_expression','zara_parser_with_translation.py',56),
  ('expression -> term','expression',1,'p_expression_term','zara_parser_with_translation.py',64),
  ('term -> term TIMES factor','term',3,'p_term','zara_parser_with_translation.py',68),
  ('term -> term DIVIDE factor','term',3,'p_term','zara_parser_with_translation.py',69),
  ('term -> factor','term',1,'p_term_factor','zara_parser_with_translation.py',77),
  ('factor -> NUMBER','factor',1,'p_factor_number','zara_parser_with_translation.py',81),
  ('factor -> ID','factor',1,'p_factor_id','zara_parser_with_translation.py',85),
  ('conditional_statement -> IF expression statement ELSE statement','conditional_statement',5,'p_conditional_statement','zara_parser_with_translation.py',90),
  ('conditional_statement -> IF expression statement','conditional_statement',3,'p_conditional_statement','zara_parser_with_translation.py',91),
  ('loop_statement -> WHILE expression statement','loop_statement',3,'p_loop_statement','zara_parser_with_translation.py',106),
]
