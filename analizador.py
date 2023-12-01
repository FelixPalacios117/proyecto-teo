import ply.lex as lex
from utils.reservadas import *
from utils.tokens import *
from utils.Nterminales import *  # No terminales
from utils.Tabla import tabla


# fin del archivo
t_eof = r"\$"
# ignora tabs y espacios
t_ignore = " \t"
t_suma = r"\+"
t_resta = r"\-"
t_multiplicacion = r"\*"
t_division = r"/"
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


def t_return(token):
    r"(return)"
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
    token.lexer.skip(1)


stack = ["eof", 0]


def leer_fichero(txt):
    with open(txt, "r", encoding="utf8") as archivo:
        # Lee el contenido del archivo
        contenido = archivo.read()
    return contenido


lexer = lex.lex()
tabla_simbolos = {}
def parser(txt):
    hasErrors = False
    lexer.input(str(leer_fichero(txt)+"\n $"))
    tok = lexer.token()
    x = stack[-1]  # primer elemento de derecha a izquierda
    while True:
        if tok:
            tabla_simbolos[tok.lexpos] = {
            'Linea': tok.lineno,
            'Posicion': tok.lexpos,
            'Tipo': tok.type,
            'Valor': tok.value}
        if x == tok.type and x == 'eof':
            print("\nAnálisis sintáctico finalizado con errores\n") if hasErrors else print(
                "\nAnálisis sintáctico finalizado con exito\n")
            return  # se acepta
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x = stack[-1]
                tok = lexer.token()
            if x in tokens and x != tok.type:
                print("\nError: se esperaba ", tok.type)
                print('en la posicion: ', tok.lexpos)
                print("en la línea: ", tok.lineno)
                hasErrors = True
                stack.pop()
                if (len(stack) != 0):
                    x = stack[-1]
                else:
                    return 0
            if x not in tokens:  # el actual es no terminal
                celda = buscar_en_tabla(x, tok.type)
                if celda is None:
                    print("\nError: NO se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos)
                    print("en la línea: ", tok.lineno)
                    hasErrors = True
                    stack.pop()
                    if (len(stack) != 0):
                        x = stack[-1]
                        tok = lexer.token()  # continua leyendo aunque encuentre error
                    else:
                        return 0
                else:
                    stack.pop()
                    agregar_pila(celda)
                    x = stack[-1]

def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla)):
        if tabla[i][0] == no_terminal and tabla[i][1] == terminal:
            return tabla[i][2]  # retorno la celda


def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != "vacia":  # se ignora la vacia
            stack.append(elemento)


def imprimir_tabla(tabla):
    encabezados = ("Linea", "Posicion", "Tipo", "Valor")
    # Imprimir encabezados
    print("| {:<10} | {:<10} | {:<25} | {:<35} |".format(*encabezados))
    print("|{:-<12}|{:-<12}|{:-<27}|{:-<37}|".format('', '', '', ''))

    for lexpos, data in tabla.items():
        fila = "| {:<10} | {:<10} | {:<25} | {:<35} |".format(
            data['Linea'], data['Posicion'], data['Tipo'], data['Valor'])
        print(fila)


if __name__ == "__main__":
    print("\n")
    result = parser("./test/prueba.c")
    print("\n")
    print("Imprimiendo tabla de simbolos..")
    print("\n")
    imprimir_tabla(tabla_simbolos)
    if result == 0:
        print("\nAnálisis sintáctico finalizado con errores\n")
