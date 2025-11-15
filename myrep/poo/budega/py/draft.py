class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    
    
    def getnome(self) -> str:
        return self.__nome

        
    def setnome(self, nome: str):
        self.__nome = nome
    
    def __str__(self):
        return self.__nome

class Market:
    def __init__(self, caixas: int):
        self.caixas: list[Pessoa | None] = [None]
        for _ in range(caixas - 1):
            self.caixas.append(None)
        self.espera: list[Pessoa] = []
        self.numerocaixas = caixas

    def arrive(self, pessoa: Pessoa):
        self.espera.append(pessoa)
    
    def call(self, index: int) -> bool:
        if self.caixas[index] != None:
            print("fail: caixa ocupado")
            return False
        if len(self.espera) > 0:
            self.caixas[index] = self.espera.pop(0)
        else:
            print('fail: sem clientes')

    def finish(self, index: int) -> bool:
        if index < 0 or index >= len(self.caixas):
            print('fail: caixa inexistente')
            return False
        if self.caixas[index] is None:
            print('fail: caixa vazio')
            return False
        self.caixas[index] = None
        return True

    def __str__(self) -> str:
        nomes = ['' if espera is None else str(espera) for espera in self.espera]
        nomes_str = ', '.join(nome for nome in nomes if nome)

        caixas_str = ['-----' if caixa is None else str(caixa) for caixa in self.caixas]
        caixas_str2 = ', '.join(caixas_str)

        return f"Caixas: [{caixas_str2}]\nEspera: [{nomes_str}]"


def main():
    mercado = Market(0)
    while True:
        linha = input()
        args: linha[str] = linha.split(' ')
        print(f'$' + linha)
        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(mercado)
        elif args[0] == 'init':
            mercado = Market(int(args[1]))
        elif args[0] == 'arrive':
            mercado.arrive((args[1]))
        elif args[0] == 'call':
            index = int(args[1])
            mercado.call(index)
        elif args[0] == 'finish':
            index = int(args[1])
            mercado.finish(index)
main()