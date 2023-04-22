#Estado H: estado halt, estado final
#Caracteres especiais: '*', '_', '!', 'pare'

class MT:
    def __init__(self, input, arquivo):
        input = ''.join(['_']) + input + ''.join(['_'])
        self.dicionario = {}
        self.estado = '0'
        self.fita = list(input)
        self.cabeca = 1
        for linha in arquivo.splitlines():
            if ';' not in linha:
                estado_atual, simbolo_atual, novo_simbolo, movimento, novo_estado = linha.split(' ')
                #Tupla no formato:
                #<estado atual> <símbolo atual> - - <novo símbolo> <movimento> <novo estado>
                if len(estado_atual) > 4 and estado_atual != 'retorne':
                    print('Erro: o estado atual atingiu o limite de 4 digitos.')
                    print('Estado: ', estado_atual)
                    break
                if len(novo_estado) > 4 and novo_estado != 'retorne':
                    print('Erro: o novo estado atingiu o limite de 4 digitos.')
                    print('Estado: ', novo_estado)
                    break
                if movimento not in {'e', 'd', 'i'}:
                    print('Erro: caractere de movimento nao identificado.')
                    print('Movimento: ', movimento)
                    break
                self.dicionario[estado_atual, simbolo_atual] = (novo_simbolo, movimento, novo_estado)

    def teste(self):
        print(self.dicionario)
        print(self.fita)

    def passo(self):
        if self.estado != 'pare' or self.estado != 'retorne':
            for estado, simbolo in self.dicionario:
                if self.estado == estado and self.fita[self.cabeca] == simbolo:
                    novo_simbolo, movimento, novo_estado = self.dicionario[estado, simbolo]
                    self.estado = novo_estado
                    self.fita[self.cabeca] = novo_simbolo
                    #print(novo_simbolo, movimento, novo_estado)
                    print(simbolo)
                    if movimento == 'e':
                        self.cabeca -= 1
                    elif movimento == 'd':
                        self.cabeca += 1
                    elif movimento == 'i':
                        pass

    def programa(self):
        erro = 0
        #self.teste()
        while self.estado != 'pare' and erro < 10:
            self.passo()
            erro += 1


input = '11'
arquivo = open('programa.txt').read()
mt = MT(input, arquivo)
#mt.teste()
mt.programa()
