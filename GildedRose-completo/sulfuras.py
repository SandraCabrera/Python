from regularItem import RegularItem


class Sulfuras(RegularItem):
    
    
    def update_quality(self):
        assert self.quality == 80, "quality de %s distinta de 80" % self.__class__.__name__
        pass



#CASOS TEST
if __name__ == "__main__":
    
    pato = Sulfuras("Pato", 1, 80)
    pato.update_quality()
    assert pato.getQuality() == 80
    pato.update_quality()
    assert pato.getQuality() == 80