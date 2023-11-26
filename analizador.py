import ply.lex as lex
from utils.reservadas import *
from utils.tokens import *
from utils.Nterminales import *  # No terminales
from utils.Tabla import tablaLL1


# fin del archivo
t_eof = r"\$"
# ignora tabs y espacios
t_ignore = " \t"

t_puntocoma = r"\;"
t_asignacion = r"\="
t_coma = r"\,"
t_parenizq = r'\('
t_parender = r'\)'
t_logico = r'(<=)|(<(?!<))|(>(?!>))'
t_for_or = r'\+\+|--'
t_llaveizq = r'\{'
# t_vacia= r'\'
t_llaveder = r'\}'


def t_character(t):
    r"'.'"
    return t

def t_define(t):
    r"\#define"
    return t

def t_include(t):
    r'\#include\s*[<"][^>"]+[>"]'
    return t
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_double(token):
    r"\d+\.\d+"
    token.value = float(token.value)
    return token


def t_number(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_int(t):
    r"(int)"
    return t


def t_if(t):
    r"(if)"
    return t


def t_for(t):
    r"(for)"
    return t


def t_else(t):
    r"(else)"
    return t


def t_float(token):
    r"(float)"
    return token


def t_char(token):
    r"(char)"
    return token

def t_void(token):
    r"(void)"
    return token

def t_identificador(token):
    r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*"
    return token


def t_reservada(token):
    r"(char)|(int)|(if)|(else)|(float)|(return)|(void)"
    return token


def t_comentario(t):
    r"\/\/.*"
    pass

# linea de comentario


def t_comentario_bloque(token):
    r'\/\*[\s\S]*?\*\/'
    pass

# Manejo de errores


def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)
    return token


stack = ["eof", 0]


def leer_fichero(txt):
    with open(txt, "r", encoding="utf8") as archivo:
        # Lee el contenido del archivo
        contenido = archivo.read()
    return contenido


lexer = lex.lex()


def parser(txt):
    lexer.input(str(leer_fichero(txt)+"\n $"))
    tok = lexer.token()
    errorFlag = False
    x = stack[-1]  # primer elemento de der a izq
    while True:
        print(tok)
        print(x)
        if x == tok.type and x == 'eof':
            print(stack.__len__())
            print(stack)
            print("\nAnálisis sintáctico terminado con errores\n") if errorFlag else print("\nAnálisis sintáctico terminado correctamente\n")
            #print("Cadena reconocida exitosamente")
            return  # aceptar
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x = stack[-1]
                tok = lexer.token()
            if x in tokens and x != tok.type:
                #print(tok)
                #print(x)
                print("\nError: se esperaba ", tok.type)
                print('en la posicion: ', tok.lexpos)
                print("en la línea: ", tok.lineno)
                """  while True :
                    tok = lexer.token()
                    if tok.type == x :
                        break  """
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
                print(tok.type)
                celda = buscar_en_tabla(x, tok.type)
                if celda is None:
                    print("\nError: NO se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos)
                    print("en la línea: ", tok.lineno)
                    errorFlag = True
                    stack.pop()
                    if(len(stack) != 0):
                        x = stack[-1]
                        tok = lexer.token() #thiss
                    else:
                        return 0 
                    #return 0
                else:
                    stack.pop()
                    agregar_pila(celda)
                    x = stack[-1]


def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tablaLL1)):
        if tablaLL1[i][0] == no_terminal and tablaLL1[i][1] == terminal:
            return tablaLL1[i][2]  # retorno la celda


def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != "vacia":  # la vacía no la inserta
            stack.append(elemento)


if __name__ == "__main__":
    print("\n")
    result = parser("./test/prueba.c")
    if result == 0:
        print("\nAnálisis sintáctico terminado con errores\n")
    # input("Presiona enter para salir")