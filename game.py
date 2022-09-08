

from email.mime import base
from copy import deepcopy


def TowerToDisplay(level: list) -> str:

    x = ['#' if item else '-' for item in level]
    level_output = ''.join(x)
    return level_output


def create_base_level(*args: list) -> str:
    output = list(zip(args))
    level = [item[0] + '|' for item in output]
    return '|' + ''.join(level)


def move_disk(current_tower: list, target_tower: list):
    if check_available_move_of_current_tower(current_tower):
        for index, level in enumerate(current_tower):
            if level[7]:
                place = find_place_in_tower(target_tower=target_tower)
                target_tower[place] = deepcopy(level)
                current_tower[index] = deepcopy(target_tower[1])
                break
            else:
                continue
    else:
        print("Перемещение не возможно. На данной башне нет доступных дисков для перемещения")


def check_available_move_of_current_tower(tower):
    if sum(tower[-1]) == 0:
        return False
    else:
        return True
    
    
def find_place_in_tower(target_tower: list):
    for i in range(len(target_tower) - 1, -1, -1):
        
        if target_tower[i][7]:
            continue
        else:
            return i


def isDisplay(tower1, tower2, tower3):
    levels_of_first_tower = [TowerToDisplay(level=item) for item in tower1]
    levels_of_second_tower = [TowerToDisplay(level=item) for item in tower2]
    levels_of_third_tower = [TowerToDisplay(level=item) for item in tower3]
    
    base_game_level = list(map(create_base_level, levels_of_first_tower, levels_of_second_tower, levels_of_third_tower))

    for item in base_game_level:
        print(item)


first_tower = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               ]

second_tower = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

third_tower = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               ]


if __name__ == '__main__':
    isDisplay(first_tower, second_tower, third_tower)
    move_disk(first_tower, second_tower)
    move_disk(first_tower, second_tower)
    move_disk(first_tower, second_tower)
    isDisplay(first_tower, second_tower, third_tower)
