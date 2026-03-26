print("Digite 4 números reais para ver a média aritmética entre eles e a diferença entre o maior e o menor")

pau = float(input())
latina = float(input())
mente = float(input())
exclamação = float(input())

safadezaMAX = float #abc acb bac bca cab cba, latina mente excl
if pau > latina > mente > exclamação:
    safadezaMAX = pau
if pau > latina > exclamação > mente:
    safadezaMAX = pau
if pau > mente > latina > exclamação:
    safadezaMAX = pau
if pau > mente > exclamação > latina:
    safadezaMAX = pau
if pau > exclamação > latina > mente:
    safadezaMAX = pau
if pau > exclamação > mente > latina:
    safadezaMAX = pau

if latina > pau > mente > exclamação:
    safadezaMAX = latina
if latina > pau > exclamação > mente:
    safadezaMAX = latina
if latina > mente > pau > exclamação:
    safadezaMAX = latina
if latina > mente > exclamação > pau:
    safadezaMAX = latina
if latina > exclamação > pau > mente:
    safadezaMAX = latina
if latina > exclamação > mente > pau:
    safadezaMAX = latina

if mente > pau > latina > exclamação:
    safadezaMAX = mente
if mente > pau > exclamação > latina:
    safadezaMAX = mente
if mente > latina > pau > exclamação:
    safadezaMAX = mente
if mente > latina > exclamação > pau:
    safadezaMAX = mente
if mente > exclamação > pau > latina:
    safadezaMAX = mente
if mente > exclamação > latina > pau:
    safadezaMAX = mente

if exclamação > pau > mente > latina:
    safadezaMAX = exclamação
if exclamação > pau > latina > mente:
    safadezaMAX = exclamação
if exclamação > mente > pau > latina:
    safadezaMAX = exclamação
if exclamação > mente > latina > pau:
    safadezaMAX = exclamação
if exclamação > latina > pau > mente:
    safadezaMAX = exclamação
if exclamação > latina > mente > pau:
    safadezaMAX = exclamação

safadezaMIN = float
if pau < latina < mente < exclamação:
    safadezaMIN = pau
if pau < latina < exclamação < mente:
    safadezaMIN = pau
if pau < mente < latina < exclamação:
    safadezaMIN = pau
if pau < mente < exclamação < latina:
    safadezaMIN = pau
if pau < exclamação < latina < mente:
    safadezaMIN = pau
if pau < exclamação < mente < latina:
    safadezaMIN = pau

if latina < pau < mente < exclamação:
    safadezaMIN = latina
if latina < pau < exclamação < mente:
    safadezaMIN = latina
if latina < mente < pau < exclamação:
    safadezaMIN = latina
if latina < mente < exclamação < pau:
    safadezaMIN = latina
if latina < exclamação < pau < mente:
    safadezaMIN = latina
if latina < exclamação < mente < pau:
    safadezaMIN = latina

if mente < pau < latina < exclamação:
    safadezaMIN = mente
if mente < pau < exclamação < latina:
    safadezaMIN = mente
if mente < latina < pau < exclamação:
    safadezaMIN = mente
if mente < latina < exclamação < pau:
    safadezaMIN = mente
if mente < exclamação < pau < latina:
    safadezaMIN = mente
if mente < exclamação < latina < pau:
    safadezaMIN = mente

if exclamação < pau < mente < latina:
    safadezaMIN = exclamação
if exclamação < pau < latina < mente:
    safadezaMIN = exclamação
if exclamação < mente < pau < latina:
    safadezaMIN = exclamação
if exclamação < mente < latina < pau:
    safadezaMIN = exclamação
if exclamação < latina < pau < mente:
    safadezaMIN = exclamação
if exclamação < latina < mente < pau:
    safadezaMIN = exclamação

print(f'A média aritmética entre {pau}, {latina}, {mente} & {exclamação} é {(pau + latina + mente + exclamação) / 4} \nE a diferença entre o maior número e o menor número dentre eles é {safadezaMAX - safadezaMIN}')