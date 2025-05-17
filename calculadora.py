print(30*"#")
print("Olá! Vamos calcular!")
print(30*"#")

operacao = int(input("Qual operação você quer?\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))

primeiro_numero = int(input("\nDigite o primeiro valor:\n"))
segundo_numero = int(input("\nDigite o segundo valor:\n"))


def soma(primeiro_numero,segundo_numero):
    return primeiro_numero + segundo_numero

def subtracao(primeiro_numero,segundo_numero):
    return primeiro_numero - segundo_numero 

def multiplicacao(primeiro_numero,segundo_numero):
    return primeiro_numero * segundo_numero

def divisao(primeiro_numero,segundo_numero):
    return primeiro_numero / segundo_numero

if operacao == 1:
    print(f"\n{soma(primeiro_numero,segundo_numero)}")
elif operacao == 2:
    print(f"\n{subtracao(primeiro_numero,segundo_numero)}")
elif operacao == 3:
    print(f"\n{multiplicacao(primeiro_numero,segundo_numero)}")
elif operacao == 4:
    print(f"\n{divisao(primeiro_numero,segundo_numero)}")
else:
    print("Operação inválida!")