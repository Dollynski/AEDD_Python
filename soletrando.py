import time
palavra = input("Palavra: ")

print("Soletrando a palavra...")

for letra in palavra:
    print(letra.upper())
    time.sleep(1)

# ------------------------------- Outro Meio

palavra = input("Palavra: ")

print("Soletrando a palavra...")

for letra in palavra:
    print(letra.upper(), end=" ")
    time.sleep(1)