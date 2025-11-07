import random
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


arrayaleatorio = [random.randint(0, 100) for _ in range(10)] # _ placeholder
print(arrayaleatorio)
print(arrayaleatorio[2])
for i, valor in enumerate(arrayaleatorio):
    print(f'indice: {i}, valor: {valor}')

arrayaleatorio = [random.randint(0, 100) for _ in range(10) if _ % 2 == 0]
print(arrayaleatorio)

class Foo:
    def __init__(self, x: int):
        self.x = x
    def __str__(self):
        return f'Foo{self.x}'
    def __repr__(self):
        return self.__str__()

lista_vazia: list[int] = []
lista_preenchida: list[int] = [1, 3, 4, 5]
lista_preencida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

lista_vazia.append(1)
lista_preenchida.append(Foo(4))
print(lista_preenchida)