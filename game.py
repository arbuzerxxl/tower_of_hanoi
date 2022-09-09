from copy import deepcopy
from termcolor import cprint
from art import tprint
from pygame import mixer
import sys


class TowerOfHanoi:
    def __init__(self, *args, **kwargs):
        self._tower_1 = [
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self._tower_2 = [[0 for i in range(0, 16)] for i in range(0, 8)]
        self._tower_3 = [[0 for i in range(0, 16)] for i in range(0, 8)]
        self._TOWERS = {"1": self._tower_1, "2": self._tower_2, "3": self._tower_3}

    def isDisplayTowers(self):
        """Show towers in the terminal"""

        levels_of_first_tower = [
            self.convertingTowersToString(tower_level=item) for item in self._tower_1
        ]
        levels_of_second_tower = [
            self.convertingTowersToString(tower_level=item) for item in self._tower_2
        ]
        levels_of_third_tower = [
            self.convertingTowersToString(tower_level=item) for item in self._tower_3
        ]

        connectedTowers = self.joinTowers(
            levels_of_first_tower, levels_of_second_tower, levels_of_third_tower
        )

        for item in connectedTowers:
            print(item)

    def convertingTowersToString(self, tower_level: list) -> str:
        """In base Towers is matrix with values 1 or 0. This func converting values of matrix to str for showing towers in terminal

        Args:
            tower_level (list): Towers consist of 8 levels with 16 values (1 or 0) each.

        Returns:
            str: like '---##---'
        """

        x = ["#" if item else "-" for item in tower_level]
        level_output = "".join(x)
        return level_output

    def joinTowers(self, tower1, tower2, tower3) -> list:
        """Joining all levells of towers (type 'str') to one collection

        Returns:
            list: like [['level_8'], ['level_7'] ...]
        """

        return list(map(self.joinLevel, tower1, tower2, tower3))

    def joinLevel(self, *args: list) -> str:
        """Joining same levels of towers to one level

        Returns:
            str: like '|---##---|--------|--------|'
        """
        output = list(zip(args))
        level = [item[0] + "|" for item in output]
        return "|" + "".join(level)

    def moveDisk(self, current_tower: int, target_tower: int):
        """Move disk from current_tower to target_tower with control game rules

        Args:
            current_tower (int): user_input of tower which we remove the disk
            target_tower (int): user_input of tower which we put the disk
        """

        currentTower = self._TOWERS[str(current_tower)]
        targetTower = self._TOWERS[str(target_tower)]
        freeLevel = self.checkFreePlaceOnTower(tower=targetTower)
        for index, level in enumerate(currentTower):
            if level[7]:
                if freeLevel == 7 or sum(currentTower[index]) < sum(
                    targetTower[freeLevel + 1]
                ):  # Check availability for move disk according game's rules
                    targetTower[freeLevel] = deepcopy(level)
                    currentTower[index] = [0 for i in range(0, 16)]
                    break
                else:
                    print(
                        "Перемещение не возможно. Нельзя положить больший диск на меньший диск"
                    )
                    break
        else:
            print(
                "Перемещение не возможно. На данной башне нет доступных дисков для перемещения"
            )

    def checkFreePlaceOnTower(self, tower: list) -> int:
        """TODO Write description

        Args:
            tower (lisr): Matrix of target tower

        Returns:
            int: If free place was finded, return index of this free level
        """

        for indexLevel in range(len(tower) - 1, -1, -1):

            if tower[indexLevel][7]:
                continue
            else:
                return indexLevel

    def menu(self):
        side = "+------------+".center(82)
        tprint("TowerOfHanoi", font="stforek")
        print(side)
        print("|  1.Играть  |".center(82))
        print(side)
        print("|  2.Инстр.  |".center(82))
        print(side)
        print("|  3.Опции   |".center(82))
        print(side)
        print("|  4.Рекорды |".center(82))
        print(side)
        print("|  5.Выход   |".center(82))
        print(side)
        return int(input())

    def startGame(self):
        self.isDisplayTowers()
        print(
            "Выберите башни для перемещения диска, например с первой на третью: 1 > 3"
        )
        numberTower = input("Место для вашего ввода: ").strip().split(">")
        self.moveDisk(
            current_tower=int(numberTower[0]), target_tower=int(numberTower[1])
        )

    def gameRules(self):
        print("\nХанойская башня является одной из популярных головоломок XIX века. \n\
Даны три стержня, на один из которых нанизаны восемь колец, причём кольца отличаются размером и лежат меньшее на большем. \n\
Задача состоит в том, чтобы перенести пирамиду из восьми колец за наименьшее число ходов на другой стержень. \n\
За один раз разрешается переносить только одно кольцо, причём нельзя класть большее кольцо на меньшее.\n")
        return self.run()
        
    def gameOptions(self):
        pass

    def showRecords(self):
        pass

    def run(self):
        valueMenu = self.menu()
        while True:
            if valueMenu == 1:
                self.startGame()
            elif valueMenu == 2:
                self.gameRules()
            elif valueMenu == 3:
                self.gameOptions()
            elif valueMenu == 4:
                self.showRecords()
            elif valueMenu == 5:
                sys.exit()
            else:
                print("Введены неверные данные! Введите цифру согласно номерам в меню")


if __name__ == "__main__":
    game = TowerOfHanoi()
    game.gameRules()
