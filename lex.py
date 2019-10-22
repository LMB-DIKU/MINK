import ply.lex as lex # importing the lexing library

# tokens navne
tokens = (
    # typer
    'NUMBER',
    'DECIMAL',
    'STRING',
    'BOOL',

    # variabelnavne
    'ID',

    # taloperatorer
    'MINUS',
    'PLUS',
    'DIVIDE',
    'MULTIPLY',

    #boolean operatorer
    'AND',
    'OR',
    'EQUALS',
    'NOT',

    # højre og venstre parenteser (right vs left)
    'RPAR', 
    'LPAR',

    # keywords
    'IF',
    'ELSE',
    'PRINT',

    # comment
    'COMM'

)

############ SEKTION 1: SIMPLE REGEX REGLER ############

# operatorer
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'/'
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_STRING = r'"[a-zA-Z0-9()!.,: ]*"'

# keywords
t_IF = r'if'
t_ELSE = r'else'
t_PRINT = r'print'


def t_error(t):
    print("Lexeren forstår ikke følgende tegn: {t}")

    t.lexer.skip(1) # springer ugyldigt tegn over

lexer = lex.lex()

#if (dfkjdfhskjdfj) {} else {}
