from utils.Nterminales import *

tablaLL1 = [
    [S, 'int', ['int', I, S]],
    [S, 'asignacion', None],
    [S, 'identificador', [I, S]],
    [S, 'eof', ['eof']],
    [I, 'identificador', ['identificador', A, S]],
    [I, 'asignacion', None],
    [I, 'float', None],
    [I, 'eof', ['eof']],
    [A, 'asignacion', ['asignacion', IN, A]],
    [A, 'coma', ['coma', I]],
    [A, 'puntocoma', ['puntocoma']],
    [IN, 'number', ['number']]
]
