#variavel vazia modelo srt
entrada_idade = ''
#veriicar se a entrada é diferente de 0
while str(entrada_idade)!= '0':
    #solicitar um entrada
    entrada_idade = input("Digite sua idade (digite 0 para sair): ")

    #verificar se a entrada é um número antes de tentar converter
    if entrada_idade.isdigit(): #tentar garantir que o valor seja um número
        entrada_idade = int(entrada_idade) #tentar converter para int se for um número valido

        if entrada_idade == 0:
            print("encerrando o programa...")
        else:
            print(f"sua idade{entrada_idade}.")
    else:
        print("Por favor, insira um número válido.")