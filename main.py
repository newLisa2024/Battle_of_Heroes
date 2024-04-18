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

class Hero:
    # Нужно использовать двойное подчеркивание для init. Определяем конструктор.
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    # Методы должны быть выровнены на одном уровне отступа с методом __init__
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

# Класс Game также должен правильно начинаться с отступа на одном уровне с Hero
class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
                if self.computer.is_alive():
                    print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
                else:
                    print(f"{self.computer.name} повержен!")
            else:
                self.computer.attack(self.player)
                if self.player.is_alive():
                    print(f"У {self.player.name} осталось {self.player.health} здоровья.")
                else:
                    print(f"{self.player.name} повержен!")
            turn += 1

        winner = self.player if self.player.is_alive() else self.computer
        print(f"Игра окончена! Победитель: {winner.name}.")

# Пример использования не должен выполняться при каждом импорте модуля.
if __name__ == "__main__":
    game = Game("Игрок", "Компьютер")
    game.start()