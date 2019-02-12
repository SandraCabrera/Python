from item import Item
from updatable import Updatable


class RegularItem(Item, Updatable):


    def setSell_in(self):
        self.sell_in = self.sell_in - 1


    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality += value
        else:
            self.quality = 0
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__
        

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else: 
            self.setQuality(-2)
        self.setSell_in()


#CASOS TEST
if __name__ == "__main__":
    
    pato = RegularItem("Pato", 100, 10)
    pato.update_quality()
    assert pato.getQuality() == 9

    pata = RegularItem("Pata", 0, 10)
    pata.update_quality()
    assert pata.getQuality() == 8

    ordenador = RegularItem("Ordenador", 100 , 59)
    ordenador.update_quality()
    assert ordenador.getQuality() == 50

    pepito = RegularItem("Pepito", 100, 10)
    pepito.setSell_in()
    assert pepito.getSell_in() == 99