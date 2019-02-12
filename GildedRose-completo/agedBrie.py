from regularItem import RegularItem


class AgedBrie(RegularItem):


    def update_quality(self):
        
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()




#CASOS TEST
if __name__ == "__main__":
    
    pato = AgedBrie("Pato", 1, 10)
    pato.update_quality()
    assert pato.getQuality() == 11
    pato.update_quality()
    assert pato.getQuality() == 13