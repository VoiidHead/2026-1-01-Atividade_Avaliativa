mentecaptos = []

for uff in range(15):
	print('Digite as notas e o nome do aluno, tudo separado por barra (nota1/nota2/nota3/nota4/nome)')
	manjericão, hortelã, menta, boldo, pequenoalecrim = input().split('/')
	manjericão = float(manjericão)
	hortelã = float(hortelã)
	menta = float(menta)
	boldo = float(boldo)

	misturamaluca = (manjericão + hortelã + menta + boldo) / 4
	if misturamaluca >=6:
		kvalo = 'APROVADO'
	elif 4 <= misturamaluca < 6:
		kvalo = 'em recuperação'
	else:
		kvalo = 'REPROVADO'

	mentecaptos.append([manjericão, hortelã, menta, boldo, pequenoalecrim, misturamaluca, kvalo])
	
for 豚 in mentecaptos:
	print(f'Nome: {豚[4]} \t1º Bim.: {豚[0]} \t2º Bim.: {豚[1]} \t3º Bim.: {豚[2]} \t4º Bim.: {豚[3]} \tMédia: {豚[5]:.2f} \tSituação: {豚[6]}')
