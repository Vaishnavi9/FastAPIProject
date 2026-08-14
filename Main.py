from Hero import *
from Weapon import *
from Zombie import *
from Ogre import *


# def battle (e: Enemy):
#     e.talk()
#     e.attack()
#
# zombie = Zombie(15, 3)
# ogre = Ogre(20, 3)
#
# battle(zombie)
# battle(ogre)


# zombie.spread_disease()
#
# ogre = Ogre(15, 5)
#
#
# print(f"{zombie.get_type_of_enemy()} has {zombie.get_health_points()} health points and can do attack of {zombie.get_attack_damage()}")
# print(f"{ogre.get_type_of_enemy()} has {ogre.get_health_points()} health points and can do attack of {ogre.get_attack_damage()}")
#
#
# zombie.talk()
# ogre.talk()


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.get_health_points() > 0 and e2.get_health_points() > 0:
        print('----------------------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.get_health_points()} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.get_health_points()} HP left')
        e2.attack()
        e1.set_health_points(e1.get_health_points() - e2.get_attack_damage())
        e1.attack()
        e2.set_health_points(e2.get_health_points() - e1.get_attack_damage())

    print("------------")
    if e1.get_health_points() > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')

def hero_battle(hero:Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.get_health_points() > 0:
        print('----------------------------')
        hero.attack()
        enemy.special_attack()

        enemy.attack()
        hero.health_points-=enemy.get_attack_damage()
        hero.attack()
        enemy.set_health_points(enemy.get_health_points() - hero.attack_damage)

    print("------------")
    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

# battle(zombie, ogre)
hero = Hero(10, 1)
weapon = Weapon('Sword', 10)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, ogre)