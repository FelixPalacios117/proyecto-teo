from utils.Nterminales import *
#bug int a, 
tablaLL1 = [
    [S, 'int', ['int', I, S]],
    [S, 'float', ['float', I, S]],
    [S, 'asignacion', None],
    [S, 'identificador', [I, S]],
    [S, 'eof', ['eof']],
    [S, 'puntocoma', None],
    [S, 'llaveder', ['llaveder']],
    [S, 'coma', None],
    [S, 'for', ['for', BU]],
    [BU, 'for', None],
    [BU, 'int', None],
    [BU, 'parenizq', ['parenizq', EF]],  # for
    [EF, 'int', ['int', 'identificador', 'asignacion', 'number', 'puntocoma',
                 'identificador', OL, 'number', 'puntocoma', 'identificador', 'for_or', 'parender', 'llaveizq', B, S]],  # for]
    # [I, 'identificador', ['identificador', A, S]],#
    [I, 'identificador', ['identificador', A]],
    [I, 'asignacion', None],
    [I, 'float', None],
    [I, 'int', None],
    [I, 'coma', None],
    [I, 'puntocoma', None],
    [I, 'eof', None],
    # [I, 'eof', ['eof', S]],  # ya veremos
    [A, 'asignacion', ['asignacion', T, A]],
    [A, 'parenizq', ['parenizq', E]],  # funcion
    [A, 'coma', ['coma', I]],
    [A, 'puntocoma', ['puntocoma']],
    [E, 'parender', [F]],  # funcion

    # [E, 'identificador', ['identificador', OL, 'identificador', F]],  # if
    # parametros de funcion
    [E, 'int', ['int', 'identificador', E]],
    [E, 'coma', ['coma', E]],
    [E, 'float', ['float', 'identificador', E]],
    [E, 'char', ['char', 'identificador', E]],
    [F, 'parender', ['parender', 'llaveizq', B, S]],  # funcion
    [B, 'int', ['int', 'identificador', A, B]],
    [B, 'float', ['float', 'identificador', A, B]],
    [B, 'identificador', ['identificador', A, B]],
    [B, 'llaveder', ['llaveder']],
    [B, 'for', ['for', BU]],
    [B, 'eof', None],
    [T, 'number', ['number']],
    [T, 'double', ['double']],
    [T, 'int', None],
    [T, 'char', None],
    [T, 'float', None],
    [OL, 'logico', ['logico']],  # funcion
]
