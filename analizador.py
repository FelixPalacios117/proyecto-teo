import ply.lex as lex
from utils.reservadas import reservadas
from utils.tokens import *


def t_identificador(token):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return token
def t_reservada(token):
    r'(char)|(int)|(if)|(else)|(float)|(return)|(void)'
    return token

#ignora tabs y espacios
t_ignore  = ' \t'

#Manejo de errores
def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)    
    return token
    
if __name__ == '__main__':
    ##descomentar para testear con otro archivo de c#
    ##identificar_tokens(analizador,'./test/test3.cs')
    ##identificar_tokens(analizador,'./test/test1.cs')
    #identificar_tokens(analizador,'./test/test2.cs')
    print('\n')
    input("Presiona enter para salir")
    