texto = "A raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras ={}

for palavra in palavras:
  if palavra in contagem_palavras:
    contagem_palavras[palavra] +=1
  else:
    contagem_palavras[palavra] =1

print(contagem_palavras)