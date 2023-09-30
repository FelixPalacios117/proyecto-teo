import ply.lex as lex
import re
from utils.reservadas import reservadas
from utils.tokens import *

##tokens=tokens+list(reservadas.values())
t_ignore=' \t'
t_plus=r'\+'
t_assign=r'='
t_minus=r'\-'
t_multiplication=r'\*'
t_division=r'/'
t_comma=r','
t_semicolon=r';'
t_leftkey=r'\{'
t_rightkey=r'\}'
t_leftparent=r'\('
t_rightparent=r'\)'
t_namespace=r'namespace'
# Manejo de saltos de línea
def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
def t_id(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reservadas.get(token.value, 'id')
    return token
def t_comment(token):
    r'\/\/.*'
    return token
def t_comment_line(token):
    r'\/\*[\s\S]*?\*\/'
    return token
def t_int(token):
    r'\d+'
    token.value=int(token.value)
def t_float(token):
    r'\d+(\.\d+)?'
    token.value = float(token.value)
    return token
def t_return(token):
    r'return\s+\d+;'
    return token
def t_include(token):
    r'\#include\s+[<"][\w\.]+[>"]'
    token.type = reservadas.get(token.value, 'include')
    return token
def t_error(t):
    print(f"Error léxico: '{t.value}'")
    t.lexer.skip(1)
# Crear el analizador léxico
lexer = lex.lex()
def leer_fichero():
    with open('./test/test.cpp', 'r') as archivo_cpp:
    # Lee el contenido del archivo
        contenido=archivo_cpp.read()
    print(contenido)
    return contenido
# correr lexer
if __name__ == '__main__':
    lexer.input(str(leer_fichero()))
    print('archivo cargado')
    while True:
        token = lexer.token()
        if not token:
           break
        print(f'Tipo: {token.type}, Valor: {token.value}')

