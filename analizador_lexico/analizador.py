import ply.lex as lex
import re
from utils.reservadas import reservadas
from utils.tokens import tokens
tokens_list=tokens+list(reservadas.values())
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

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_id(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reservadas.get(token.value, 'id')
    return token
def t_comment(token):
    r'\/\/.*'
    pass
def comment_line_token(token):
    r'\/\*[\s\S]*?\*\/'
    pass
def identify_number(token):
    r'\d+'
    token.value=int(token.value)
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)
# Crear el analizador léxico
lexer = lex.lex()
#leer fichero cpp

def leer_fichero():
    with open('./test/test.cpp', 'r') as archivo_cpp:
    # Lee el contenido del archivo
        contenido=archivo_cpp.read()
    print(contenido)
    return contenido
# Ejemplo de uso
if __name__ == '__main__':
    lexer.input(str(leer_fichero()))
    print('archivo cargado')
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

