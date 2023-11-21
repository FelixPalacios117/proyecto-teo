from utils.Nterminales import *

# int a,b;
# int a=0,b;
# if(a==0)
# if(a<0) if(a<=0) if(a>=0)
tablaLL1 = [
    [S, 'int', ['int', I, F]],
    [S, 'char', ['char', I, F]],
    [S, 'float', ['float', I, F]],
    [S, 'identificador', [I, F, S]],
    [S, 'if', ['if', K]],
    [S, 'llaveder', ['llaveder', C, S]],
    [S, 'eof', ['eof']],
    # [S, 'llaveder', ['llaveder']],
    # S seria el bloque de codigo
    [K, 'parenizq', ['parenizq', E, 'parender', 'llaveizq', S]],
    [C, 'else', ['else', 'llaveizq', S, 'llaveder', S]],
    #[C, 'else', ['else', 'llaveizq', S, 'llaveder', S]],
    [C, 'if', ['if', K]],
    # esto posiblemente cambie al implementar toda la estructura base
    [C, 'eof', ['eof']],
    [E, 'identificador', ['identificador', OL, 'identificador']],
    # [E, T, [T, AR, T]],
    [OL, 'logico', ['logico']],
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
    # [F, 'puntocoma', ['puntocoma',S]],
]