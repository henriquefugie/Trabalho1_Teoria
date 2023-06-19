# Feito por Joao Vitor

linhas_modificadas = []

# Lê o arquivo original
with open("trabalho_parte2_morphett.txt", 'r') as arquivo:
    linhas = arquivo.readlines()

# Realiza as alterações nas linhas
for linha in linhas:
    tokens = linha.split()
    if len(tokens) >= 2:
        tokens.insert(2, "--")  # Adiciona "--" após o segundo token
    if len(tokens) >= 5:  # Verifica se existe um quinto token
        if tokens[4] == "r":
            tokens[4] = "d"  # Substitui "r" por "d"
        elif tokens[4] == "l":
            tokens[4] = "e"  # Substitui "l" por "e"
        elif tokens[4] == "*":
            tokens[4] = "i"  # Substitui "*" por "i"
    linhas_modificadas.append(" ".join(tokens) + "\n")  # Adiciona a quebra de linha

# Escreve as linhas modificadas no novo arquivo
with open("arquivo.txt", 'w') as novo_arquivo:
    novo_arquivo.writelines(linhas_modificadas)

print("Novo arquivo criado com sucesso!")
