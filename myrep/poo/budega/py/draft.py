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
        self.__caixas: list[Pessoa | None] = []
        self.__espera: list[Pessoa] = []
        self.__numerocaixas = caixas
    def __str__(self) -> str:
        
        #return f'{self.__caixas}\nEspera: []'
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
            
main()