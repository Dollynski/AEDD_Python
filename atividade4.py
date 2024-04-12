num = int(input("Nº Chinchinlas: "))
anos = int(input("Nº Anos de Criação: "))

total = num

if num < 2:
    print("Deve iniciar com, no mínimo, 2 chinchilas")
else:
    for i in range(1, anos+1):
        print(f"{i}º ano: {total}")
        total = total * 3