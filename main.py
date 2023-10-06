import numpy as np
n = np.array([[5, 8, 3], 
             [9, 10, 7],
             [4, 10, 7]]
             )
print(n)

#Transposta da array n
n.T
np.transpose(n)

#Estatísticas (min, max, sum, mean, median, etc.)
n.max()
n.max(axis=1)
n.max(axis=0)
n.min()
n.min(axis=0)
n.min(axis=1)
n.sum()
n.sum(axis=0)
n.min(axis=1)
n.mean()
mediana = np.median(n)
print(mediana)
med_1 = np.median(n, axis=0)
print(med_1)

#Aritmética entre arrays P1 e P2
p1 = np.array([1,2,3])
p2 = np.array([8, 9, 10])

soma = p1 + p2

print(f'A soma dos elementos é: {soma}')
p1 + p2

print(f'p1:\n{p1}\n')
print(f'p2:\n{p2}\n')
print(f'p1 @ p2:\n{p1@p2}\n')
print(f'np.dot(p1,p2):\n{np.dot(p1,p2)}')

#fazendo operação com transposta
print(np.transpose(p1+p2))

#Reshape de array

array_1 = np.array([8, 7, 6,5])
array_2 = array_1.reshape(2,2)

print(f'Array unidimensional: {array_1}')
print(f'Array bidimensional: {array_2}')

#Filtro 

f = np.array([[15, 23, 90], [2, 33, 60], [5, 17, 41]])
f
print(f'Filtro números maiores que 16: {f[f>16]}')
print(f'Filtro números pares: {f[f%2==0]}')

