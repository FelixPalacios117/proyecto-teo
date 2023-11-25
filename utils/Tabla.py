from utils.Nterminales import *

tablaLL1 = [
    [S, 'int', ['int', I, S]],
    [S, 'float', ['float', I, S]],
    [S, 'asignacion', None],
    [S, 'identificador', [I, S]],
    [S, 'eof', ['eof']],
    [S, 'puntocoma', None],
    [S, 'coma', None],
    # [I, 'identificador', ['identificador', A, S]],#
    [I, 'identificador', ['identificador', A]],
    [I, 'asignacion', None],
    [I, 'float', None],
    [I, 'int', None],
    [I, 'eof', ['eof', S]],  # ya veremos
    [A, 'asignacion', ['asignacion', T, A]],
    [A, 'parenizq', ['parenizq', E]],  # funcion
    [A, 'coma', ['coma', I]],
    [A, 'puntocoma', ['puntocoma']],
    [E, 'parender', [F]],  # funcion
    [E, 'identificador', ['identificador', OL, 'identificador', F]],  # funcion
    [F, 'parender', ['parender', 'llaveizq', B, S]],  # funcion
    [B, 'int', ['int', 'identificador', A, B]],
    [B, 'float', ['float', 'identificador', A, B]],
    [B, 'llaveder', ['llaveder']],
    [T, 'number', ['number']],
    [T, 'double', ['double']],
    [OL, 'logico', ['logico']],  # funcion
]
