#  Elaborar um programa que leia uma senha e informe se ela é válida ou não. Para ser válida a senha
# deve conter letras maiúsculas, minúsculas e números. Além disso, a senha deve possuir entre 8 e 12
# caracteres

senha = input("Insira uma Senha: ")

if len(senha) < 8 or len(senha) > 12:
    print("\nSenha Inválida: Insira uma senha de 8 a 12 caracteres: ")
else:
    pequenas = 0
    grandes = 0
    numeros = 0
    
    for letra in senha:
        if letra.isupper():
            grandes += 1
        elif letra.islower():
            pequenas += 1
        elif letra.isdigit():
            numeros += 1
    
    if grandes > 0 and pequenas > 0 and numeros > 0:
        print("Ok! Senha Válida")
    else:
        print("Erro... Use letras maísculas, minúsculas e números.")