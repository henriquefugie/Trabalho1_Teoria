import sys
import argparse

# Joao Vitor Dias Fernandes e Henrique Fugie

# Comando de exemplo cmd para executar: python simturing.py tp2teoria.MT -v

# Pilha para ser usada na verificacao de blocos
class NoPilha:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class MT:
    def __init__(self, input, arquivo, delimitador):
        self.simbolo = input[0]
        input = ''.join(['_____________________']) + input + \
            ''.join(['____________________'])
        self.dicionario = {}
        self.estado = '1'
        self.fita = list(input)
        self.cabeca = 21
        self.linha_atual = 0
        self.bloco = 'main'
        self.bloco_linha = ('main', None)
        self.inicio_bloco = {}
        self.fimArquivo = True
        self.linhasArquivo_array = arquivo.splitlines()
        self.topo_pilha = None
        self.conta_passos = 0
        self.delimitador = delimitador
        while self.fimArquivo:
            if self.linha_atual == len(self.linhasArquivo_array):
                self.fimArquivo = False
            elif self.linha_atual < len(self.linhasArquivo_array):
                valores_linha = self.linhasArquivo_array[self.linha_atual].split(
                    ' ')
                # Se nao for comentario
                if valores_linha[0] != ';':
                    # Bloco ou chamada de bloco ou fim
                    if len(valores_linha) == 3:
                        if valores_linha[0] == 'bloco':
                            # Armazena nome do bloco e a linha em formato de tupla
                            self.bloco_linha = (valores_linha[1], self.linha_atual)
                            # Armazena o nome do bloco e onde comeca o estado do bloco em dicionario para ser usado posteriormente
                            self.inicio_bloco[valores_linha[1]] = (
                                valores_linha[2])
                            # Atualiza o self.estado para o estado inicial do bloco main
                            if valores_linha[1] == 'main':
                                self.estado = valores_linha[2]

                        # Entra aqui quando for mandado para outro bloco
                        # Exemplo: 10 moveFim 11
                        else:
                            if valores_linha[0] != 'fim':
                                self.dicionario[self.bloco_linha[0], valores_linha[0]] = (
                                    valores_linha[2], valores_linha[1], 1)
                    # Caso breakpoint
                    if len(valores_linha) == 4:
                        self.dicionario[self.bloco_linha[0], valores_linha[0]] = (
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
                        
                        # Armazena o nome do bloco atual, o estado atual, simbolo atual,
                        # linha do bloco, simbolo a ser escrito, movimento do cabecote e qual o novo estado a ir
                        self.dicionario[self.bloco_linha[0], estado_atual, simbolo_atual] = (
                            self.bloco_linha[1], novo_simbolo, movimento, novo_estado)
                        
                        # Armazena tambem para cada caso, a situacao de se ter um simbolo qualquer que pode
                        # ser identificado pelo *, se tem isso pois o * identifica todos os simbolos existentes
                        if valores_linha[1] == '*':
                            self.dicionario[self.bloco_linha[0], estado_atual, '*'] = (
                                self.bloco_linha[1], novo_simbolo, movimento, novo_estado)
                    # Caso breakpoint
                    if len(valores_linha) == 7:
                        estado_atual, simbolo_atual, traco, novo_simbolo, movimento, novo_estado, breakpoint = valores_linha
                        self.dicionario[self.bloco_linha[0], estado_atual, simbolo_atual] = (
                            self.bloco_linha[1], novo_simbolo, movimento, novo_estado, '!')
                self.linha_atual += 1
    
    # Responsavel por executar uma linha de comando do arquivo
    # Exemplo: 1 _ -- * d 2
    def executa_linha(self, dados_linha):
        if len(dados_linha) == 4:
            linha, novo_simbolo, movimento, novo_estado = dados_linha
        elif len(dados_linha) == 5:
            linha, novo_simbolo, movimento, novo_estado, breakpoint = dados_linha
        if novo_estado != '*':
            self.estado = novo_estado
        if novo_simbolo != '*':
            self.fita[self.cabeca] = novo_simbolo
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

    # Retorna o valor do dicionario baseado no bloco, estado e simbolo atual
    def chave_dicionario(self, bloco, estado, simbolo):
        chave1 = bloco, str(estado), simbolo
        chave2 = bloco, str(estado), '*'
        if chave1 in self.dicionario:
            dados_linha = self.dicionario[chave1]
        elif chave2 in self.dicionario:
            dados_linha = self.dicionario[chave2]
        else:
            chave = bloco, str(estado)
            if chave in self.dicionario:
                dados_linha = self.dicionario[bloco, str(estado)]
            else:
                sys.exit("Chave nao existente")
        return dados_linha

    def passo(self, bloco, estado, simbolo, args, passo_limite):
        if args.step:
            if passo_limite > 0 and self.conta_passos <= passo_limite:
                self.conta_passos += 1
        if str(estado) != 'pare':
            dados_linha = self.chave_dicionario(bloco, estado, simbolo)
            # Breakpoint
            if len(dados_linha) != 5:
                if len(dados_linha) == 4:
                    self.executa_linha(dados_linha)
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
            else:
                self.executa_linha(dados_linha)
                return 1
        return 0

    def passo_bloco(self, bloco, estado, simbolo, estado_retorno, bloco_retorno, args, passo_limite):
        if args.step:
            if passo_limite > 0 and self.conta_passos <= passo_limite:
                self.mostra_fita()
                self.conta_passos += 1
        elif args.verbose:
            self.mostra_fita()
        if str(estado) != 'pare':
            dados_linha = self.chave_dicionario(bloco, estado, simbolo)
            if len(dados_linha) != 5:
                # Breakpoint
                if len(dados_linha) == 4:
                    if dados_linha[3] != 'retorne':
                        self.executa_linha(dados_linha)
                        self.passo_bloco(
                            bloco, self.estado, self.simbolo, estado_retorno, bloco_retorno, args, passo_limite)
                    else:
                        self.remove_pilha()
                        # Retornar para o bloco anterior
                        self.executa_linha(dados_linha)
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
            else:
                self.executa_linha(dados_linha)
                return 1
        return 0

    def programa(self, args, passo_limite):
        erro = 0
        verifica_break = -1
        while self.estado != 'pare' and erro < 100000000 and verifica_break != 1 and erro < passo_limite:
            verifica_break = self.passo(self.bloco, self.estado, self.simbolo, args, passo_limite)
            if not args.resume:
                self.mostra_fita()
            erro += 1
        return verifica_break

    def mostra_fita(self):
        delim = self.delimitador[0]
        token_esquerda = delim[0]
        token_direita = delim[1]
        elementos_esquerda = self.fita[max(0, self.cabeca-20):self.cabeca]
        elementos_direita = self.fita[self.cabeca+1:self.cabeca+21]
        nova_lista = elementos_esquerda + [token_esquerda + self.fita[self.cabeca] + token_direita] + elementos_direita
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
    breakpoint = -1
    execucao_inicial = True
    while True:
        if execucao_inicial == True:
            parser = argparse.ArgumentParser(description='Simulador de Máquina de Turing')
            parser.add_argument('programa', help='Nome do arquivo que contém o código da MT')
            parser.add_argument('-verbose', '-v', action='store_true', help='Mostra a execução passo a passo do programa até o fim')
            parser.add_argument('-step', '-s', type=int, help='Mostra n linhas de execução passo a passo na tela')
            parser.add_argument('-resume', '-r', action='store_true', help='Executa o programa até o fim e imprime o conteúdo final na fita')
            parser.add_argument('-head', metavar='<>', nargs=1, help='Descrição da opção -head')
            args = parser.parse_args()
            print('Simulador de Máquina de Turing v1.0 - IFMG 2023')
            print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação')
            print('Autores: Joao Vitor Dias Fernandes & Henrique Fugie\n')
            step_value = args.step

        if execucao_inicial == False:
            aux = args
            opcao = input("Forneça opção ( r , v , s ) : ")
            if opcao == 'r':
                args.verbose = False
                args.step = False
                args.resume = True
            elif opcao == 'v':
                args.step = False
                args.resume = False
                args.verbose = True
            elif opcao == 's':
                args.verbose = False
                args.resume = False
                args.step = True
                step_value = int(input("Quantidade de passos: "))
            # Apertou enter
            elif opcao == '':
                args = aux
        if breakpoint != 1:
            palavra_inicial = input('Forneça a palavra inicial: ')
            programa_value = 'tp2etestes/'
            programa_value += args.programa
            arquivo_sem_tab1 = remove_tabulacao(programa_value)
            if args.head:
                delimitador = args.head[0].split()
            else:
                delimitador = ['()']
            mt = MT(palavra_inicial, arquivo_sem_tab1,delimitador)
        if args.verbose:
            print("Executando a opcao verbose")
            breakpoint = mt.programa(args, 1000000)
            if breakpoint != 1:
                return
        if args.step:
            print("Executando a opcao step")
            print("Quantidade de steps:", step_value)
            mt.programa(args, step_value)
            mt.conta_passos = 0
        if args.resume:
            print("Executando a opcao resume")
            breakpoint = mt.programa(args, 1000000)
            elementos = ''.join(mt.fita)
            print(elementos)

        execucao_inicial = False

if __name__ == "__main__":
    main()