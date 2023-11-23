from utils.Nterminales import *

# int a,b;
# int a=0,b;
# if(a==0)
# if(a<0) if(a<=0) if(a>=0)
tablaLL1 = [
    [S, 'int', ['int', I, F]],
    [S, 'char', ['char', I, F]],
    [S, 'float', ['float', I, F]],
    [S, 'void', ['void', I, F]],
    [S, 'identificador', [I, F]],
    [S, 'if', [K]],
    [S, 'llaveder', ['llaveder']],
    [S, 'for', ['for', B]],
    [S, 'while', ['while']],
    [S, 'eof', ['eof']],
    [B, 'parenizq', ['parenizq', E, 'parender', 'llaveizq', S, S]],
    # S seria el bloque de codigo
    [K, 'if', ['if', 'parenizq', E, 'parender',
               'llaveizq', S, 'else', 'llaveizq', S, S]],
    [E, 'identificador', ['identificador', OL, 'identificador']],
    [E, 'int', ['int', 'identificador', 'asignacion', 'number', 'puntocoma',
                'identificador', OL, 'number', 'puntocoma', 'identificador', 'for_or']],
    # [E, T, [T, AR, T]],
    [OL, 'logico', ['logico']],
    [I, 'identificador', ['identificador', A]],
    [A, 'asignacion', ['asignacion', T]],
    [A, 'parenizq', ['parenizq', FU, 'puntocoma', S]],  # declaracion de funciones
    [FU, 'int', ['int', FU]],
    [FU, 'float', ['float', FU]],
    [FU, 'char', ['char', FU]],
    [FU, 'parender', ['parender']],
    [FU, 'coma', ['coma', FU]],
    [A, 'coma', [F]],
    [A, 'puntocoma', [F]],
    [T, 'number', ['number']],
    [T, 'double', ['double']],
    [T, 'character', ['character']],
    [F, 'identificador', None],
    [F, 'coma', ['coma', I, F]],
    [F, 'puntocoma', ['puntocoma', S]],
    # [F, 'puntocoma', ['puntocoma',S]],
]