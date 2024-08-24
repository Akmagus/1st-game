from random import randint
from time import sleep 
from data import *


def fight(current_enemy):
    # Код драки
        # Драка1
        round = randint(1, 2)
        enemy = enemies[current_enemy]
        enemy_hp = enemies[current_enemy]['hp']

        # Драка 2
        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        input('Enter чтобы продолжить')
        print()
        while player['hp'] > 0 and enemy_hp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}.')
                crit = randint(1, 100)
                if crit < player['attack']:
                    enemy_hp -= player['attack'] * 3
                else:
                    enemy_hp -= player['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            else:
                print(f'{enemy["name"]} атакует {player["name"]}.')
                player['hp'] -= enemy['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            round += 1

        # Окончание драки
        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
        player["hp"] = 100
        return current_enemy

def training(trainingtype):
     energy = 10
     for i in range(1, 101, 20):
            print(f'Тренировка завершена на {i}%')
            sleep(1.5)
        # Игрок выбрал атаку
     if trainingtype == '1':
            player['attack'] += 3
            sleep(5)
            print(f'Вы завершили тренировку, ваша атака теперь составляет {player["attack"]} урона!')
            energy -= 1
        # Игрок выбрал оборону
     elif trainingtype == '2':
            player['armor'] -= 0.5
            print(f'Тренировка завершена, ваша броня теперь защищает на {100 - player["armor"] * 100} урона')
            energy -= 1
        # Игрок выбрал здоровье
     elif trainingtype == '3':
            player['hp'] += 5
            print(f'Тренировка завершена, ваше здоровье теперь составляет {player["hp"]}')
            energy -= 1
     else:
            print('Такой тренировки нет')

def shop():
    print('Добро пожаловать, путник! Что хочешь приобрести?')
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')
    
    item = input()
    if item in player['inventory']:
        print(f'У тебя уже есть {items[item]["name"]}')
    elif player['money'] >= items[item]['price']:
        print(f'Ты успешно приобрёл {items[item]["name"]}')
        player['inventory'].append(items[item]["name"])
        player['money'] -= items[item]['price']
    else:
        print('Не хватает монет :(')
    print()
    print('Буду ждать тебя снова, путник!')
    print()

def display_inventory():
    print(f'У вас есть:')
    for value in player['inventory']:
        print(value)
    print(f'{player["money"]} монет.')
    print()
    if 'Зелье удачи' in player['inventory']:
        potion = input('''Желаешь выпить зелье удачи?
    1 - да
    2 - нет
    ''')
        if potion == '1':
            player['luck'] += 7
            print(f'Готово! Теперь шанс нанести критический урон равен {player["luck"]}%.')
            player['inventory'].remove('Зелье удачи')
    if 'Меч' in player['inventory']:
        mech = input('''Взять меч в руки?
    1 - да
    2 - нет ''')
        if mech == '1':
            player['attack'] += 2.5
            print(f'Теперь ваш урон составляет {player["attack"]} урона.')
            player['inventory'].remove('Меч')
    if 'Шлем' in player['inventory']:
        shlem = input('''Одеть шлем?
    1 - да
    2 - нет ''')
        if shlem == '1':
            player['armor'] -= 0.5
            print(f'Теперь ваша защита составляет {player["armor"]}.')
            player['inventory'].remove('Шлем')

def earn():
    print('Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 500 монет. Соответственно, 33.33% чтобы их потерять')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат....')
    sleep(1.5)
    print('Страшно?!')
    if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет :(')
        player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()

def secret_boss():
        round = randint(1, 2)
        boss_hp = secret_bosses[0]["hp"]
        print(f'Противник - НЕподозрительный человек: НИКТО НЕ СМЕЕТ МНЕ ОТКАЗЫВАТЬ!')
        input('Enter чтобы продолжить')
        print()
        while player['hp'] > 0 and boss_hp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {boss_hp}.')
                crit = randint(1, 100)
                if crit < player['attack']:
                    boss_hp -= player['attack'] * 3
                else:
                    boss_hp -= player['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {boss_hp} - {boss_hp}''')
                print()
                sleep(1)
            else:
                print(f'{secret_bosses[0]["name"]} атакует {player["name"]}.')
                player['hp'] -= secret_bosses[0]['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {secret_bosses[0]['name']} - {boss_hp}''')
                print()
                sleep(1)
            round += 1

        # Окончание драки
        if player['hp'] > 0:
            print(f'Противник - {secret_bosses[0]["name"]}: {secret_bosses[0]["win"]}')
            player["money"] += 1000
        else:
            print(f'Противник - {secret_bosses[0]["name"]}: {secret_bosses[0]["loss"]}')
        player["hp"] = 100
        player["money"] -= player["money"]

def talk():
    print('Привет, хочешь МНОГО денег?')
    vibor = input('''
    1 - хочу
    2 - нет
    ''')
    if vibor == '1':
        print('Для этого нужно всего лишь выпить это зелье.')
        vibor2 = input('''Выпить 'НИ В КОЕМ СЛУЧАЕ НЕ ПОДОЗРИТЕЛЬНОЕ ЗЕЛЬЕ'?
        1 - да
        2 - нет
        3 - кинуть бутылёк в НЕподозрительного человека
        ''')
        if vibor2 == '1':
            print("Вы выпили 'НИ В КОЕМ СЛУЧАЕ НЕ ПОДОЗРИТЕЛЬНОЕ ЗЕЛЬЕ'")
            sleep(2)
            print('Вы заснули и пронулись без денег!')
            print('Он вас обманул!')
            print('У вас теперь 0 монет!')
            player["money"] -= player["money"]
        elif vibor2 == '2':
            print('ДА КАК ТЫ ПОСМЕЛ ОТКАЗАТЬ МНЕ?!')
            secret_boss()
        elif vibor2 == '3':
            print('Вы кинули загадочный бутылёк в НЕподозрительного человека, он заснул.')
            print('Вы поняли что он хотел вас обмануть и забрали его деньги!')
            player["money"] += 1000
    elif vibor == '2':
        print('ДА КАК ТЫ ПОСМЕЛ ОТКАЗАТЬ МНЕ?!')
        secret_boss()