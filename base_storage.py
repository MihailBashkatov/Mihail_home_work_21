# Создание абстрактного класса
from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def add(self, title, quantity):
        """
            Добавление товара в юнит
        """
        pass

    @abstractmethod
    def remove(self, title, quantity):
        """
            Удаление товара из юнита
        """
        pass

    @abstractmethod
    def get_free_space(self):
        """
            Получение свободного места в юните
        """
        pass

    @abstractmethod
    def get_items(self):
        """
            Получение всех товаров и количества в юните. Словарь
        """
        pass

    @abstractmethod
    def get_unique_items_count(self):
        """
            Проверка количества уникальных товаров юните
        """
        pass

