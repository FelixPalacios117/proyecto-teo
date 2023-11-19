import ply.lex as lex
from utils.reservadas import *
from utils.tokens import *
from utils.Nterminales import *  # No terminales
from utils.Tabla import tablaLL1


def t_salto_de_linea(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
def t_double(token):
    r'\d+\.\d+'
    token.value=float(token.value)
    return token
def t_number(t):
    r'\d+'
    t.value = int(t.value)  
    return t
def t_int(t):
    r'(int)'
    return t
def t_float(token):
    r'(float)'
    return token
def t_identificador(token):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return token

def t_reservada(token):
    r'(char)|(int)|(if)|(else)|(float)|(return)|(void)'
    return token

# ignora tabs y espacios
t_ignore=' \t'
# fin del archivo
t_eof = r'\$'
t_puntocoma = r'\;'
t_asignacion = r'\='
t_coma= r'\,'

def t_comentario(t):
    r'\/\/.*'

def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'

# Manejo de errores


def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)
    return token

stack = ['eof', 0]
lexer = lex.lex()
def leer_fichero(txt):
    with open(txt, 'r',encoding = "utf8") as archivo:
    # Lee el contenido del archivo
        contenido=archivo.read()
    return contenido
def parser(txt):
    #print(tokens)
    lexer.input(str(leer_fichero(txt))+'$')
    tok = lexer.token()
    errorFlag = False
    """ while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
    print(lexer)
    print('xxxx') """
    x = stack[-1]  # primer elemento de der a izq
    while True:
        #print(tok.type)
        #print(x)
        if x == tok.type and x == 'eof':
            print("\nAnálisis sintáctico terminado con errores\n") if errorFlag else print("\nAnálisis sintáctico terminado correctamente\n")
            #print("Cadena reconocida exitosamente")
            return  # aceptar
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x = stack[-1]
                tok = lexer.token()
            if x in tokens and x != tok.type:
                print(x)
                print(tok)
                print("\nError: se esperaba ", tok.type)
                print('en la posicion: ', tok.lexpos)
                print("en la línea: ", tok.lineno)
                errorFlag = True
                stack.pop()
                if(len(stack) != 0):
                    x = stack[-1]
                else:
                    return 0
                #return 0
            if x not in tokens:  # es no terminal
                print("van entrar a la tabla:")
                print(x)
                print(tok)
                celda = buscar_en_tabla(x, tok.type)
                if celda is None:
                    print("\nError: NO se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos)
                    print("en la línea: ", tok.lineno)
                    errorFlag = True
                    stack.pop()
                    if(len(stack) != 0):
                        x = stack[-1]
                        #tok = lexer.token()
                    else:
                        return 0
                    #return 0
                else:
                    stack.pop()
                    agregar_pila(celda)
                    x = stack[-1]

def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tablaLL1)):
        """  print(terminal)
        print(no_terminal)
        print(tablaLL1[i][0])
        print(tablaLL1[i][1]) """
        if (tablaLL1[i][0] == no_terminal and tablaLL1[i][1] == terminal):
            return tablaLL1[i][2]  # retorno la celda


def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia':  # la vacía no la inserta
            stack.append(elemento)


if __name__ == '__main__':
    # descomentar para testear con otro archivo de c
    # identificar_tokens(analizador,'./test/test.c')
    print('\n')
    parser('./test/prueba.c')
    #input("Presiona enter para salir")
