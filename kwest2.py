from random import randint
from time import sleep
from data import *
from helpers import *



curent_enemy = 0
while True:
    action = input('''
выберите действие:
1 - бой
2 - тренеровка
3 - информация об игроке
4 - информация о противнике
5 - магазин
6 - получить валюту
7 - показать инвентарь
''')
    if action == '1':
        curent_enemy = fight(curent_enemy)
        if curent_enemy == 7:
            break
    elif action == '2':
        traning_tipe = input('''
    выберите тренеровку:
    1 - тренеровать атаку
    2 - тренеровать оборону
''')
            
    elif action == '3':
        display_player()
        print()
    elif action == '4':
        display_enemy(curent_enemy)
        print()
    elif action == '5':
        shop()
    elif action == '6':
        money()
    elif action == '7':
        display_inventory()
        
