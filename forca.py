import os
import random

# Desenhar na tela a ASCII conforme cada etapa
def desenhar_bonequinho(etapa_erro):
    etapas = [
        '''
            ____
           |    |
                |
                |
                |
                |
                |
              -----
        ''',
        '''
            ____
           |    |
           O    |
                |
                |
                |
                |
              -----
        ''',
        '''
            ____
           |    |
           O    |
           |    |
                |
                |
                |
              -----
        ''',
        '''
            ____
           |    |
           O    |
          /|    |
                |
                |
                |
              -----
        ''',
        '''
            ____
           |    |
           O    |
          /|\   |
                |
                |
                |
              -----
        ''',
        '''
            ____
           |    |
           O    |
          /|\   |
          /     |
                |
                |
              -----
        ''',
        '''
            ____
           |    |
           O    |
          /|\   |
          / \   |
                |
                |
              -----
        '''
    ]
    print(etapas[etapa_erro])

# Escolher uma palavra aleatória no banco de palavras
def escolher_palavra():
    with open('C:/palavras.txt', 'r', encoding='utf-8') as f:
        palavras = f.read().splitlines()
    palavra = random.choice(palavras)
    while len(palavra) < 5:
        palavra = random.choice(palavras)
    return palavra.upper()

# Função com o jogo da forca
def forca():
    palavra_selecionada = escolher_palavra()
    palavra_exibida = ['_' for _ in palavra_selecionada]
    letras_erradas = []
    etapa_erro = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        desenhar_bonequinho(etapa_erro)
        
        print('Palavra: ', ' '.join(palavra_exibida))
        
        if letras_erradas:
            print('Letras erradas: ', ', '.join(letras_erradas))
        else:
            print('Nenhuma letra errada ainda')

        if etapa_erro > 5:
            print('\nDerrota!\nA palavra era ' + palavra_selecionada)
            break

        letra = input('\n\nDigite uma letra: ').upper()

        if letra in palavra_selecionada:
            for i in range(len(palavra_selecionada)):
                if letra == palavra_selecionada[i]:
                    palavra_exibida[i] = letra
        else:
            if letra not in letras_erradas:
                letras_erradas.append(letra)
                etapa_erro += 1

        if '_' not in palavra_exibida:
            print('\nSucesso!\nA palavra era ' + palavra_selecionada)
            break

# Inicio
forca()
