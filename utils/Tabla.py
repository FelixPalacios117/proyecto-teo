from utils.Nterminales import *
# bug int a,
# pendiente if, macros, inclusion, operacion de aritmeticos y revisar bien errores
tablaLL1 = [
    [S, 'int', ['int', I, S]],
    [S, 'float', ['float', I, S]],
    [S, 'char', ['char', I, S]],
    [S, 'asignacion', None],
    [S, 'identificador', [I, S]],
    [S, 'eof', ['eof']],
    [S, 'puntocoma', None],
    [S, 'llaveder', ['llaveder']],
    [S, 'if', ['if', C, S]],
    [S, 'llaveizq', None],
    [S, 'else', None],
    [S, 'coma', None],
    [S, 'for_or', None],
    [S, 'for', ['for', BU]],
    [S, 'parender', None],
    [S, 'parenizq', None],
    [C, 'parenizq', ['parenizq', EI, 'parender', 'llaveizq', B, EL, S]],  # if
    [C, 'for', None],
    [C, 'if', None],
    [C, 'parenizq', [S]],
    [C, 'eof', None],
    [EI, 'parender', None],
    [EI, 'identificador', ['identificador', OL, 'identificador']],
    [EL, 'if', ['if', C]],
    [EL, 'else', ['else', 'llaveizq', B, S]],
    [EL, 'eof', ['eof']],
    [BU, 'for', None],
    [BU, 'int', None],
    [BU, 'parenizq', ['parenizq', EF]],  # for
    # [BU, 'eof', ['eof']],
    [EF, 'int', ['int', 'identificador', 'asignacion', 'number', 'puntocoma',
                 'identificador', OL, 'number', 'puntocoma', 'identificador', 'for_or', 'parender', 'llaveizq', B, S]],  # for]
    # [I, 'identificador', ['identificador', A, S]],#
    [I, 'identificador', ['identificador', A]],
    [I, 'asignacion', None],
    [I, 'float', None],
    [I, 'int', None],
    [I, 'coma', None],
    [I, 'puntocoma', None],
    [I, 'logico', None],
    # [I, 'eof', [S]],
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
    [B, 'char', ['char', 'identificador', A, B]],
    [B, 'identificador', ['identificador', A, B]],
    [B, 'llaveder', ['llaveder']],
    [B, 'for', ['for', BU]],
    [B, 'eof', None],
    [T, 'number', ['number']],
    [T, 'double', ['double']],
    [T, 'character', ['character']],
    [T, 'int', None],
    [T, 'char', None],
    [T, 'float', None],
    [OL, 'logico', ['logico']],  # funcion
]
