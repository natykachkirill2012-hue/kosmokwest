from random import randint
from time import sleep
from data import *

def display_player():
    print(f"здоровье игрока: {player['hp']}")
    print(f"броня игрока: {player['armor']}")
    print(f"баланс игрока: {player['money']}")
    print(f"атака игрока: {player['attack']}")

def display_enemy(curent_enemy):
    enemy = enemies [curent_enemy]
    print(f"атака противника: {enemy['attack']}")
    print(f"имя противника: {enemy['name']}")
    print(f"здоровье противника: {enemy['hp']}")

def traning(traning_tipe):
    for i in  range(0, 101, 20):
        print(f"тренеровка завершена на {i}%")
        sleep(1.5)
    if traning_tipe == '1':
        player['attack'] += 1
        print(f"тренеровка завершина: теперь уровень атаки равен {player['attack']}")
    elif traning_tipe == '2':
        player['armor'] += 2
        print(f"тренеровка завершина: теперь уровень брони равен {player['armor']}")
    print()
    
def fight(curent_enemy):
    round = randint(1,2)
    enemy = enemies[curent_enemy]
    enemy_hp = enemies[curent_enemy]['hp']
    print(f"противник - {enemy['name']}:{enemy['script']}")
    while player ['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * 3
            else:
                enemy_hp -= player['attack']
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack'] * player['armor']
            sleep(1)
        print(f'''{player['name']}: {player['hp']}
{enemy['name']}: {enemy_hp}''')
        print()
        sleep(1)
        round += 1
    if player ['hp'] > 0:
        print(f"противник - {enemy['name']}:{enemy['win']}")
        curent_enemy += 1
    else:
        print(f"противник - {enemy['name']}:{enemy['loss']}")
    player['hp'] = 100
    return curent_enemy

def  display_inventory():
    print('у вас есть')
    for i in player['inventory']:
        print(i)
    print(f'{player["money"]} монет')
    if 'Зелье удачи' in player['inventory']:
        potion = input('''Желаешь выпить зелье удачи?
    1 - да
    2 - нет
    ''')
        if potion == '1':
            player['luck'] += 7
            print(f'Готово! Теперь шанс нанести критический урон равен {player["luck"]}%')
            player['inventory'].remove('Зелье удачи')
    if 'Зелье силы' in player['inventory']:
        potion = input('''Желаешь выпить зелье силы?
    1 - да
    2 - нет
    ''')
        if potion == '1':
            player['attack'] += 7
            print(f'Готово! Теперь шанс нанести критический урон равен {player["attack"]}%')
            player['inventory'].remove('Зелье силы')

def shop():
    print('добро пожаловать что вы хотите купить')
    print(f'{player["money"]} монет')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')
    item = input()
    if item in player['inventory']:
        print('у вас уже есть такой товар')
    elif player['money'] >= items[item] ['price']:
        print('вы успешно преобрели товар')
        player['inventory'].append(items[item]['name'])
        player['money'] -=  items[item] ['price']
    else:
        print('у вас не хватает монет') 

def money():
    resalt = randint(1,100)
    if resalt < 50 :
        print('вы выиграли 300 монет')
        player['money'] += 300
    else:
        print('вы проиграли 300 монет')
        player['money'] -= 300
    print(f'у вас осталось:{player["money"]}')