import ply.yacc as yacc # importerer parsing biblioteket

# præsedens og assosiation
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    
    )




# parsing
parser = yacc.yacc()