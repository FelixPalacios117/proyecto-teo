import ply.lex as lex
from utils.reservadas import reservadas
from utils.tokens import *

#ignora espacios y tabs
t_ignore=' \t'
t_mas=r'\+'
t_asignacion=r'\='
t_menos=r'\-'
t_multiplicacion=r'\*'
t_insercion = r'<<'
t_extraccion = r'>>'
t_menor=r'\<'
t_mayor=r'\>'
t_division=r'/'
t_coma=r'\,'
t_fin_instruccion=r'\;'
t_llave_de_inicio=r'\{'
t_llave_de_cierre=r'\}'
t_parentesis_de_inicio=r'\('
t_parentesis_de_cierre=r'\)'
t_namespace=r'namespace'

def t_char(token):
    r"'.'"
    return token
def t_bool(token):
    r'true|false'
    return token
# Manejo de saltos de línea
def t_salto_de_linea(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
#incluir librerias
""" def t_libreria(token):
    r'[<"][\w\.]+[>"]'
    return token """
def t_include(token):
    r'\#include'
    return token
def t_string(token):
    r'"[^"]*"'
    return token
#nombre de la variable
def t_identificador(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reservadas.get(token.value, 'identificador')
    return token
#comentario
def t_comentario(token):
    r'\/\/.*'
    pass
#linea de comentario
def t_linea_de_comentario(token):
    r'\/\*[\s\S]*?\*\/'
    pass
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
""" def t_libreria_incluida(token):
    r'\#include\s+[<"][\w\.]+[>"]'
    token.type = reservadas.get(token.value, 'libreria_incluida')
    return token """
#El manejo de errores(simbolos que no pertenecen al lenguaje)
def t_error(t):
    """ print("\n")
    print("* Error, el token {} no es válido en la linea {} *".format(str(t.value[0]),str(t.lineno)))
    print("\n") """
    t.lexer.skip(1)
# Crear el analizador léxico
analizador = lex.lex()
def leer_fichero():
    with open('./test/test.cpp', 'r') as archivo_cpp:
    # Lee el contenido del archivo
        contenido=archivo_cpp.read()
    return contenido
# correr lexer
if __name__ == '__main__':
    analizador.input(str(leer_fichero()))
    print('Archivo cargado correctamente')
    print('\n')
    print('Lista de tokens')
    print ('\n')
    while True:
        token= analizador.token()
        if not token:
           break
        print("Linea {:6} Posicion: {:12} Tipo: {:24} Valor: {:30}".format(str(token.lineno), str(token.lexpos), str(token.type) ,str(token.value)))

