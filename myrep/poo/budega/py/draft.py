class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    
    
    def getnome(self) -> str:
        return self.__nome

        
    def setnome(self, nome: str):
        self.__nome = nome
    
    def __str__(self):
        return f"nome: {self.__nome}"

class Market:
    def __init__(self, caixas: int):
        self.caixas: list[Pessoa | None] = [None] * caixas
        self.espera: list[Pessoa] = []
        self.numerocaixas = caixas

    def arrive(self, pessoa: Pessoa):
        self.espera.append(pessoa)
    
    def call(self, index: int):
        self.espera[index] = self.caixas[0]
        #atualizar valor self.caixas
    def __str__(self) -> str:
        nomes = "[" + ', '.join(self.espera)+ "]" #sequence item 0: expected str instance
        caixas_str = list(map(lambda caixa: '-----' if caixa is None else caixa, self.caixas))
        caixas_str2 = ', '.join(caixas_str)
        resultado = f"Caixas: [{caixas_str2}]\nEspera: {nomes}"
        return resultado


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
main()