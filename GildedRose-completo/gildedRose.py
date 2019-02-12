class GildedRose(object):


    def __init__(self, items):

        self.items = items


    def update_quality(self):

        for item in self.items:
            item.update_quality()


    def getQualityItem(self, name):
        
        for item in self.items:
            if item.getName() == name:
                return (item.getQuality())