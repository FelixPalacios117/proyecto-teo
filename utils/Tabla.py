from utils.Nterminales import *

# int a,b;
# int a=0,b;
tablaLL1 = [
    [S, 'int', ['int', I, F]],
    [S, 'char', ['char', I, F]],
    [S, 'float', ['float', I, F]],
    [S, 'eof', ['eof']],
    [I, 'identificador', ['identificador', A]],
    [A, 'asignacion', ['asignacion', Z]],
    [A, 'coma', [F]],
    [A, 'puntocoma', [F]],
    [Z, 'number', ['number']],
    [Z, 'double', ['double']],
    [Z, 'character', ['character']],
    [F, 'identificador', None],
    [F, 'coma', ['coma', I, F]],
    [F, 'puntocoma', ['puntocoma', S]],
]
