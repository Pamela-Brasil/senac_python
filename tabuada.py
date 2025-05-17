print(30*"-")
print("Vamos fazer a tabuada!")
print(30*"-")

numero_tab = int(input("Qual número você quer calcular?\n"))

def tabuada():
    contador = 0 
    i = 0 
    while contador < 10:
        contador += 1
        i = i + numero_tab
        print(f"{numero_tab} x {contador} = {i}")

tabuada()