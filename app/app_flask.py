from flask import Flask, render_template, url_for, request
from app.analisador_lexico import inicia_analisador_lexico
from app.oracle import Oracle

app = Flask(__name__)
oracle = Oracle()

@app.route('/inicio')
def index():
    return render_template('index.html', titulo='Bem Vindo')

@app.route('/converter', methods=['POST',])
def converter():
    data = request.form['text_entrada']
    # data = '''
    # DECLARE
    #
    #   variavel INTEGER;
    #
    #   CURSOR cur_pend IS
    #
    #   dbms_outputput_line
    #
    # BEGIN
    #   FOR x IN cur_pend loop
    #
    #
    #   END loop;
    # END;
    # '''
    tokens = inicia_analisador_lexico(data)
    declare = oracle.get_declare(tokens)
    nome_cursor = oracle.get_declaracao_cursor(tokens)
    inicia_script = oracle.get_inicia_script(tokens)
    variavel_for = oracle.get_for_cursor(tokens, nome_cursor)

    if declare:
        print('abriu o declare')
        if nome_cursor:
            print('Cursor: ' + nome_cursor + ' foi aberto')
            if inicia_script:
                print('iniciou')
                if variavel_for:
                    print('Usando a variavek: ' + variavel_for + ' para iterar os resultados')
                    return render_template('index.html', titulo='Pronto', texto=declare)
    return render_template('index.html', titulo='Pronto', texto='nao deu')

app.run(debug=True)