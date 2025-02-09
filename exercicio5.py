idade = 25
email = "usuario@exemplo.com"

if not 18<= idade <= 65:
  print("Idade fora do intervalo permitido")
elif "@" not in email or "." not in email:
  print("Email inválido")
else:
  print("Dados de usuário válidos")