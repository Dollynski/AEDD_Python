# A entrada para um clube de pesca custa R$ 20,00 por pessoa e cada pessoa tem direito a levar um
# peixe. Peixes extras custam 12,00. Elabore um programa que leia o número de pessoas de uma
# família que foram ao clube e o número de peixes obtidos na pescaria. Informe o valor a pagar

pessoas = int(input("Quantas pessoas foram ao clube? "))
peixes = int(input("Quantos peixes foram pescados? "))

total = pessoas * 20

if peixes > pessoas:
    extras = peixes - pessoas
    total = total + (extras * 12)

print(f"Pagar R$ {total:.2f}")



