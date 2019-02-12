class Item():


    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality 


    def getName(self):
        return self.name


    def getSell_in(self):
        return self.sell_in


    def getQuality(self):
        return self.quality


    def __repr__(self):
        return '%s, %s, %s' % (self.getName(), self.getSell_in(), self.getQuality())   


#CASOS TEST
if __name__ == "__main__":


    pato = Item("Pato",100,20)
    assert pato.getName() == "Pato" 
    assert pato.getSell_in() == 100
    assert pato.getQuality() == 20

    ordenador = Item("Ordenador",52,10)
    assert ordenador.getName() == "Ordenador"
    assert ordenador.getSell_in() == 52
    assert ordenador.getQuality() == 10



