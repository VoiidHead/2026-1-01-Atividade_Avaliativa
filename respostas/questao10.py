print("Digite a sua média dos 4 bimestres para descobrir sua nota final!")

cansaço = float(input())
sono = float(input())
ansiedade = float(input())
melancolia = float(input())

falta_de_graça = (cansaço + sono + ansiedade + melancolia) / 4
print(f"A sua nota final é: {falta_de_graça}")
if falta_de_graça >= 6:
    print("Parabéns, está aprovado!")
else:
    print("Você está reprovado.")