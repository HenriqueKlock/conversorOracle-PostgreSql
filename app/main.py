from app.analisador_lexico import inicia_analisador_lexico
from app.oracle import Oracle

data = '''
declare

  variavel INTEGER;

  CURSOR cur_pend IS

  dbms_output.put_line
  

BEGIN
  for x IN cur_pend loop

  END loop;
END;
'''

tokens = inicia_analisador_lexico(data)
oracle = Oracle()
declare = oracle.get_declare(tokens)
nome_cursor = oracle.get_declaracao_cursor(tokens)
inicia_script = oracle.get_inicia_script(tokens)
variavel_for = oracle.get_for_cursor(tokens, nome_cursor)

if declare:
    print('abriu o declare')
    if nome_cursor:
        print('Cursor: '+ nome_cursor + ' foi aberto')
        if inicia_script:
            print('iniciou')
            if variavel_for:
                print('Usando a variavek: '+variavel_for+ ' para iterar os resultados')