import argparse

# Joao Vitor Dias Fernandes e Henrique Fugie

# Pilha para ser usada na verificacao de blocos
class NoPilha:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
    

class MT:
    def __init__(self, input, arquivo):
        self.simbolo = input[0]
        input = ''.join(['_____________________']) + input + \
            ''.join(['____________________'])
        self.dicionario = {}
        self.estado = '1'
        self.fita = list(input)
        self.cabeca = 21
        self.linha_atual = 0
        self.bloco = 'main'
        self.verificaFim = None
        self.inicio_bloco = {}
        self.chama_bloco = 'main'
        self.fimArquivo = True
        self.linhasArquivo_array = arquivo.splitlines()
        self.topo_pilha = None
        self.conta_passos = 0
        while self.fimArquivo:
            if self.linha_atual == len(self.linhasArquivo_array):
                self.fimArquivo = False
            elif self.linha_atual < len(self.linhasArquivo_array):
                valores_linha = self.linhasArquivo_array[self.linha_atual].split(
                    ' ')
                # Se nao for comentario
                if valores_linha[0] != ';':
                    # BLOCO
                    if len(valores_linha) == 3:
                        if valores_linha[0] == 'bloco':
                            self.verificaFim = (
                                valores_linha[1], self.linha_atual)

                            self.chama_bloco = valores_linha[1]
                            # Armazena o nome do bloco e onde comeca o estado do bloco
                            self.inicio_bloco[valores_linha[1]] = (
                                valores_linha[2])
                            
                            # Atualiza o self.estado para o estado inicial do bloco main
                            if valores_linha[1] == 'main':
                                self.estado = valores_linha[2]
                        # Entra aqui quando for mandado para outro bloco
                        # Exemplo: 10 moveFim 11
                        else:
                            self.dicionario[self.chama_bloco, valores_linha[0]] = (
                                valores_linha[2], valores_linha[1], 1)
                    # Caso breakpoint
                    if len(valores_linha) == 4:
                        self.dicionario[self.chama_bloco, valores_linha[0]] = (
                                valores_linha[2], valores_linha[1], 1, '!')
                    if len(valores_linha) == 6:
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

                        self.dicionario[self.verificaFim[0], estado_atual, simbolo_atual] = (
                            self.verificaFim[1], novo_simbolo, movimento, novo_estado)
                        self.dicionario[self.verificaFim[0], estado_atual, '*'] = (
                            self.verificaFim[1], novo_simbolo, movimento, novo_estado)
                    # Caso breakpoint
                    if len(valores_linha) == 7:
                        self.dicionario[self.verificaFim[0], estado_atual, simbolo_atual] = (
                            self.verificaFim[1], novo_simbolo, movimento, novo_estado, '!')
                self.linha_atual += 1

    def passo(self, bloco, estado, simbolo, args, passo_limite):
        if args.step:
            if passo_limite > 0 and self.conta_passos <= passo_limite:
                self.mostra_fita()
                self.conta_passos += 1
        elif args.verbose:
            self.mostra_fita()
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

            if len(dados_linha) == 4:
                linha, novo_simbolo, movimento, novo_estado = dados_linha
                if novo_estado != '*':
                    self.estado = novo_estado
                if novo_simbolo != '*':
                    self.fita[self.cabeca] = novo_simbolo
                #print()
                #print(self.estado, self.simbolo)
                #print(self.fita)
                #print()
                if movimento == 'e':
                    self.cabeca -= 1
                    if self.cabeca == 0:
                        self.fita.insert(0, '_')
                        self.cabeca += 1
                        self.simbolo = self.fita[self.cabeca]
                    else:
                        self.simbolo = self.fita[self.cabeca]
                elif movimento == 'd':
                    self.cabeca += 1
                    if self.cabeca == len(self.fita):
                        self.fita.append('_')
                    self.simbolo = self.fita[self.cabeca]
                elif movimento == 'i':
                    self.simbolo = self.fita[self.cabeca]
            elif len(dados_linha) == 5:
                return
            else:
                bloco_retorno = self.bloco
                estado_retorno, bloco_atual, estado_inicial = dados_linha
                self.bloco = bloco_atual
                bloco, estado, simbolo, estado_retorno, bloco_retorno
                self.insere_pilha((bloco_atual, estado_inicial,
                                self.fita[self.cabeca], estado_retorno, bloco_retorno))
                dados = self.topo_pilha.dado

                # Essa linha eh responsavel por checar qual o estado inicial do bloco chamado e atualizar o self.estado com esse estado inicial
                self.estado = self.inicio_bloco[dados[0]]

                self.passo_bloco(dados[0], self.estado, dados[2], dados[3], dados[4], args, passo_limite)

    def passo_bloco(self, bloco, estado, simbolo, estado_retorno, bloco_retorno, args, passo_limite):
        if args.step:
            if passo_limite > 0 and self.conta_passos <= passo_limite:
                self.mostra_fita()
                self.conta_passos += 1
        elif args.verbose:
            self.mostra_fita()
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
            if len(dados_linha) == 4:
                if dados_linha[3] != 'retorne':
                    linha, novo_simbolo, movimento, novo_estado = dados_linha
                    if novo_estado != '*':
                        self.estado = novo_estado
                    if novo_simbolo != '*':
                        self.fita[self.cabeca] = novo_simbolo
                    #print(bloco, simbolo, self.estado)
                    if movimento == 'e':
                        self.cabeca -= 1
                        if self.cabeca == 0:
                            self.fita.insert(0, '_')
                            self.cabeca += 1
                            self.simbolo = self.fita[self.cabeca]
                        else:
                            self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'd':
                        self.cabeca += 1
                        if self.cabeca == len(self.fita):
                            self.fita.append('_')
                        self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'i':
                        self.simbolo = self.fita[self.cabeca]
                    self.passo_bloco(
                        bloco, self.estado, self.simbolo, estado_retorno, bloco_retorno, args, passo_limite)
                else:
                    self.remove_pilha()

                    # Retornar para o bloco anterior
                    linha, novo_simbolo, movimento, novo_estado = dados_linha

                    if novo_estado != '*':
                        self.estado = novo_estado
                    if novo_simbolo != '*':
                        self.fita[self.cabeca] = novo_simbolo

                    #print(bloco, simbolo, self.estado)
                    if movimento == 'e':
                        self.cabeca -= 1
                        if self.cabeca == 0:
                            self.fita.insert(0, '_')
                            self.cabeca += 1
                            self.simbolo = self.fita[self.cabeca]
                        else:
                            self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'd':
                        self.cabeca += 1
                        if self.cabeca == len(self.fita):
                            self.fita.append('_')
                        self.simbolo = self.fita[self.cabeca]
                    elif movimento == 'i':
                        self.simbolo = self.fita[self.cabeca]

                    if self.topo_pilha is not None:
                        if self.topo_pilha.anterior == None:
                            self.bloco = self.topo_pilha.dado[4]
                            self.estado = self.topo_pilha.dado[3]
                            self.passo(self.bloco, self.estado,
                                       self.fita[self.cabeca], args, passo_limite)
                        else:
                            dados = self.topo_pilha.dado
                            self.passo_bloco(
                                dados[0], dados[1], dados[2], dados[3], dados[4], args, passo_limite)
                    else:
                        self.bloco = bloco_retorno
                        self.estado = estado_retorno
                        self.passo(bloco_retorno, estado_retorno, self.simbolo, args, passo_limite)
            elif len(dados_linha) == 5:
                return
            else:
                # Caso de bloco sendo chamado dentro de outro bloco
                bloco_retorno = self.bloco
                estado_retorno, bloco_atual, estado_inicial = dados_linha
                self.bloco = bloco_atual
                bloco, estado, simbolo, estado_retorno, bloco_retorno
                self.insere_pilha(
                    (bloco_atual, estado_inicial, self.fita[self.cabeca], estado_retorno, bloco_retorno))
                dados = self.topo_pilha.dado

                # Essa linha eh responsavel por checar qual o estado inicial do bloco chamado e atualizar o self.estado com esse estado inicial
                self.estado = self.inicio_bloco[dados[0]]

                self.passo_bloco(dados[0], self.estado,
                                 dados[2], dados[3], dados[4], args, passo_limite)

    def programa(self, args, passo_limite):
        erro = 0
        while self.estado != 'pare' and erro < 100000000:
            #print(self.conta_passos)
            self.passo(self.bloco, self.estado, self.simbolo, args, passo_limite)
            erro += 1
        if args.verbose:
            self.mostra_fita()

    def mostra_fita(self):
        elementos_esquerda = self.fita[max(0, self.cabeca-20):self.cabeca]
        elementos_direita = self.fita[self.cabeca+1:self.cabeca+21]
        nova_lista = elementos_esquerda + ['(' + self.fita[self.cabeca] + ')'] + elementos_direita
        elementos = ''.join(nova_lista)
        print(self.bloco, self.estado, elementos)

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


def main():
    parser = argparse.ArgumentParser(description='Simulador de Máquina de Turing')
    parser.add_argument('programa', help='Nome do arquivo que contém o código da MT')
    parser.add_argument('-resume', '-r', action='store_true', help='Executa o programa até o fim e imprime o conteúdo final na fita')
    parser.add_argument('-verbose', '-v', action='store_true', help='Mostra a execução passo a passo do programa até o fim')
    parser.add_argument('-step', '-s', type=int, help='Mostra n linhas de execução passo a passo na tela')
    args = parser.parse_args()

    with open(('tp2etestes/' + args.programa), 'r') as file:
        codigo_mt = file.read()

    print('Simulador de Máquina de Turing v1.0 - IFMG 2023')
    print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação')
    print('Autores: Joao Vitor Dias Fernandes & Henrique Fugie\n')

    palavra_inicial = input('Forneça a palavra inicial: ')

    step_value = args.step
    programa_value = 'tp2etestes/'
    programa_value += args.programa

    #arquivo_sem_tab = remove_tabulacao('tp2teoria.txt')
    #print(arquivo_sem_tab)
    #mt = MT("01041+17511=", arquivo_sem_tab)
    #arquivo_sem_tab = remove_tabulacao('teste2.txt')
    arquivo_sem_tab1 = remove_tabulacao(programa_value)
    #print(programa_value)
    mt = MT(palavra_inicial, arquivo_sem_tab1)
    #mt.teste()
    if args.resume:
        print("Executando a opcao resume")
        mt.programa(args, -1)
        elementos = ''.join(mt.fita)
        print(elementos)

    #print(type(args.verbose))
    if args.verbose:
        print("Executando a opcao verbose")
        mt.programa(args, -1)

    if args.step:
        print("Executando a opcao step")
        print("Quantidade de steps:", step_value)
        mt.programa(args, step_value)

if __name__ == "__main__":
    main()