class Pessoa:
    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao
        self.genero = genero

def salvar_dados(self):
        nome = input_nome.value.strip()

        if nome:
            lista_dados.append(nome)
            input_nome.error = None
            input_nome.value = ""
        else:
            input_nome.error = "Campo Obrigatório"