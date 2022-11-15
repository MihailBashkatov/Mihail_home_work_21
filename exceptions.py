class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughGoods(BaseError):
    message = 'Недостаточно товара'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места'


class UniqueGoodsOverLoad(BaseError):
    message = 'В магазине больше 5 уникальных объектов'


class NotRequiredGoods(BaseError):
    message = 'Запрошенный товар отсутсвует'


class NotRequiredUnits(BaseError):
    message = 'Точкой отгрузки или выгрузки долдны быть магазин или склад'
