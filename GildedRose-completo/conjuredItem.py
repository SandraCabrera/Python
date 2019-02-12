from regularItem import RegularItem


class ConjuredItem(RegularItem):


    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()



#CASOS TEST
if __name__ == "__main__":

    magia = ConjuredItem("Magia", 100, 10)
    magia.update_quality()
    assert magia.getQuality() == 8, 'Error, quality expected 8.'