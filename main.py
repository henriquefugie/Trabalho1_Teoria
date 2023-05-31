# Joao Vitor Dias Fernandes e Henrique Fugie

class NoPilha:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

# Executar programa pelo terminal
import argparse

parser = argparse.ArgumentParser(description='Simulador de Máquina de Turing')
parser.add_argument('programa', help='Nome do arquivo que contém o código da MT')
parser.add_argument('-resume', '-r', action='store_true', help='Executa o programa até o fim e imprime o conteúdo final na fita')
parser.add_argument('-verbose', '-v', action='store_true', help='Mostra a execução passo a passo do programa até o fim')
parser.add_argument('-step', '-s', type=int, help='Mostra n linhas de execução passo a passo na tela')
args = parser.parse_args()

with open(args.programa, 'r') as file:
    codigo_mt = file.read()

print('Simulador de Máquina de Turing v1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação')
print('Autores: Joao Vitor Dias Fernandes & Henrique Fugie\n')

palavra_inicial = input('Forneça a palavra inicial: ')

step_value = args.step
programa_value = args.programa

if args.resume:
    print("Executando a opcao resume")

if args.verbose:
    print("Executando a opcao verbose")

if args.step:
    print("Executando a opcao step")
    print("Quantidade de steps:", step_value)

class MT:
    def __init__(self, input, arquivo):
        self.simbolo = input[0]
        input = ''.join(['_____________________']) + input + \
            ''.join(['____________________'])
        self.dicionario = {}
        # Lembrete, self.estado diz em qual linha o programa vai comecar do main
        # Tem que arrumar isso
        self.estado = '1'
        self.fita = list(input)
        self.cabeca = 21
        self.linha_atual = 0
        self.bloco = 'main'
        self.verificaFim = None
        self.blocos = {}
        self.chama_bloco = 'main'
        self.fimArquivo = True
        self.linhasArquivo_array = arquivo.splitlines()
        self.topo_pilha = None
        self.bloco_pilha = 'main'
        while self.fimArquivo:
            if self.linha_atual == len(self.linhasArquivo_array):
                self.fimArquivo = False
            elif self.linha_atual < len(self.linhasArquivo_array):
                valores_linha = self.linhasArquivo_array[self.linha_atual].split(
                    ' ')
                #print(valores_linha)
                #print(len(valores_linha))
                # Se nao for comentario
                if valores_linha[0] != ';':
                    # BLOCO
                    if len(valores_linha) == 3:
                        if valores_linha[0] == 'bloco':
                            self.verificaFim = (
                                valores_linha[1], self.linha_atual)

                            self.chama_bloco = valores_linha[1]
                            # Armazena o nome do bloco, onde comeca o estado do bloco e a linha do bloco
                            self.blocos[valores_linha[1]] = (
                                valores_linha[2], self.linha_atual)
                            # print(self.blocos)
                            # print(self.bloco)
                            # print(self.blocos)
                        elif valores_linha[0] == 'fim':
                            # TODO
                            # print(self.linha_atual)
                            # print(self.blocos)
                            # print(self.verificaFim)
                            """linha_fim = self.linha_atual - self.verificaFim[1]
                            for linha in range(linha_fim):
                                self.dicionario[(self.verificaFim[0], estado_atual)] = (linha + self.verificaFim[1], valores_linha[1], novo_estado)
                                #print(linha + self.verificaFim[1])
                            #print(linha_fim)"""
                            pass
                        # Entra aqui quando for mandado para outro bloco
                        # Exemplo: 10 moveFim 11
                        else:
                            # print(self.blocos[valores_linha[1]])
                            # print(valores_linha)
                            #print(self.chama_bloco, valores_linha[0],self.linha_atual, valores_linha[1], novo_estado)
                            # print(estado_atual)
                            """ARRUMAR NOVO_ESTADO"""

                            self.dicionario[self.chama_bloco, valores_linha[0]] = (
                                valores_linha[2], valores_linha[1], 1)
                            # print(valores_linha)
                    if len(valores_linha) == 6:
                        # print(self.verificaFim)
                        estado_atual, simbolo_atual, traco, novo_simbolo, movimento, novo_estado = valores_linha
                        # Tupla no formato:
                        # <estado atual> <símbolo atual> - - <novo símbolo> <movimento> <novo estado>
                        if len(estado_atual) > 4 and estado_atual != 'retorne':
                            print(
                                'Erro: o estado atual atingiu o limite de 4 digitos.')
                            print('Estado: ', estado_atual)
                            break
                        if len(novo_estado) > 4 and novo_estado != 'retorne':
                            print(
                                'Erro: o novo estado atingiu o limite de 4 digitos.')
                            print('Estado: ', novo_estado)
                            break
                        if movimento not in {'e', 'd', 'i'}:
                            print('Erro: caractere de movimento nao identificado.')
                            print('Movimento: ', movimento)
                            break

                        #print(self.verificaFim[0], estado_atual, simbolo_atual, self.verificaFim[1], novo_simbolo, movimento, novo_estado)
                        self.dicionario[self.verificaFim[0], estado_atual, simbolo_atual] = (
                            self.verificaFim[1], novo_simbolo, movimento, novo_estado)
                        self.dicionario[self.verificaFim[0], estado_atual, '*'] = (
                            self.verificaFim[1], novo_simbolo, movimento, novo_estado)
                self.linha_atual += 1

    def teste(self):
        #print(self.dicionario)
        print(self.fita)

    def passo(self, bloco, estado, simbolo):
        # print(self.blocos)
        # print(self.dicionario)
        chave = bloco, str(estado), simbolo
        if chave in self.dicionario:
            dados_linha = self.dicionario[chave]
        else:
            chave = bloco, str(estado), '*'
            if chave in self.dicionario:
                dados_linha = self.dicionario[bloco, str(estado), '*']
            else:
                dados_linha = self.dicionario[bloco, str(estado)]

        if len(dados_linha) == 4:
            linha, novo_simbolo, movimento, novo_estado = dados_linha
            if novo_estado != '*':
                self.estado = novo_estado
            if novo_simbolo != '*':
                self.fita[self.cabeca] = novo_simbolo
            #print(bloco, self.fita[self.cabeca], movimento, self.estado)
            print(bloco, simbolo, self.cabeca)
            #print(self.fita)
            # print(self.fita)
            if movimento == 'e':
                self.cabeca -= 1
                self.simbolo = self.fita[self.cabeca]
            elif movimento == 'd':
                self.cabeca += 1
                self.simbolo = self.fita[self.cabeca]
            elif movimento == 'i':
                pass
        else:
            bloco_retorno = self.bloco
            estado_retorno, bloco_atual, estado_inicial = dados_linha
            self.bloco = bloco_atual
            bloco, estado, simbolo, estado_retorno, bloco_retorno
            self.insere_pilha((bloco_atual, estado_inicial,
                              self.fita[self.cabeca], estado_retorno, bloco_retorno))
            dados = self.topo_pilha.dado
            # print(estado)

            self.passo_bloco(dados[0], dados[1], dados[2], dados[3], dados[4])
            #print(estado_retorno, bloco_atual, estado_inicial)

    def passo_bloco(self, bloco, estado, simbolo, estado_retorno, bloco_retorno):
        # print(self.blocos)
        # print(self.dicionario)
        #print(bloco, estado, simbolo)
        if str(estado) != 'pare':
            chave = bloco, str(estado), simbolo
            if chave in self.dicionario:
                dados_linha = self.dicionario[chave]
            else:
                chave = bloco, str(estado), '*'
                if chave in self.dicionario:
                    dados_linha = self.dicionario[bloco, str(estado), '*']
                else:
                    dados_linha = self.dicionario[bloco, str(estado)]
            # print(dados_linha)
            if len(dados_linha) == 4:
                if dados_linha[3] != 'retorne':
                    linha, novo_simbolo, movimento, novo_estado = dados_linha
                    #print(linha, novo_simbolo, movimento, novo_estado)
                    if novo_estado != '*':
                        self.estado = novo_estado
                    if novo_simbolo != '*':
                        self.fita[self.cabeca] = novo_simbolo
                    #print(bloco, self.fita[self.cabeca], movimento, self.estado)
                    print(bloco, simbolo, self.cabeca)
                    # print(self.fita)
                    if movimento == 'e':
                        self.cabeca -= 1
                        self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'd':
                        self.cabeca += 1
                        self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'i':
                        pass
                    self.passo_bloco(
                        bloco, self.estado, self.simbolo, estado_retorno, bloco_retorno)
                else:
                    # print(self.topo_pilha.dado)
                    self.remove_pilha()
                    # print(self.topo_pilha)
                    # Retornar para o bloco anterior
                    linha, novo_simbolo, movimento, novo_estado = dados_linha
                    #print(linha, novo_simbolo, movimento, novo_estado)
                    if novo_estado != '*':
                        self.estado = novo_estado
                    if novo_simbolo != '*':
                        self.fita[self.cabeca] = novo_simbolo
                    #print(bloco, self.fita[self.cabeca], movimento, self.estado)
                    print(bloco, simbolo)
                    # print(self.fita)
                    if movimento == 'e':
                        self.cabeca -= 1
                        self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'd':
                        self.cabeca += 1
                        self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'i':
                        pass

                    if self.topo_pilha is not None:
                        if self.topo_pilha.anterior == None:
                            # print("AAAAAAAAA")
                            self.bloco = self.topo_pilha.dado[4]
                            self.estado = self.topo_pilha.dado[3]
                            self.passo(self.bloco, self.estado,
                                       self.fita[self.cabeca])
                        else:
                            dados = self.topo_pilha.dado
                            self.passo_bloco(
                                dados[0], dados[1], dados[2], dados[3], dados[4])
                    else:
                        self.bloco = bloco_retorno
                        self.estado = estado_retorno
                        self.passo(bloco_retorno, estado_retorno, self.simbolo)
            else:
                # Caso de bloco sendo chamado dentro de outro bloco
                # print("-----------------------")
                # print(self.topo_pilha.dado)

                bloco_retorno = self.bloco
                estado_retorno, bloco_atual, estado_inicial = dados_linha
                self.bloco = bloco_atual
                bloco, estado, simbolo, estado_retorno, bloco_retorno
                self.insere_pilha(
                    (bloco_atual, estado_inicial, self.fita[self.cabeca], estado_retorno, bloco_retorno))
                dados = self.topo_pilha.dado
                # print(estado)

                self.passo_bloco(dados[0], dados[1],
                                 dados[2], dados[3], dados[4])
                #print(estado_retorno, bloco_atual, estado_inicial)

    def programa(self):
        erro = 0
        # self.teste()
        while self.estado != 'pare' and erro < 100:
            self.passo(self.bloco, self.estado, self.simbolo)
            erro += 1

    def insere_pilha(self, novo_dado):
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NoPilha(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo_pilha

        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo_pilha = novo_nodo

    def remove_pilha(self):
        """Remove o elemento que está no topo da pilha."""
        assert self.topo_pilha, "Impossível remover valor de pilha vazia."

        self.topo_pilha = self.topo_pilha.anterior

# Remove todas as tabulacoes do arquivo texto para nao dar erro

def remove_tabulacao(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo_sem_tab = ''
        for linha in arquivo:
            conteudo_sem_tab += linha.lstrip()
        return conteudo_sem_tab


input = '11'
arquivo_sem_tab = remove_tabulacao('teste_bloco_retorne.txt')
# mt = MT(input, arquivo_sem_tab)
arquivo_sem_tab1 = remove_tabulacao(programa_value)
mt = MT(palavra_inicial, arquivo_sem_tab)
mt.teste()
mt.programa()
mt.teste()
