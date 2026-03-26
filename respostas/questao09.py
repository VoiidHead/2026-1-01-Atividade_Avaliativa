print("Digite 4 números reais para ver o produto deles e se o produto é positivo")

GOATminora = float(input())
GOATfischer = float(input())
GOATbrave = float(input())
GOATcharmander = float(input())

gyatt = float(GOATminora * GOATfischer * GOATbrave * GOATcharmander)
print(f'{GOATminora} · {GOATfischer} · {GOATbrave} · {GOATcharmander} = {gyatt}')
if gyatt > 0:
    print(f'O produto de {GOATminora}, {GOATfischer}, {GOATbrave} & {GOATcharmander} é positivo')
elif gyatt < 0:
    print(f'O produto de {GOATminora}, {GOATfischer}, {GOATbrave} & {GOATcharmander} não é positivo')