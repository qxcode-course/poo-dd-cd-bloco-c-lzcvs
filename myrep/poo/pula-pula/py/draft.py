class Crianca:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
    
    def getnome(self):
        return self.__nome

    def setnome(self, nome_novo: str):
        self.__nome = nome_novo

    def getidade(self):
        return self.__idade
    
    def setidade(self, nova_idade: int):
        self.__idade = nova_idade

    def __str__(self):
        return f'{self.__nome}:{self.__idade}'

class PulaPula:
    def __init__(self):
        self.__brincado: list[Crianca] = []
        self.__esperando: list[Crianca] = []
    
    def chegar(self, crianca: Crianca):
        self.__esperando.append(crianca)
        return True
    
    def enter(self):
        espera = self.__esperando.pop(0)
        self.__brincado.insert(1, espera)

    def leave(self):
        if not self.__brincado:
            return False
        pulando = self.__brincado.pop(0)
        self.__esperando.insert(1, pulando)
    
    def remove(self, nome: str) -> Crianca | None:
        if not self.__brincado and not self.__esperando:
            print(f'fail: {nome} nao esta no pula-pula')
        for crianca in self.__esperando:
            if crianca.getnome() == nome:
                self.__esperando.remove(crianca)
        for crianca in self.__brincado:
            if crianca.getnome() == nome:
                self.__brincado.remove(crianca)

    def __str__(self):
        brincando = ', '.join([str(x) for x in self.__brincado[::-1]])
        esperando = ', '.join([str(x) for x in self.__esperando[::-1]])
        return f'[{esperando}] => [{brincando}]'

def main():
    pulapula = PulaPula()
    while True:
        linha = input()
        args = linha.split(' ')
        print(f"$" + linha)

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(pulapula)
        elif args[0] == 'arrive':
            nome = args[1]
            idade = args[2]
            crianca = Crianca(nome, idade)
            pulapula.chegar(crianca)
        elif args[0] == 'enter':
            pulapula.enter()
        elif args[0] == 'leave':
            pulapula.leave()
        elif args[0] == 'remove':
            nome = args[1]
            pulapula.remove(nome)
main()