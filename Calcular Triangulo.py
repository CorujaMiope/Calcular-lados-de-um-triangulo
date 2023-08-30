#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
#será formado:

n1 = int(input('Digite o valor de três retas e veja se elas conseguem formar um triângulo:\n Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

#– EQUILÁTERO: todos os lados iguais
if n1 == n2 and n2==n3:
    print('Os três valores são idênticos, logo formam um triângulo EQUILÁTERO')

#– ISÓSCELES: dois lados iguais, um diferente
elif n1 > n2 or n2 == n3:
    ('Temos dois valores iguais e um diferente, logo teremos um triângulo ISÓCELES')

#– ESCALENO: todos os lados diferente
elif n1 != n2 and n2 != n3 and n3 != n1:
    print('Todos os lados são diferente, logo formam um triângulo ESCALENO')

