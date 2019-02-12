from gildedRose import GildedRose
from sulfuras import Sulfuras
from backstage import Backstage
from agedBrie import AgedBrie


if __name__ == "__main__":

    cheese = Sulfuras("cheese", 5, 80)
    entrance = AgedBrie("entrance", 5, 10)
    magicwater = Backstage("magicwater", 5, 10)
    stock = [cheese, entrance, magicwater]
    
    tienda = GildedRose(stock)
    tienda.update_quality()
    assert cheese.getQuality() == 80, "La calidad debería ser 80"
    assert entrance.getQuality() == 11, "La calidad debería ser 11"
    tienda.update_quality()
    assert entrance.getQuality() == 12, "La calidad debería ser 12"

    for i in range(1,10):
        tienda.update_quality()
    
    assert cheese.getQuality() == 80, "La calidad debería ser 80!"
    assert entrance.getQuality() == 27, "La calidad debería ser 25!!"
    assert magicwater.getQuality() == 0, "La calidad debería ser 0, ha caducado!"
    assert 80 == tienda.getQualityItem(cheese.getName()), "La calidada debería ser 80"
    assert 27 == tienda.getQualityItem(entrance.getName()), "La calidad debería ser 27"
    assert 0 == tienda.getQualityItem(magicwater.getName()), "La calidad debería ser 0"