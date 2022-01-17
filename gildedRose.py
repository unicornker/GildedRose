# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.MAX_QUALITY = 50
        self.MIN_QUALITY = 0
        self.MAX_QUALITY_SULFURAS = 80

    def update_quality(self):
        for item in self.items:

            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1

            else: #item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1


            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1



    def update_quality_items(self):

        for index,item in enumerate(self.items):

            if "Sulfuras" in item.name:
                self.update_quality_sulfuras(index)
                continue

            if "Backstage" in item.name:
                self.update_quality_backstage(index)
                continue

            if item.sell_in < 0 and item.name != "Aged Brie":
                item.quality /= 2
                if item.quality < 1:
                    item.quality = 0
                continue

            item.quality += 1 #item.sell_in > 0:

            if item.quality > self.MAX_QUALITY:
                item.quality = self.MAX_QUALITY


    def update_quality_sulfuras(self,index):
        self.items[index].quality = self.MAX_QUALITY_SULFURAS

    def update_quality_backstage(self,index):
        if self.items[index].sell_in < 10 and any([ele > self.MAX_QUALITY for ele in [self.items[index].quality + 2, self.items[index].quality + 3]]):
            self.items[index].quality = self.MAX_QUALITY
        else:
            if self.items[index].sell_in <= 5:
                self.items[index].quality += 3
            else:
                self.items[index].quality += 2




    def update_qulity_ori(self):
        for item in self.items:
            if item.quality < 1:
                item.quality = 0

            if item.quality > self.MAX_QUALITY and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = self.MAX_QUALITY
                if item.sell_in == 0:
                    continue
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in < 10:
                if all(ele > self.MAX_QUALITY for ele in [item.quality + 2, item.quality + 3]):
                    item.quality = self.MAX_QUALITY
                    continue

                if item.sell_in <= 5:
                    item.quality += 3
                else:
                    item.quality += 2

                continue

            if item.sell_in < 0:
                if item.name == "Aged Brie" and item.quality < self.MAX_QUALITY:
                    item.quality += 1
                    continue

                item.quality /= 2
                if item.quality < 1:
                    item.quality = 0

                continue

            else:# item.sell_in > 0:
                item.quality += 1

            if item.quality > self.MAX_QUALITY:
                item.quality = self.MAX_QUALITY


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
