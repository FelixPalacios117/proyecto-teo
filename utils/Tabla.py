from utils.Nterminales import *
tablaLL1 = [
    [S, 'identificador', None],
    [S, 'int', ['int', I]],
    #[S, 'float', ['float', I]],
    [I, 'identificador', ['identificador', A]],
    [A, 'asignacion', ['asignacion', T,F]],
    #[T, 'double', ['double']],
    [T, 'number', ['number']],
    [F, 'identificador', ['identificado', I]],
    [F, 'coma', ['coma', I]],
    [F, 'puntocoma', ['puntocoma']],
    #[F, 'puntocoma', ['puntocoma',None]],
]