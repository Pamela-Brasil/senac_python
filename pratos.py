import random

print(30*"-")
print("Vamos jogar Adivinhe o prato!")
print(30*"-")

pratos = ["Gnocchi","Carbonara","Puttanesca","Feijoada","Baião-de-dois","Pastel com Caldo"]
prato_secreto = random.sample(pratos,1)
tentativa = 0
ficha = 5

if prato_secreto == pratos[0] or pratos[1] or pratos[2]:
    print("\nÉ um prato típico da culinária italiana! E não é pizza!\n")
elif prato_secreto == pratos[3] or pratos[4] or pratos[5]:
    print("\nÉ um prato típico da culinária brasileira! E não é churrasco!\n")

print("Você terá 5 chances para acertar!\n\nVamos começar!")



while tentativa <= ficha:
    tentativa += 1
    
    print(f"\nTentativa {tentativa} de {ficha}")
    palpite = input("\nQual o prato você acha que é?\n")

    if palpite !=
    elif palpite == prato_secreto:
        print("\nUAU! Você é bom nisso!\nParabéns você acertou o prato secreto:", prato_secreto)
        break
    else:
        print("\nPoxa! Você não acertou! Vamos tentar de novo!")
        

print("\nQue pena! Você não acertou, o prato secreto era:",prato_secreto)