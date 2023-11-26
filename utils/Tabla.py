from utils.Nterminales import *
# declaracion de funciones ok
# pendiente if ok,
# bug int a,
# return
# funcion void
# macros, inclusion, operacion de aritmeticos y revisar bien errores
tablaLL1 = [
    # inclusion
    [S, 'int', ['int', I, S]],
    [S, 'float', ['float', I, S]],
    [S, 'char', ['char', I, S]],
    [S, 'asignacion', None],
    [S, 'define', ['define', ID, S]],
    [S, 'include', ['include', S]],
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
    # identificadores
    [I, 'identificador', ['identificador', A]],
    [I, 'include', None],
    [I, 'asignacion', None],
    [I, 'float', None],
    [I, 'int', None],
    [I, 'coma', None],
    [I, 'puntocoma', None],
    [I, 'logico', None],
    [I, 'double', None],
    [I, 'char', None],
    [I, 'number', None],
    [I, 'character', None],
    [I, 'for_or', None],
    [I, 'parender', None],
    [I, 'parenizq', None],
    [I, 'llaveizq', None],
    [I, 'llaveder', None],
    [I, 'for', None],
    [I, 'if', None],
    [I, 'else', None],
    [I, 'void', None],
    # asignar
    [A, 'asignacion', ['asignacion', T, A]],
    [A, 'parenizq', ['parenizq', E]],  # usado para funciones
    [A, 'coma', ['coma', I]],
    [A, 'puntocoma', ['puntocoma']],
    [A, 'include', None],
    [A, 'int', None],
    [A, 'for', None],
    [A, 'if', None],
    [A, 'else', None],
    [A, 'llaveizq', None],
    [A, 'parender', None],
    [A, 'llaveder', None],
    [A, 'logico', None],
    [A, 'double', None],
    [A, 'char', None],
    [A, 'number', None],
    [A, 'character', None],
    [A, 'for_or', None],
    [A, 'identificador', None],
    [A, 'float', None],
    [A, 'void', None],
    [T, 'number', ['number']],
    [T, 'double', ['double']],
    [T, 'character', ['character']],
    [T, 'int', None],
    [T, 'char', None],
    [T, 'float', None],
    [T, 'eof', None],
    [T, 'for', None],
    [T, 'if', None],
    [T, 'else', None],
    [T, 'asignacion', None],
    [T, 'define', None],
    [T, 'llaveizq', None],
    [T, 'llaveder', None],
    [T, 'parender', None],
    [T, 'parenizq', None],
    [T, 'coma', None],
    [T, 'for_or', None],
    [T, 'logico', None],
    [T, 'void', None],
    [T, 'puntocoma', None],
    [T, 'identificador', None],
    # usado en funciones para definir bloque
    [F, 'parender', ['parender', 'llaveizq', B, S]],
    [F, 'number', ['number']],
    [F, 'double', ['double']],
    [F, 'character', ['character']],
    [F, 'int', None],
    [F, 'char', None],
    [F, 'float', None],
    [F, 'eof', None],
    [F, 'for', None],
    [F, 'if', None],
    [F, 'else', None],
    [F, 'asignacion', None],
    [F, 'define', None],
    [F, 'llaveizq', None],
    [F, 'llaveder', None],
    [F, 'parenizq', None],
    [F, 'coma', None],
    [F, 'for_or', None],
    [F, 'logico', None],
    [F, 'void', None],
    [F, 'puntocoma', None],
    [F, 'identificador', None],
    # usado en parametros de funciones
    [E, 'int', ['int', EF]],
    [E, 'coma', ['coma', E]],
    [E, 'float', ['float', EF]],
    [E, 'char', ['char', EF]],
    [E, 'number', None],
    [E, 'character', None],
    [E, 'double', None],
    [E, 'eof', None],
    [E, 'for', None],
    [E, 'if', None],
    [E, 'else', None],
    [E, 'asignacion', None],
    [E, 'define', None],
    [E, 'llaveizq', None],
    [E, 'llaveder', None],
    [E, 'parenizq', None],
    [E, 'parender', None],
    [E, 'for_or', None],
    [E, 'logico', None],
    [E, 'void', None],
    [E, 'puntocoma', None],
    [E, 'identificador', None],
    # Bloques usados en funciones, if, for
    [B, 'int', ['int', 'identificador', A, B]],
    [B, 'float', ['float', 'identificador', A, B]],
    [B, 'char', ['char', 'identificador', A, B]],
    [B, 'identificador', ['identificador', A, B]],
    [B, 'llaveder', ['llaveder']],
    [B, 'for', ['for', BU]],
    [B, 'if', ['if', C]],
    [B, 'eof', None],
    [B, 'number', None],
    [B, 'character', None],
    [B, 'double', None],
    [B, 'logico', None],
    [B, 'for_or', None],
    [B, 'void', None],
    [B, 'llaveizq', None],
    [B, 'parender', None],
    [B, 'parenizq', None],
    [B, 'else', None],
    [B, 'define', None],
    [B, 'coma', None],
    [B, 'puntocoma', None],
    [B, 'include', None],
    # usado para definir la estructura de un if,if-else
    [C, 'parenizq', ['parenizq', EI, 'parender', 'llaveizq', B, EL, S]],  # if
    [C, 'for', None],
    [C, 'int', None],
    [C, 'double', None],
    [C, 'char', None],
    [C, 'if', None],
    [C, 'eof', None],
    [C, 'number', None],
    [C, 'character', None],
    [C, 'float', None],
    [C, 'logico', None],
    [C, 'for_or', None],
    [C, 'void', None],
    [C, 'llaveizq', None],
    [C, 'llaveder', None],
    [C, 'parender', None],
    [C, 'else', None],
    [C, 'define', None],
    [C, 'coma', None],
    [C, 'puntocoma', None],
    [C, 'include', None],
    # Expresion valida o condicion dentro del if
    [EI, 'parender', None],
    [EI, 'identificador', ['identificador', OL, 'identificador']],
    [EI, 'for', None],
    [EI, 'int', None],
    [EI, 'double', None],
    [EI, 'char', None],
    [EI, 'if', None],
    [EI, 'eof', None],
    [EI, 'number', None],
    [EI, 'character', None],
    [EI, 'float', None],
    [EI, 'logico', None],
    [EI, 'for_or', None],
    [EI, 'void', None],
    [EI, 'llaveizq', None],
    [EI, 'parenizq', None],
    [EI, 'llaveder', None],
    [EI, 'else', None],
    [EI, 'define', None],
    [EI, 'coma', None],
    [EI, 'puntocoma', None],
    [EI, 'include', None],
    #Operador logico
    [OL, 'logico', ['logico']],  # funcion
    [OL, 'parender', None],
    [OL, 'identificador', None],
    [OL, 'for', None],
    [OL, 'int', None],
    [OL, 'double', None],
    [OL, 'char', None],
    [OL, 'if', None],
    [OL, 'eof', None],
    [OL, 'number', None],
    [OL, 'character', None],
    [OL, 'float', None],
    [OL, 'for_or', None],
    [OL, 'void', None],
    [OL, 'llaveizq', None],
    [OL, 'parenizq', None],
    [OL, 'llaveder', None],
    [OL, 'else', None],
    [OL, 'define', None],
    [OL, 'coma', None],
    [OL, 'puntocoma', None],
    [OL, 'include', None],
    # definicion macros para constantes simbolicas
    [ID, 'identificador', ['identificador', T]],
    [ID, 'int', None],
    [ID, 'float', None],
    [ID, 'eof', None],
    [ID, 'char', None],
    [ID, 'for', None],
    [ID, 'if', None],
    [ID, 'else', None],
    [ID, 'asignacion', None],
    [ID, 'define', None],
    [ID, 'llaveizq', None],
    [ID, 'llaveder', None],
    [ID, 'parender', None],
    [ID, 'parenizq', None],
    [ID, 'coma', None],
    [ID, 'for_or', None],
    [ID, 'logico', None],
    [ID, 'number', None],
    [ID, 'character', None],
    [ID, 'double', None],
    [ID, 'void', None],
    [ID, 'puntocoma', None],


    [EL, 'if', ['if', C]],
    [EL, 'else', ['else', 'llaveizq', B, S]],
    [EL, 'llaveder', ['llaveder']],
    [EL, 'char', [S]],
    [EL, 'int', [S]],
    [EL, 'float', [S]],
    [EL, 'for', [S]],
    [EL, 'eof', ['eof']],
    [BU, 'for', None],
    [BU, 'int', None],
    [BU, 'parenizq', ['parenizq', EF]],  # for
    # [BU, 'eof', ['eof']],
    [EF, 'int', ['int', 'identificador', 'asignacion', 'number', 'puntocoma',
                 'identificador', OL, 'number', 'puntocoma', 'identificador', 'for_or', 'parender', 'llaveizq', B, S]],  # for]
    # [I, 'identificador', ['identificador', A, S]],#

    # [I, 'eof', [S]],
    # [I, 'eof', ['eof', S]],  # ya veremos

    # [E, 'parender', [F]],  # funcion

    # [E, 'identificador', ['identificador', OL, 'identificador', F]],  # if
    # parametros de funcion

    [EF, 'coma', ['coma', TI, EF]],
    [EF, 'identificador', ['identificador', DF]],
    [EF, 'parender', ['parender', 'puntocoma', S]],
    [DF, 'coma', ['coma', TI, 'identificador', DF]],
    [DF, 'parender', [F]],
    [DF, 'int', None],
    [DF, 'float', None],
    [DF, 'char', None],
    [DF, 'identificador', None],
    [DF, 'llaveizq', None],
    [DF, 'llaveder', None],
    [TI, 'int', ['int']],
    [TI, 'char', ['char']],
    [TI, 'float', ['float']],
    [TI, 'for', None],
    [TI, 'if', None],
    [TI, 'identificador', None],




]
