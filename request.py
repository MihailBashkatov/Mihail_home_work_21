# Импорт объектов классов Store, Shop
from config import store, shop

#Импорт ошибки
from exceptions import NotRequiredUnits


class Request:

    def __init__(self, text: str):
        try:
            self.text = text.lower().strip().split()
            self.from_str = self.text[4]
            self.to_str = self.text[6]
            self.amount = int(self.text[1])
            self.product = self.text[2]

            if 'магазин' not in [self.from_str, self.to_str] or 'склад' not in [self.from_str, self.to_str]:
                raise NotRequiredUnits
        except NotRequiredUnits as e:
            print(e.message)
            quit()

    def define_departure_unit(self):
        """
            Определение юнитов, где товар забирается и куда отвозится. Подсчет товаров в юнитах
        """
        unit_1 = None
        unit_2 = None
        if self.from_str == 'склад':
            unit_1 = store
            unit_2 = shop
        elif self.from_str == 'магазин':
            unit_1 = shop
            unit_2 = store
        unit_1.remove(self.product, self.amount)
        print(f'В {self.from_str}е хранится:')
        for key, value in unit_1.get_items().items():
            print(key, value)
        print('*'*10)
        unit_2.add(self.product, self.amount)
        print(f'В {self.to_str} хранится:')
        for key, value in unit_2.get_items().items():
            print(key, value)
