# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN',
    'IF', 'THEN', 'ELSE', 'FI',
    'QUESTIONMARK', 'COLON',
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IF      = r'if\s'
t_THEN    = r'then\s'
t_ELSE    = r'else\s'
t_FI      = r'fi'
t_QUESTIONMARK = r'\?'
t_COLON   = r':'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])






def p_expression_bool(t):
    'BOOL : LPAREN expression EQUALS EQUALS expression RPAREN'
    t[0] = (t[2] == t[5])

def p_expression_booldiv(t):
    'expression : expression BOOL expression'
    if (t[2]):
        t[0] = t[1] / t[3]

# ERROR: Not working
def p_expression_if_else(t):
    'expression : IF BOOL THEN expression ELSE expression FI'
    if (t[2]):
        t[0] = t[4]
    else:
        t[0] = t[6]

# ERROR: Not working
def p_expression_if(t):
    'expression : IF BOOL THEN expression FI'
    if (t[2]):
        t[0] = t[4]

def p_expression_tenary_if(t):
    'expression : BOOL QUESTIONMARK expression COLON expression'
    if (t[1]):
        t[0] = t[3]
    else:
        t[0] = t[5]



def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
