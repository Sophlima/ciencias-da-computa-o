'''Python'''
# Arrays (vetores/matrizes utilizando a biblioteca NumPy)
import numpy as np 

# Criando um array NumPy unidimensional a partir de uma lista 
array = np.array ([1, 2, 3, 4, 5])
prrint("Array:", array)

# Acessando elementos do array:
# - Índices começam em 0
# - Índices negativos acessam a partir do final 
print("Primeiro elemento:", array[0])
print("Último elemento:", array[-1])

#Slicing (fatiamento) de arrays:
# - SIntaxe: [iníio:fim]
# - O índice finl não é incluído 
print ("Elementos do índice 1 a 3 (exclusivo):", array[1:3])

# Listas (estrutura mutável de elementos)
# Criando uma lista básica 
my_list = [1, 2, 3, 4, 5]
print("Lista original:",  my_lyst)

# Adicionando um elemento ao final da lista
my_list. append(6)
print ("Lista após adicionar6:", my_list)

# Inserindo um elemento em posição específica:
# - Sintaxe: insert (índice, valor)
# - Desloca elementos existentes para a direita 
my_lyst. insert (2, 7)
print("Lista após inserir 7 na posição 2", my_list)

# Removendo a primeira ocorrência de um elemento 
print("Último elemento:", array[-1])

my_list.remove(4)
print("Lista após remover o valor 4:", my_list)

# Tuplas (estrutura imutável de elementos)
# Criando uma tupla - usa parênteses ao invés de colchetes
my_tuple = (1, 2, 3, 4, 5)
print("Tupla:", my_tuple)

# Acesso a elementos funciona igual às listas
print("Primeiro elemento da tupla:", my_tuple[0])
print("Último elemento da tupla:", my_tuple[-1])

# Loops (estruturas de repetição)

# Loop for interando sobre elementos de uma lista 
fruits = ["maça", "banana", "morango"]
print("Frutas na lista:")
for fruit in fruits:
    print(fruit)

# Loop while executando enquanto condição é verdadeira 
print("Contagem de 0 a 4:")
i = 0
while i < 5:
    print(i)
    i+=1 #Incrementa o contador

# Loop for com acesso ao índice e elemento simultaneamente usando enumerate
print("Elementos da lista com seus índices:")
my_list = [1, 2, 3, 4, 5]
for indice, elemento in enumarate(my_list):
    print(f"Índice {indice}: {elemento}")

#python 
# Importa o módulo random para seleção aleatória de palavras
import random

# Lista de palavras para o jogo (banco de palavras)
palavras = ['maçã', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    """
    Função principal que gerencia toda a lógica do jogo da forca:
    - Seleção da palavra
    - Controle de tentativas
    - Validação das letras
    - Exibição do estado do jogo
    """
    
    # Seleciona aleatoriamente uma palavra da lista
    palavra_secreta = random.choice(palavras)
    
    # Lista para armazenar as letras descobertas (inicialmente todas ocultas)
    letras_corretas = ['_'] * len(palavra_secreta)
    
    # Lista para registrar letras incorretas digitadas
    letras_erradas = []
    
    # Define o número máximo de tentativas permitidas
    tentativas_restantes = 6

    # Mensagem inicial do jogo
    print("\nBem-vindo ao jogo da forca!")
    print(f"Você tem {tentativas_restantes} tentativas para adivinhar a palavra.\n")

    # Loop principal do jogo: continua enquanto houver tentativas e letras faltando
    while tentativas_restantes > 0 and '_' in letras_corretas:
        # Exibe o progresso atual do jogador
        print(' '.join(letras_corretas))
        
        # Solicita e processa a tentativa do jogador
        tentativa = input("\nDigite uma letra: ").lower()  # Converte para minúscula
        
        # Verifica se a letra está na palavra secreta
        if tentativa in palavra_secreta:
            # Atualiza as letras corretas reveladas
            for indice, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_corretas[indice] = tentativa
        else:
            # Trata letra incorreta
            letras_erradas.append(tentativa)  # Registra a tentativa errada
            tentativas_restantes -= 1         # Reduz o número de tentativas
            
            # Feedback imediato para o jogador
            print(f"\nLetra incorreta! Tentativas restantes: {tentativas_restantes}")
            if letras_erradas:  # Só mostra se houver letras erradas
                print(f"Letras erradas: {', '.join(letras_erradas)}")

    # Verificação final do resultado do jogo
    if '_' not in letras_corretas:
        # Vitória: todas as letras foram reveladas
        print(f"\nParabéns! Você ganhou! A palavra era: {palavra_secreta}")
    else:
        # Derrota: acabaram as tentativas
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")

# Inicia o jogo quando o script é executado
if __name__ == "__main__":
    jogo_da_forca()

#python
# Jogo da Velha (Tic Tac Toe) em Python 

#Tabuleiro representado por uma lista de 9 posições (inicialmente vazias)
board = ['' for _ in range (9)]

def print_board():
    """
    Exibe o tabuleiro atual formatado com as marcações dos jogadores 
    Formato: 
     | X | O | X |
     | O | X | O |
     | X | O | X |
     """
     # Cria cada linha do tabuleiro usando formatação de string
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    # Exibe o tabuleiro completo
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    """
    Gerencia a jogada de um participante
    :para icon: 'X' ou 'O' - símbolo do jogador atual
    """

    # Determina o número do jogador baseado n símbolo
    if icon == 'X':
        number = 1
    elif icon == '0':
        number = 2
    
    print("Sua vez, jogador {}". format(number))

    # Loop para entrada válida da jogada
    while True:
        try:
            # Converte a entrada para número e ajusta para índice 0-8
            choice = int(input("Digite sua jogada (1-9): ").strip()) -1

            # Valida se a posição está disponível 
            if board[choice] == '':
                board[choice] = icon
                break
            else:
                print("\nEsta posição já está ocupada!")
            except (ValueError, IndexError):
                print("\nEntrada inválida! Digite um número entre 1 e 9.")

def is_victory(icon)
    """
    Verifica se o jogador atual venceu
