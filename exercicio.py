# Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números. 
# Para fazer isso, some os três números e, em seguida, divida o resultado por três.
# Por fim, a função deve retornar o valor da média aritmética calculada.


colunas= "-" * 60

print(colunas)
print("MÉDIA ESCOLAR")
print(colunas)


a = float(input("insira a sua nota 1: "))
b = float(input("insira a sua nota 2: "))
c = float(input("insira a sua nota 3: "))


def media_aritmetica(a, b, c):
    soma = a + b + c 
    resultado = soma/3
    print(f"A média das suas notas é: {resultado: }")

media_aritmetica(a, b, c)








