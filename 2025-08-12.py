palavras = []

while True:
    palavra = input().upper()
    if palavra == 'FIM':
        break
    palavras.append(palavra)

frase = ''
for p in palavras:
    if frase != '':
        frase += ' '
    frase += p

vogais = 'AEIOU'
frase_asterisco = ''

for letra in frase:
    if letra in vogais:
        frase_asterisco += '*'
    else:
        frase_asterisco += letra
        
print(frase)
print(frase_asterisco)