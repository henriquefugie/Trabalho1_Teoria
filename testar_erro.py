import subprocess
import random
import re

def executar_arquivo(nome_arquivo, x):
    resultados_diferentes = False

    for _ in range(x):
        # Gerar dois números aleatórios entre 1 e 100
        numero1 = random.randint(1, 1000000)
        numero2 = random.randint(1, 1000000)
        expressao = f"{numero1}+{numero2}="
        resultado = numero1 + numero2
        try:
            comando = f"python {nome_arquivo} -r tp2teoria.MT"
            processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            saida, _ = processo.communicate(input=expressao + '\n')  # Envia a expressão seguida de um "Enter"
            print(saida)

            # Filtrar a saída para obter apenas a parte desejada
            linhas = saida.split('\n')
            resultado_programa = None
            for linha in linhas:
                if linha.startswith('_____________________'):
                    resultado_programa = re.sub(r'[^0-9]', '', linha.split('=')[-1].strip())
                    break

            print(f"{numero1} + {numero2} = {resultado}")
            if resultado_programa == str(resultado):
                print("resultados iguais.")
            else:
                print("resultados diferentes.")
                resultados_diferentes = True
        except FileNotFoundError:
            print(f"O arquivo {nome_arquivo} não foi encontrado.")
        except subprocess.SubprocessError as e:
            print(f"Ocorreu um erro ao executar o arquivo: {str(e)}")

    if resultados_diferentes:
        print("Existem casos com resultados diferentes.")
    else:
        print("Todos os casos têm resultados iguais.")

# Solicitar o valor de x ao usuário
x = int(input("Digite o valor de x: "))
executar_arquivo("main.py", x)  # Execute x times with random values
