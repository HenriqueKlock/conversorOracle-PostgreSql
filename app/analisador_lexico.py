import ply.lex as lex

reserved = {
    'DECLARE': 'DECLARE',
    'INTEGER': 'INTEGER',
    'CHAR': 'CHAR',
    'DATE': 'DATE',
    'VARCHAR2': 'VARCHAR2',
    'CURSOR': 'CURSOR',
    'IS': 'IS',
    'PRINT': 'PRINT',
    'DBMS_OUTPUT': 'DBMS_OUTPUT',
    'OR': 'OR',
    'IF': 'IF',
    'THEN': 'THEN',
    'END': 'END',
    'TRUNC': 'TRUNC',
    'INTO': 'INTO',
    'COUNT': 'COUNT',
    'SELECT': 'SELECT',
    'NVL': 'NVL',
    'MAX': 'MAX',
    'ELSIF': 'ELSIF',
    'CASE': 'CASE',
    'WHEN': 'WHEN',
    'TO_CHAR': 'TO_CHAR',
    'SYSDATE': 'SYSDATE',
    'FOR': 'FOR',
    'BEGIN': 'BEGIN',
    'IN': 'IN',
    'LOOP': 'LOOP'
}

# List of token names.   This is always required
tokens = [
             'ID',
             'NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'CONCAT',
             'EQUALS',
             'MAIOR',
             'MENOR',
             'MENORIGUAL',
             'MAIORIGUAL',
             'SEMICOLON',
             'COMMA'
         ] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CONCAT = r'\|\|'
t_EQUALS = r'\='
t_MAIOR = r'\>'
t_MENOR = r'\<'
t_MENORIGUAL = r'\<='
t_MAIORIGUAL = r'\<='
t_SEMICOLON = r';'
t_COMMA = r','
t_ignore = ' \t'

# Check for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    valor = t.value.upper()
    if valor in reserved:
        t.type = reserved[valor]
    return t


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# No return value. Token discarded
def t_COMMENT(t):
    r'\#.*'
    pass


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def inicia_analisador_lexico(data):
    lexer = lex.lex()
    lexer.input(data)
    lista = []
    for tok in lexer:
        lista.append(tok)
    return lista