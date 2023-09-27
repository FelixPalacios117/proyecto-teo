import ply.lex as lex
import re
import sys
import os
import codecs
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
t_leftparent=r'\('
t_rightparent=r'\)'

def id_token(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if token.value.upper() in reservadas:
        token.value=token.value.upper()
        token.type=token.value
    return token
def comment_token(token):
    r'\/\/.*'
    pass
def comment_line_token(token):
    r'\/\*[\s\S]*?\*\/'
    pass
def identify_number(token):
    r'\d+'
    token.value=int(token.value)
def t_error(t):
    print(f"Error léxico: Caracter inesperado '{t.value[0]}'")
    t.lexer.skip(1)
# Crear el analizador léxico
lexer = lex.lex()

# Ejemplo de uso
if __name__ == '__main__':
    data = "int main() { return 0; }"
    lexer.input(data)
    print('ok')
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

