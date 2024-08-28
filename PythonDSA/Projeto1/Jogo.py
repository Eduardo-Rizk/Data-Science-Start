import random
from os import name, system

def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac/Linux
    else:
        _ = system('clear')

def iteracao(palavra):
    for c in palavra:
        print(c, end=" ")
    print()

def game():
    limpa_tela()
    print('Bem vindo ao jogo da forca')
    print('Advinhe a palavra abaixo: ')
    
    # Aqui eu estou definindo as palavras que serão utilizadas no meu jogo
    palavras = ['banana', 'melao', 'melancia', 'uva', 'maca']
    palavra = random.choice(palavras)

    tamanho = ["_" for letter in palavra]
    letrasErradas = []
    vidas = 6

    while True:
        limpa_tela()
        iteracao(tamanho)
        print(f"\nChances restantes: {vidas}")
        print(f"As letras tentadas foram: {', '.join(letrasErradas)}")

        tentativa = input("Tente uma letra: ").strip().lower()[0]

        if tentativa in palavra:
            posicao = [i for i, v in enumerate(palavra) if v == tentativa]
            for indx in posicao:
                tamanho[indx] = tentativa
        else:
            if tentativa not in letrasErradas:
                letrasErradas.append(tentativa)
                vidas -= 1

        if "_" not in tamanho:
            limpa_tela()
            print(f"Parabéns! Você acertou a palavra: {''.join(tamanho)}")
            break
        if vidas == 0:
            limpa_tela()
            print(f"Você perdeu! A palavra era: {palavra}")
            break

game()

