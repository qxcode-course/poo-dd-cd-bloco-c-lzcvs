class Lapiseira:
    def __init__(self, hardness: str, thickness: int, size: int):
        self.__size = size
        self.__thickness = thickness
        self.__hardness = hardness
    def usagepersheet(self):
        if self.__hardness == 'HB':
            self.__size -= 1
        if self.__hardness == '2B':
            self.__size -= 2
        if self.__hardness == '4B':
            self.__size -= 4
        if self.__hardness == '6B':
            self.__size -= 6
    def setSize(self, novo_tamanho: int):
        self.__size = novo_tamanho
    def getthickness(self):
        return self.__thickness
    def gethardness(self):
        return self.__hardness
    def getsize(self):
        return self.__size
    def __str__(self):
        return f"[{self.__size}:{self.__hardness}:{self.__thickness}]"
class Grafite:
    def __init__(self, calibre: int):
        self.__calibre = calibre
        self.__bico: Lapiseira | None = []
        self.__tambor: list[grafite] = []

    def insert(self, grafite: Lapiseira) -> bool:
        if grafite.getthickness() != self.__calibre:
            print('fail: calibre incompatível')
            return False
        if grafite.getthickness() == self.__calibre:
            self.__tambor = grafite
        self.__calibre = grafite
        return True

    def __str__(self) -> str:
        
        return f"calibre: {self.__calibre}, bico: {self.__bico}, tambor: <>"

def main():
    polis = Grafite(' ')
    while True:
        linha: str = input()
        args: list[str] = linha.split(' ')
        print(f'$' + linha)

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            calibre = float(args[1])
            polis = Grafite(calibre)
        elif args[0] == 'show':
            print(polis)
        elif args[0] == 'insert':
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            graf = Lapiseira(thickness, hardness, size)
            polis.insert(graf)
main()