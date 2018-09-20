class Oracle:

    def gera_codigo_posicao(self, tokens):
        posicao_token = []
        for token in range(len(tokens)):
            posicao_token.append(int(str(tokens[token].lineno)+str(tokens[token].lexpos)))
        return posicao_token

    def get_declare(self, tokens):
        for token in range(len(tokens)):
            if tokens[token].value.upper() == 'DECLARE':
                return True
            else:
                return False

    def get_declaracao_cursor(self, tokens):
        for token in range(len(tokens)):
            if tokens[token].value.upper() == 'CURSOR':
                if tokens[token+1].type == 'ID':
                    nome_cursor = tokens[token+1].value.upper()
                    if tokens[token+2].value.upper() == 'IS':
                        return nome_cursor

    def get_inicia_script(self, tokens):
        posicao_begin = 0
        posicao_token = self.gera_codigo_posicao(tokens)
        for token in range(len(tokens)):
            if tokens[token].value == 'BEGIN':
                posicao_begin = posicao_token[token]
            if posicao_begin:
                if tokens[token].value == 'END':
                    if tokens[token+1].value == ';':
                        return True

    def get_for_cursor(self, tokens, nome_cursor):
        posicao_for = 0
        posicao_token = self.gera_codigo_posicao(tokens)
        for token in range(len(tokens)):
            if tokens[token].value.upper() == 'FOR':
                if tokens[token + 1].type.upper() == 'ID':
                    variavel_for = tokens[token+1].value
                    if tokens[token + 2].value.upper() == 'IN':
                        if tokens[token + 3].value.upper() == nome_cursor:
                            if tokens[token + 4].type.upper() == 'LOOP':
                                posicao_for = posicao_token[token]
            if posicao_for:
                if tokens[token].value.upper() == 'END':
                    if tokens[token + 1].value.upper() == 'LOOP':
                        if tokens[token + 2].value.upper() == ';':
                            return variavel_for