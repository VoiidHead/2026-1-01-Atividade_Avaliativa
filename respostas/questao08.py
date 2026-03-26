print("Digite 4 números inteiros para descobrir a soma deles e se ela é maior que 100")

S = int(input())
E = int(input())
X = int(input())
O = int(input())

SimpsonGamer = S + E + X + O
print(f'{S} + {E} + {X} + {O} = {SimpsonGamer}')
if SimpsonGamer > 100:
    print(f'A soma de {S}, {E}, {X} & {O} é maior que 100')
elif SimpsonGamer < 100:
    print(f'A soma de {S}, {E}, {X} & {O} é menor que 100')