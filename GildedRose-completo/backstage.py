from regularItem import RegularItem


class Backstage(RegularItem):
    

    def setQuality(self, valor):
        RegularItem.setQuality(self, valor)
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__


    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.setSell_in()



#CASOS TEST
if __name__ == "__main__":
    
    pato = Backstage("Pato", 11, 20)
    pato.update_quality()
    assert pato.getQuality() == 21
    pato.update_quality()
    assert pato.getQuality() == 23