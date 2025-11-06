array: list[int] = []
array2 = [1, 2, 3, 4, 5]
print(array)
print(array2)

leng = len(array2)
print(leng)

counter = 0
for item in array2:
    counter += 1
print(counter)

array.append(1)
print(array)
array.insert(0, 2) # insere posição especifica
print(array)

juncao_array = array + array2
juncao_array.pop(1)
juncao_array.pop(0)
juncao_array.insert(0, 3)
print(juncao_array)

arraygens = ['ametista', 'garnet', 'perola'
,'steven'
]
arraygens.append('lapis lazulli')
gem_removida = arraygens[0]
arraygens.remove('ametista')
print(gem_removida)
print('[ ' + ' '.join(arraygens) + ' ]')

n = 10
lista = list(range(1 + n))
print(lista)

n = 10
lista = [item for item in range(n+1)]
print(lista)

lista = [item for item in range(10 + 1) if item % 2 == 0]
print(lista)
