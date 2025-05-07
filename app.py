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
