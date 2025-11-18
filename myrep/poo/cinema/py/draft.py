class Cliente:
    def __init__(self, id: str, fone: int):
        self.__id = id
        self.__fone = fone
    
    def getfone(self):
        return self.__fone
    
    def setfone(self, telefone: int):
        self.__fone = telefone

    def getid(self):
        return self.__id

    def setid(self, id: str):
        self.__id = id

    def __str__(self) -> str:
        return f'{self.__id}:{self.__fone}'

class Cinema:
    def __init__(self, capacidade: int):
        self.seats: list[Cliente | None] = []
        self.capacidade = capacidade

        for _ in range(capacidade):
            self.seats.append(None)
    
    
    def verificarIndex(self, index:int):
        if index > self.capacidade or index < 0:
            return False
        return True

    def reserve(self, cliente: Cliente, index: int):
        if self.verificarIndex(index) == False:
            print('fail: cadeira nao existe')
            return
        for i in self.seats:
            if i != None and cliente.getid() == i.getid():
                print('fail: cliente ja esta no cinema')
        if self.seats[index] is not None:
            print('fail: cadeira ja esta ocupada')
            return False
        self.seats[index] = cliente
        return 
    def cancelar(self, id: str):
        for i, cliente in enumerate(self.seats):
            if cliente != None and cliente.getid() == id:
                self.seats[i] = None
                break
            else:
                print('fail: cliente nao esta no cinema')
                break

    def __str__(self):
        lugares = ' '.join(['-' if lugar is None else str(lugar) for lugar in self.seats])
        return f'[{lugares}]'

def main():
    cinema = Cinema(0)
    cliente = Cliente(' ', 0)
    while True:
        linha = input()
        args = linha.split(' ')
        print(f'$' + linha)

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(cinema)
        elif args[0] == 'init':
            seats = int(args[1])
            cinema = Cinema(seats)
        elif args[0] == 'reserve':
            nome = args[1]
            fone = int(args[2])
            index = int(args[3])
            cliente = Cliente(nome, fone)
            cinema.reserve(cliente, index)
        elif args[0] == 'cancel':
            nome = args[1]
            cinema.cancelar(nome)
main()