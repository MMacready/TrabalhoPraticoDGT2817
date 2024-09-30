saida = ''
def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b 
def divisao(a, b):
    if b == 0:
        return "Desculpe não foi possivel realizar a divisão por 0"
    return a/b
#Criar uma função chamada calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adicao':
     return adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
     return subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
     return multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
     return divisao(num1, num2)
    else:
     return "Operação inválida"
#Criar um laço while
while saida.lower() != 'n':
    # Inserir os dois números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou o nome da operação): ")

    # Chamar a função calculadora e armazenar o resultado
    resultado = calculadora(num1, num2, operacao)
    
    # Calcular o resultado
    print("Resultado da operação: ", resultado)
    
    # Perguntar ao usuário se deseja continuar ou sair
    saida = input("Deseja continuar? (S/N): ")
