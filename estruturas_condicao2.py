#Microatividade 2: Descrever a utilização da estrutura de condição else if (elif) em Python
#Crie uma variável chamada tempoExperiencia e atribua a ela o valor 5;
tempo_experiencia = 5
#Crie uma verificação, utilizando a condição if, para checar se o valor da variável tempoExperiencia é menor que 2;

tempo_experiencia = int(input("Digite o número teste aqui!"))
if tempo_experiencia < 2:
    print("Experiência insuficiente")
elif tempo_experiencia > 2 <5:
    print("Nivel de conhecimento Pleno")
else:
    print("Nível de conhecimento júnior")
