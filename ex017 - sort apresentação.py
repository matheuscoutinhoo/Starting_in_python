'''O mesmo professor do desafio 016 quer sortear a ordem de apresentação de trabalhos 
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
sort = shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))