"""#crie um programa que receba de um professor varias notas de um aluno de 0 a 10(nao importa quantas notas).
Ao final do programa a media das notas devera ser calculada e informada e em seguida o programa ira informar se o aluno
foi aprovado, caso media for maior ou igual a 7 
ficou de recuperacao caso for entre 5 e 7
e reprovado caso seja menor que 5.
"""

"""""
#entrada de dados 

nota1 =(input("Informe a primeira nota do aluno de 0 a 10:"))
nota2 = (input("Informe a primeira nota do aluno de 0 a 10:"))
nota3 = (input("Informe a primeira nota do aluno de 0 a 10:"))

calculo_media = nota1 + nota2 + nota3
media = calculo_media /3

#saida de dados
print(f"A media do aluno é {media:.2f}.")
if media >= 7:
    print("O aluno foi aprovado.")
elif media >= 5:
    print("O aluno ficou de recuperação.")

else:
    print("O aluno foi reprovado.")

"""""


import os
nota=[]

while True:
    print("1 informe a nota do aluno de 0 a 10")
    print("2 informar a media e sair do programa")
    opcao = input("Escolha uma opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                nova_nota = float(input("Infore a nova nota do aluno de 0 a 10: ").replace(",", "."))
                if nova_nota >= 0 and nova_nota <= 10:
                    nota.append(nova_nota)
                    print("nota inserida com sucesso.")
                
                else:
                    print("Nota inválida. Deve ser entre 0 e 10.")
                continue
                
            except Exception as e:
                print(f"Erro ao inserir a nota: {e}")
            finally:
                continue
          
        case "2":
            try:
                media = sum(nota) / len(nota) 
                print(f"A média das notas é: {media:.2f}")
                if media >= 7:
                    print("O aluno foi aprovado.")
                elif media >= 5:
                    print("O aluno ficou de recuperação.")
                else:
                    print("O aluno foi reprovado.")
            except Exception as e:
                print(f"Erro ao calcular a média: {e}")
            finally:
                break 
            
        case _:
            print("Opção inválida. Tente novamente.")
            continue 




