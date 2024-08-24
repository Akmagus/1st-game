from random import randint
from time import sleep 
from data import *
from helpers import *

# Старт игры
name = input('Введите имя: ')
player['name'] = name
current_enemy = 0
current_boss = 0

# Основной цикл игры
while True:
    action = input(''' Выбери действие:
1 - в бой!
2 - тренировка
3- магазин
4 - показать инвентарь
5 - пойти работать
6 - поговорить с НЕподозрительным человеком  ''')
    
    # Игрок выбрал бой
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 2:
            break
    # Игрок выбрал тренировку
    elif action == '2':
        energy = 10
        trainingtype = input('''Выбери что будешь тренировать
    1 - атаку
    2 - оборону
    3 - здоровье''')
        trainigtype = training(trainingtype)
    elif action == '3':
        shop()
    elif action == '4':
        display_inventory()
    elif action == '5':
        earn()
    if action == '6':
        talk()