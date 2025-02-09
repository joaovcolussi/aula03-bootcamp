numero = int(input("Digite um número entre 1 e 10\n"))
while numero < 1 or numero > 10:
  print("Número fora do intervalo!")
  numero = int(input("Por favor, digite um número entre 1 e 10: "))
print("Número valido!")
