#Perguntar o nome da pessoa, o ano de nascimento e calcular a idade da pessoa

from datetime import date
nome = input("Qual é o seu nome? ")
ano_nascimento = int(input("Qual é o seu ano de nascimento? "))

#Criar uma função para calcular a idade da pessoas
def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

print(f"{nome}, você tem {calcular_idade(ano_nascimento)} anos.")
