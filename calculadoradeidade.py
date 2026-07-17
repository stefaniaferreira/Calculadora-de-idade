#Perguntar o nome da pessoa, o ano de nascimento (aaaa) e calcular a idade da pessoa

from datetime import date
nome = input("Qual é o seu nome? ")

while True:
    try:
        ano_nascimento = int(input("Qual é o seu ano de nascimento? "))
        break
    except ValueError:
        print("Por favor, digite apenas números.")

#Formatar o ano em 4 dígitos e criar uma função para calcular a idade da pessoa 

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

print(f"{nome}, você tem {calcular_idade(ano_nascimento)} anos.")





