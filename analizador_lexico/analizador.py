import ply.lex as lex
from utils.reservadas import reservadas
from utils.tokens import *

#ignora espacios y tabs
t_ignore=' \t'
t_mas=r'\+'
t_asignacion=r'\='
t_menos=r'\-'
t_multiplicacion=r'\*'
t_menor_igual_que=r'\<='
t_mayor_igual_que=r'\>='
t_menor=r'\<'
t_mayor=r'\>'
t_division=r'/'
t_punto=r'\.'
t_coma=r'\,'
t_fin_de_instruccion=r'\;'
t_llave_de_inicio=r'\{'
t_acumulado=r'\+\+'
t_restar_acumulado=r'\-\-'
t_llave_de_cierre=r'\}'
t_parentesis_de_inicio=r'\('
t_parentesis_de_cierre=r'\)'
t_operador_y = r'\&\&'
t_negacion = r'\!'
t_distinto=r'\!='
t_operador_o = r'\|{2}'
t_modulo=r'%'

def t_bool(token):
    r'true|false'
    return token
# Manejo de saltos de línea
def t_salto_de_linea(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
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
def t_linea_comentario(token):
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
#El manejo de errores(simbolos que no pertenecen al lenguaje) solo se ignoran
def t_error(t):
    t.lexer.skip(1)
# Crear el analizador léxico
analizador = lex.lex()
def leer_fichero(txt):
    with open(txt, 'r',encoding = "utf8") as archivo_csharp:
    # Lee el contenido del archivo
        contenido=archivo_csharp.read()
    return contenido
# método para generar tabla de simbolos
def imprimir_tabla(tabla):
    encabezados = ("Linea", "Posicion", "Tipo", "Valor")
    # Imprimir encabezados
    print("| {:<10} | {:<10} | {:<25} | {:<35} |".format(*encabezados))
    print("|{:-<12}|{:-<12}|{:-<27}|{:-<37}|".format('', '', '', ''))

    for lexpos, data in tabla.items():
        fila = "| {:<10} | {:<10} | {:<25} | {:<35} |".format(
            data['Linea'], data['Posicion'], data['Tipo'], data['Valor'])
        print(fila)
def identificar_tokens(analizador,txt):
    print("\n")
    analizador.input(str(leer_fichero(txt)))
    print('Dirección del archivo cargado: '+txt)
    tabla_simbolos={}
    print('Lista de tokens....')
    print("\n")
    while True:
        token= analizador.token()
        if not token:
           break
        tabla_simbolos[token.lexpos]={
            'Linea':token.lineno,
            'Posicion':token.lexpos,
            'Tipo':token.type,
            'Valor':token.value
        }
        print("Linea {:6} Posicion: {:12} Tipo: {:24} Valor: {:40}".format(str(token.lineno), str(token.lexpos), str(token.type) ,str(token.value)))
    print("\n")
    print("Tabla de simbolos...")
    print("\n")
    imprimir_tabla(tabla_simbolos)
if __name__ == '__main__':
    ##descomentar para testear con otro archivo de c#
    ##identificar_tokens(analizador,'./test/test3.cs')
    ##identificar_tokens(analizador,'./test/test1.cs')
    identificar_tokens(analizador,'./test/test2.cs')
    print('\n')
    input("Presiona enter para salir")
    