import unittest
from gildedRose import Item
from gildedRose import GildedRose

# def decorate_update(fun):
#
#     def update_item(item):
#         updater = GildedRose([fun(item)])
#         updater.update_quality_items()
#
#         # Decorator returns a function
#         return updater.items
#     return update_item


class updater_glidedRose:
    def __init__(self):
        self.lst_items = [
            Item("test", 0, 60),
            Item("test", 2, 30),
            Item("test", -2, 60),
            Item("test", -9, 1),
            Item("Sulfuras, Hand of Ragnaros", 2, 2),
            Item("Aged Brie", -4, 20),Item("Aged Brie", -4, 50),
            Item("Backstage passes to a TAFKAL80ETC concert", 2, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 8, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 2, 48)
        ]
        updater = GildedRose(self.lst_items)
        # updater.update_quality()
        updater.update_quality_items()

class MyTestCase(unittest.TestCase,updater_glidedRose):

    def setUp(self):
        updater_glidedRose.__init__(self)

    def test_max_qulity(self):
        """check if max quality is 50"""
        self.assertEqual(self.lst_items[0].quality, 50)

    def test_close_sell_date(self):
        """check quality is rising"""
        self.assertEqual(self.lst_items[1].quality, 31)

    def test_qulity_degrades_twice(self):
        """check if quality degrades twice as fast by sell_in"""
        self.assertEqual(self.lst_items[2].quality, 30)

    def test_qulity_never_negativ(self):
        """check quality degrades twice as fast by sell_in and not negativ"""
        self.assertEqual(self.lst_items[3].quality, 0)

    def test_sulfuras_quality(self):
        """check quality of Sulfuras item type doesnt change"""
        self.assertEqual(self.lst_items[4].quality, 80)

    def test_Aged_Brie_sell_day_passed(self):
        """check quality of Aged_Brie item type is rising when sell day pass"""
        self.assertEqual(self.lst_items[5].quality, 21)

    def test_Aged_Brie_sell_day_passed_no_exceed_max(self):
        """check if quality of Aged_Brie doesnt exceed the maximum"""
        self.assertEqual(self.lst_items[6].quality, 50)

    def test_Backstage_quality_close_sell_less_5(self):
        """check quality of Backstage item is rising"""
        self.assertEqual(self.lst_items[7].quality, 23)

    def test_Backstage_quality_close_sell_less_10(self):
        """check quality of Backstage item type is rising"""
        self.assertEqual(self.lst_items[8].quality, 22)

    def test_Backstage_quality_close_sell_less_5_and_no_exceed_max(self):
        """check quality of Backstage item doesnt exceed the maximum"""
        self.assertEqual(self.lst_items[9].quality, 50)



if __name__ == '__main__':
    unittest.main()
