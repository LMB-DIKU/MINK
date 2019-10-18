import ply.lex as lex

# tokens
tokens = (
    # typer
    'NUMBER',
    'DECIMAL',
    'STRING',

    # variabelnavne
    'ID',

    # operatorer
    'MINUS',
    'PLUS',
    'DIVIDE',
    'MULTIPLY',

    # højre og venstre parenteser (right vs left)
    'RPAR', 
    'LPAR'
)

# SEKTION 1: SIMPLE REGEX REGLER
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'/'
t_LPAR  = r'\('
t_RPAR  = r'\)'



