# -*- coding: utf-8 -*-
"""Numero secreto

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jR_eMkU5pqjDt-sZLFZeRifK1LmJR8wN
"""

import random
minimo = 1
maximo = 100
numero_secreto = random.randint(minimo, maximo)
print(numero_secreto)
tentativas = 0

while True:
  tentativas += 1

  palpite = int(input(f"Digite um número entre {minimo} e {maximo}: "))
  if palpite == numero_secreto:
    print(f"Parabéns! você adivinhou o número secreto em {tentativas} tentativas!")
    break
  elif palpite > numero_secreto:
    print(f"O número secreto é MENOR que {palpite}.")
  else:
    print(f"O número secreto é MAIOR que {palpite}.")