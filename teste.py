import subprocess
import random

def executar_arquivo(nome_arquivo):
    # Gerar dois números aleatórios entre 1 e 100
    numero1 = random.randint(1, 1000000)
    numero2 = random.randint(1, 1000000)
    expressao = f"{numero1}+{numero2}="
    resultado = numero1+numero2
    try:
        comando = f"python {nome_arquivo} -r tp2teoria.MT"
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE)
        processo.communicate(input=expressao.encode() + b'\n')  # Envia a expressão seguida de um "Enter"
        print(f"{numero1} + {numero2} = {resultado}")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except subprocess.SubprocessError as e:
        print(f"Ocorreu um erro ao executar o arquivo: {str(e)}")


executar_arquivo("main.py")