from config import store, shop
from exceptions import NotEnoughGoods, NotEnoughSpace, UniqueGoodsOverLoad, NotRequiredGoods
from shop import Shop


class Courier:
    @staticmethod
    def get_goods(title, amount, _from, _to):
        """
            Текст при первозке товара в зависмости от запроса
        """
        print(f"""Курьер забрал {amount} {title} из {_from}
Курьер везет {amount} {title} из {_from} в {_to}
Курьер доставил {amount} {title} в {_to}""")

    @staticmethod
    def check_goods(title, _from):
        """
            Проверка наличия товара в юните при отгрузке
        """
        unit = None
        if _from == 'склад':
            unit = store
        if _from == 'магазин':
            unit = shop
        try:
            if not unit.get_items().get(title):
                raise NotRequiredGoods
        except NotRequiredGoods:
            print(f'в {_from} нет товара {title}')
            quit()

    @staticmethod
    def check_goods_amount(title, amount, _from):
        """
            Проверка наличия нужного количества товара в юните при отгрузке
        """
        try:
            unit = None
            if _from == 'склад':
                unit = store
            if _from == 'магазин':
                unit = shop
            if unit.get_items()[title] < amount:
                raise NotEnoughGoods
        except NotEnoughGoods as error:
            print(error.message)
            quit()

    @staticmethod
    def check_availability(amount, _to):
        """
            Проверка наличия места в юните, принимающем товар
        """
        unit = None
        if _to == 'склад':
            unit = store
        if _to == 'магазин':
            unit = shop
        try:
            if amount > unit.get_free_space():
                raise NotEnoughSpace
        except NotEnoughSpace:
            print(f'Недостаточно места в {_to}. В наличии только {unit.get_free_space()} мест')
            quit()

    @staticmethod
    def check_unique_goods(_to):
        """
            Проверка наличия уникальных товаров и  в юните, принимающем товар
        """
        try:
            unit = None
            if _to == 'склад':
                unit = store
            if _to == 'магазин':
                unit = shop
            if not unit.get_unique_items_count():
                raise UniqueGoodsOverLoad
        except UniqueGoodsOverLoad:
            print(f"""Количество хранения уникальных товаров не должно быть больше 5.
Сейчас в магазине лежат следующие товары: {', '.join(list(Shop.items.keys()))}.""")
            quit()
