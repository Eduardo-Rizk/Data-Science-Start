# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
     palavras = ['uva','melancia','mamao']
     jogoRolando = True


	# Método Construtor
     def __init__(self):
        self.vidas = 6
        self.palavra = random.choice(Hangman.palavras)
        self.tamanho = ["_" for letter in self.palavra]
        self.letrasErradas = []

         # Método para adivinhar a letra
     def adivinha(self):
          print('Bem vindo ao jogo da forca')
          print('Advinhe a palavra abaixo: ')
          print(f"\nChances restantes: {self.vidas}")
          print(f"As letras tentadas foram: {', '.join(self.letrasErradas)}")
          for c in self.palavra:
               print(c, end=" ")
               print()
          tentativa = input("Tente uma letra: ").strip().lower()[0]
          if tentativa in self.palavra:
             posicao = [i for i,v in enumerate(self.palavra) if v==tentativa]
             for indx in posicao:
                self.tamanho[indx] = tentativa  
          else:
             self.letrasErradas.append(tentativa)
             self.vidas -= 1    
            
          
          
            
	# Método para verificar se o jogo terminou
     def terminou(self):
  
          if self.vidas == 0:
               print(f"Você perdeu! A palavra era: {self.palavra}")
               Hangman.jogoRolando = False
               
		
	# Método para verificar se o jogador venceu
     def venceu(self):
          if "_" not in self.tamanho:
               print(f"Parabéns! Você acertou a palavra: {''.join(self.tamanho)}")
               Hangman.jogoRolando = False
		
	# Método para não mostrar a letra no board
     def iteracao(self):
          for c in self.palavra:
               print(c, end=" ")
               print()
		
	# Método para checar o status do game e imprimir o board na tela
     def status(self):
         if self.vidas>0 and self.vidas<6:
             print(board[self.vidas])

jogo1 = Hangman()



