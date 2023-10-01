import ply.lex as lex
from utils.reservadas import reservadas
from utils.tokens import *

t_ignore=' \t'
t_mas=r'\+'
t_asignacion=r'='
t_menos=r'\-'
t_multiplicacion=r'\*'
t_division=r'/'
t_coma=r','
t_punto_y_coma=r';'
t_llave_izquierda=r'\{'
t_llave_derecha=r'\}'
t_parentesis_izquierdo=r'\('
t_parentesis_derecho=r'\)'
t_namespace=r'namespace'
t_insercion = r'<<'
t_extraccion = r'>>'

def t_char(token):
    r"'.'"
    return token
def t_string(token):
    r'"[^"]*"'
    return token
def t_bool(token):
    r'true|false'
    return token
# Manejo de saltos de línea
def t_salto_de_linea(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
#nombre de la variable
def t_identificador(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reservadas.get(token.value, 'identificador')
    return token
#comentario
def t_comentario(token):
    r'\/\/.*'
    return token
#linea de comentario
def t_linea_de_comentario(token):
    r'\/\*[\s\S]*?\*\/'
    return token
#Tipo double
def t_double(token):
    r'\d+\.\d+'
    token.value = float(token.value)
    return token
#enteros
def t_int(token):
    r'\d+'
    token.value=int(token.value)
    return token
#return
def t_return(token):
    r'return'
    return token
#Para incluir librerias
def t_inclusion(token):
    r'\#include\s+[<"][\w\.]+[>"]'
    token.type = reservadas.get(token.value, 'inclusion')
    return token
#El manejo de errores(simbolos que no pertenecen al lenguaje)
def t_error(t):
    print(f"Error léxico: '{t.value}'")
    t.lexer.skip(1)
# Crear el analizador léxico
lexer = lex.lex()
def leer_fichero():
    with open('./test/test.cpp', 'r') as archivo_cpp:
    # Lee el contenido del archivo
        contenido=archivo_cpp.read()
    return contenido
# correr lexer
if __name__ == '__main__':
    lexer.input(str(leer_fichero()))
    print('Archivo cargado correctamente')
    print('\n')
    print('Lista de tokens')
    print ('\n')
    while True:
        token = lexer.token()
        if not token:
           break
        print(f'Tipo: {token.type}, Valor: {token.value}')

