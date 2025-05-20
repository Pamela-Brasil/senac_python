
class Tabuada:
    def __init__(self,numero):
        self.numero = numero
        self._resultado = 0

    def soma(self):
        print(f"\nTabuada de Soma para o número {self.numero}:\n")
        for i in range(1,11):
            self._resultado = self.numero + i 
            print(f"{self.numero} + {i} = {self._resultado}")

    def subtracao(self):
        print(f"\nTabuada de Subtração para o número {self.numero}:\n")
        for i in range(1,11):
            self._resultado = self.numero - i 
            print(f"{self.numero} - {i} = {self._resultado}")

    def multiplicacao(self):
        print(f"\nTabuada de Multiplicação para o número {self.numero}:\n")
        for i in range(1,11):
            self._resultado = self.numero * i 
            print(f"{self.numero} x {i} = {self._resultado}")

    def divisao(self):
        print(f"\nTabuada de Divisão para o número {self.numero}:\n")
        for i in range(1,11):
            self._resultado = self.numero / i 
            print(f"{self.numero} / {i} = {self._resultado}")


print(30*"-")
print("Vamos fazer a tabuada!")
print(30*"-")

numero_tab = int(input("Qual número você quer calcular?\n"))

tabuada = Tabuada(numero_tab)

tabuada.soma()
tabuada.subtracao()
tabuada.multiplicacao()
tabuada.divisao()





