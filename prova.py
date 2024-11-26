# Crie uma função chamada maior_numero que receberá três números como argumentos. 
# Esta função deve comparar os três números e identificar qual deles é o maior. 
# Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. 
# A função deve então retornar o maior número encontrado.



while True:

    print ("  ")
    print("COMPARADOR DE VALORES")
    print (" ")

    x= float(input("insira o primeiro numero: "))
    y= float(input("insira no segundo numero: "))
    z= float(input("insira o terceiro numero: "))

    def maior_numero(x, y, z):
        if x == y == z:
            return f"Todos os numeros são iguais"

        elif x == y > z:
            return f"o primeiro e o segundo número: {x , y} são iguais e maiores que {z}"
        
        elif z == y > x:
            return f"o segundo e o terceiro numero: {z , y} são iguais e maiores que {x}"
        
        elif x == z > y:
            return f"o primeiro e o terceiro numero: {x , y} são iguais e maiores que {y}"
        
        elif x == y < z:
            return f"o primeiro e o segundo número: {x , y} são iguais e menores que {z}"
        
        elif z == y < x:
            return f"o segundo e o terceiro numero: {z , y} são iguais e menores que {x}"
        
        elif x == z < y:
            return f"o primeiro e o terceiro numero: {x , y} são iguais e menores que {y}"
        
        else:
            return f" O maior número é: {max(x, y, z)}"
        

    maior= maior_numero(x , y, z)
    print(f"{maior}")

    continuar= input(" Deseja continuar (s/n)?").strip().upper()
    if continuar != 'S' : break

    
  