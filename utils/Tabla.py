from utils.Nterminales import *

# int a,b;
# int a=0,b;
# if(a==0)
# if(a<0) if(a<=0) if(a>=0)
tablaLL1 = [
    [S, 'int', ['int', I, F]],
    [S, 'char', ['char', I, F]],
    [S, 'float', ['float', I, F]],
    [S, 'identificador', [I, F]],
    [S, 'if', ['if', K]],
    [S, 'eof', ['eof']],
    #[C, 'if', ['if',S]],
    #[C, 'else', ['else', 'llaveizq', 'llaveder']],
    [K, 'parenizq', ['parenizq', E, 'parender', 'llaveizq', 'llaveder']],
    [E, 'identificador', ['identificador', AR, 'identificador']],
    # [E, T, [T, AR, T]],
    [AR, 'aritmetico', ['aritmetico']],
    [I, 'identificador', ['identificador', A]],
    [A, 'asignacion', ['asignacion', T]],
    [A, 'coma', [F]],
    [A, 'puntocoma', [F]],
    [T, 'number', ['number']],
    [T, 'double', ['double']],
    [T, 'character', ['character']],
    [F, 'identificador', None],
    [F, 'coma', ['coma', I, F]],
    [F, 'puntocoma', ['puntocoma', S]],
]
