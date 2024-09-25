numeros = ["10000,00" , "10700,00" , "11449,00" , "12250,43" , "13107,96" , "14025,52" , "15007,30" , "16057,81" ,
           "17181,86" , "18384,59" , "19671,51" , "21048,52" , "22521,92" , "24098,45" , "25785,34" , "27590,32" ,
           "29521,64" , "31588,15" , "33799,32" , "36165,28" , "38696,84" , "41405,62" , "44304,02" , "47405,30" ,
           "50723,67" , "54274,33" , "58073,53" , "62138,68" , "66488,38" , "71142,57" , "76122,55" , "81451,13"]

quantidade_numeros_total = len(numeros)

numero = [0] * 9

Benford = ["30.103%","17.609%","12.494%","9.691%","7.918%","6.695%","5.799%","5.115%","4.576%"]

for primeiro_numero in numeros:
    primeiro_digito = int(primeiro_numero[0])
    numero[primeiro_digito ] += 1

for i in range(9):
    porcentagem = (numero[i] / quantidade_numeros_total) * 100
    print(f"\nPorcentagem de números {i+1} é: {porcentagem:.2f}% - Porcentagem Benford {i+1} é: {Benford[i]}")