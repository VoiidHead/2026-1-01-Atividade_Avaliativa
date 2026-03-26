print("Digite 4 números reais para ver a média aritmética entre eles e a diferença entre o maior e o menor")

pau = float(input())
latina = float(input())
mente = float(input())
exclamação = float(input())

safadezaMAX = float #abc acb bac bca cab cba, latina mente excl
if pau > latina > mente > exclamação:
    safadezaMAX = pau
elif pau > latina > exclamação > mente:
    safadezaMAX = pau
elif pau > mente > latina > exclamação:
    safadezaMAX = pau
elif pau > mente > exclamação > latina:
    safadezaMAX = pau
elif pau > exclamação > latina > mente:
    safadezaMAX = pau
elif pau > exclamação > mente > latina:
    safadezaMAX = pau

elif latina > pau > mente > exclamação:
    safadezaMAX = latina
elif latina > pau > exclamação > mente:
    safadezaMAX = latina
elif latina > mente > pau > exclamação:
    safadezaMAX = latina
elif latina > mente > exclamação > pau:
    safadezaMAX = latina
elif latina > exclamação > pau > mente:
    safadezaMAX = latina
elif latina > exclamação > mente > pau:
    safadezaMAX = latina

elif mente > pau > latina > exclamação:
    safadezaMAX = mente
elif mente > pau > exclamação > latina:
    safadezaMAX = mente
elif mente > latina > pau > exclamação:
    safadezaMAX = mente
elif mente > latina > exclamação > pau:
    safadezaMAX = mente
elif mente > exclamação > pau > latina:
    safadezaMAX = mente
elif mente > exclamação > latina > pau:
    safadezaMAX = mente

elif exclamação > pau > mente > latina:
    safadezaMAX = exclamação
elif exclamação > pau > latina > mente:
    safadezaMAX = exclamação
elif exclamação > mente > pau > latina:
    safadezaMAX = exclamação
elif exclamação > mente > latina > pau:
    safadezaMAX = exclamação
elif exclamação > latina > pau > mente:
    safadezaMAX = exclamação
elif exclamação > latina > mente > pau:
    safadezaMAX = exclamação

safadezaMIN = float
if pau < latina < mente < exclamação:
    safadezaMIN = pau
elif pau < latina < exclamação < mente:
    safadezaMIN = pau
elif pau < mente < latina < exclamação:
    safadezaMIN = pau
elif pau < mente < exclamação < latina:
    safadezaMIN = pau
elif pau < exclamação < latina < mente:
    safadezaMIN = pau
elif pau < exclamação < mente < latina:
    safadezaMIN = pau

elif latina < pau < mente < exclamação:
    safadezaMIN = latina
elif latina < pau < exclamação < mente:
    safadezaMIN = latina
elif latina < mente < pau < exclamação:
    safadezaMIN = latina
elif latina < mente < exclamação < pau:
    safadezaMIN = latina
elif latina < exclamação < pau < mente:
    safadezaMIN = latina
elif latina < exclamação < mente < pau:
    safadezaMIN = latina

elif mente < pau < latina < exclamação:
    safadezaMIN = mente
elif mente < pau < exclamação < latina:
    safadezaMIN = mente
elif mente < latina < pau < exclamação:
    safadezaMIN = mente
elif mente < latina < exclamação < pau:
    safadezaMIN = mente
elif mente < exclamação < pau < latina:
    safadezaMIN = mente
elif mente < exclamação < latina < pau:
    safadezaMIN = mente

elif exclamação < pau < mente < latina:
    safadezaMIN = exclamação
elif exclamação < pau < latina < mente:
    safadezaMIN = exclamação
elif exclamação < mente < pau < latina:
    safadezaMIN = exclamação
elif exclamação < mente < latina < pau:
    safadezaMIN = exclamação
elif exclamação < latina < pau < mente:
    safadezaMIN = exclamação
elif exclamação < latina < mente < pau:
    safadezaMIN = exclamação

print(f'A média aritmética entre {pau}, {latina}, {mente} & {exclamação} é {(pau + latina + mente + exclamação) / 4} \nE a diferença entre o maior número e o menor número dentre eles é {safadezaMAX - safadezaMIN}')
