class Grafite:
    def __init__(self, size: str, hardness: str, thickness: int):
        self.__size = size
        self.__hardness = hardness
        self.__thickness = thickness
        
    def usagepersheet(self):
        consumo = 0
        if self.__hardness == 'HB':
            consumo = 1
        if self.__hardness == '2B':
            consumo= 2
        if self.__hardness == '4B':
            consumo = 4
        if self.__hardness == '6B':
            consumo = 6
        self.__thickness -= consumo
        
    def setsize(self, novo_tamanho: int):
        self.__size = novo_tamanho
    def setthicness(self, novo_tamanho: int):
        self.__thickness = novo_tamanho
    def getthickness(self):
        return self.__thickness
    def gethardness(self):
        return self.__hardness
    def getsize(self):
        return self.__size
    def __str__(self):
        return f"[{self.__size}:{self.__hardness}:{self.__thickness}]"
class Lapiseira:
    def __init__(self, calibre: int):
        self.__calibre = calibre
        self.__bico: Grafite | None = None
        self.__tambor: list[Grafite] = []
    
    def insert(self, grafite: Grafite) -> bool:
        if grafite.getsize() != self.__calibre:
            print('fail: calibre incompatível')
            return False
        self.__tambor.append(grafite)
        return True

    def pull(self) -> bool:
        if self.__bico is not None:
            print("fail: ja existe grafite no bico")
            return False
        self.__bico = self.__tambor.pop(0)
        return True

    def remove(self) -> Grafite | None:
        grafite_removido = self.__bico
        self.__bico = None

    def write(self, folhas: int = 1) -> bool:
        minimo_grafite = 10

        if self.__bico is None:
            print('fail: nao existe grafite no bico')
            return False
        
        tamanho_atual = self.__bico.getthickness()
        dureza = self.__bico.gethardness()
        gasto = {'HB': 1, '2B': 2, '4B': 4, '6B': 6}.get(dureza, 1)

        if tamanho_atual <= minimo_grafite:
            print('fail: tamanho insuficiente')
            return 
        if tamanho_atual - gasto < minimo_grafite:
            print('fail: folha incompleta')
            self.__bico.setthicness(10)
            return
        self.__bico.usagepersheet()

            

    def __str__(self) -> str:
        if self.__bico is None:
            colchetes = '[]'
            tambor_str = "<" + ''.join(str(grafite) for grafite in self.__tambor) + ">"
            return f"calibre: {self.__calibre}, bico: {colchetes}, tambor: {tambor_str}"
        tambor_str = "<" + ''.join(str(grafite) for grafite in self.__tambor) + ">"
        return f"calibre: {self.__calibre}, bico: {self.__bico}, tambor: {tambor_str}"

def main():
    while True:
        linha: str = input()
        args: list[str] = linha.split(' ')
        print(f'$' + linha)

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            calibre = float(args[1])
            polis = Lapiseira(calibre)
        elif args[0] == 'show':
            print(polis)
        elif args[0] == 'insert':
            size = float(args[1])
            hardness = args[2]
            thickness = int(args[3])
            graf = Grafite(size, hardness, thickness)
            # print(graf)
            polis.insert(graf)
        elif args[0] == 'pull':
            polis.pull()
        elif args[0] == 'remove':
            polis.remove()
        elif args[0] == 'write':
            polis.write()
main()