import random

numero_aleatorio = random.randint(0, 5)


tentativa = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 5): "))

if tentativa == numero_aleatorio:
    print(f"Parabéns! Você acertou. O número era {numero_aleatorio}. Você venceu!")
else:
    print(f"Você errou. O número escolhido pelo computador era {numero_aleatorio}. Você perdeu.")
