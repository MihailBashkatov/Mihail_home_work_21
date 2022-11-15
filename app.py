from courier import Courier
from request import Request

if __name__ == '__main__':
    # Получение экземпляра класса Request
    request = Request(input('Введите запрос в формате именительного падежа "Доставить |количество(цифры)| |товар| из |объект| в |объект|"\n'))

    # Проверка наличия запрошенного товара
    Courier.check_goods(request.product, request.from_str)

    # Проверка наличия количества запрошенного товара
    Courier.check_goods_amount(request.product, request.amount, request.from_str)

    # Проверка наличия свободного места в точке выгрузки
    Courier.check_availability(request.amount, request.to_str)

    # Проверка наличия уже хранящихся уникальных товаров
    Courier.check_unique_goods(request.to_str)

    # Сообщение о перевозке товара
    Courier.get_goods(request.product, request.amount, request.from_str, request.to_str)

    # Сообщение о итоговом наличии товаров и их количества после перевозки
    request.define_departure_unit()
