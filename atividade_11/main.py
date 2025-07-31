# TODO - atividade crie um programa que receba di ysyarui um numero inteiro e o programa calcula o valor da sequencia de fibonacci 

# e imprima o resultado
def fibonacci(n): 
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
print(fibonacci(int(input("Digite um número inteiro: "))) )  
 
