# Создайте простую текстовую боевую игру, где игрок и компьютер управляют
# героями с различными характеристиками. Игра состоит из раундов, в каждом раунде
# игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# 1. Используйте ООП (Объектно-Ориентированное Программирование) для создания
# классов героев.
# 2. Игра должна быть реализована как консольное приложение.
# Классы:
# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье
# в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера,
# пока один из героев не умрет. Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Начинается игра!")
        turn = 0  # 0 - ход игрока, 1 - ход компьютера
        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                self.player.attack(self.computer)
                turn = 1
            else:
                self.computer.attack(self.player)
                turn = 0
            self.status()
        self.declare_winner()

    def status(self):
        print(f"Здоровье {self.player.name}: {self.player.health} HP")
        print(f"Здоровье {self.computer.name}: {self.computer.health} HP")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Запуск игры
player_name = input("Введите ваше имя: ")
game = Game(player_name)
game.start()