#!/usr/bin/env python3
import random

from pag import GameWorld
from pag import CommandLineInterface
from pag import classes

gameworld = GameWorld(classes.location_list)
cli = CommandLineInterface(gameworld)


class Snail(classes.Creature):

    def __init__(self):
        super().__init__(name='snail',
                         hp=2,
                         description='There is a snail on the ground.')


class Orc(classes.Baddie):

    def __init__(self):
        super().__init__(name='orc',
                         hp=50,
                         description='There is an orc in '
                                     'the room.',
                         power=random.randint(20, 50))


class Ghost(classes.Baddie):

    def __init__(self):
        super().__init__(name='ghost',
                         hp=99999999,
                         description='Wooooo',
                         power=0.01)


class GiantSpider(classes.Baddie):

    def __init__(self):
        super().__init__(name='giant spider',
                         hp=500,
                         description='The spider is large and ugly.',
                         power=15,
                         drop_items={ToiletPaper(): 1})


class Bear(classes.Baddie):

    def __init__(self):
        super().__init__(name='bear',
                         hp=200,
                         description='The bear growls at you.',
                         power=30)


class Sword(classes.Weapon):

    def __init__(self):
        super().__init__(name='sword',
                         description='The sword is small and has an el'
                         'vish look to it.',
                         loc_description='There is a small sword here.',
                         weight=75,
                         power=random.randint(90, 150))

    def examine(self, glowing):
        print(self.description, end='')
        if glowing:
            print(' It is glowing light blue.')
        else:
            print()


class HealthPot(classes.Food):

    def __init__(self):
        super().__init__(name='health potion',
                         description='The potion looks disgusting but '
                                     'is probably good for you.',
                         loc_description='There is a health potion here.',
                         weight=2,
                         health=100)


class Bread(classes.Food):

    def __init__(self):
        super().__init__(name='bread',
                         description='The bread is slightly stale but '
                         'looks wholesome.',
                         loc_description='There is a loaf of bread.',
                         weight=1,
                         health=30)


class ToiletPaper(classes.Item):

    def __init__(self):
        super().__init__(name='toilet paper',
                         description='The toilet paper is labeled "X-t'
                         'raSoft.',
                         loc_description='A roll of toilet paper is in '
                         'the room.',
                         weight=1)


class Stick(classes.Item):

    def __init__(self):
        super().__init__(name='stick',
                         description='The stick is long and thick. It '
                         'looks like it would be perfect '
                         'for bashing things with.',
                         loc_description='There is a random stick on '
                         'the ground.',
                         weight=3)


class Paper(classes.Item):

    def __init__(self, text=''):
        super().__init__(name='paper',
                         description=text,
                         loc_description='On a table is a paper labeled'
                                         ' NOTICE.',
                         weight=1)


class Coconuts(classes.Item):

    def __init__(self):
        super().__init__(name='coconut halves',
                         description='The coconuts make a noise like '
                                     'horse hooves when banged together.',
                         loc_description='Also on the table are two coc'
                                     'onut halves that look like they '
                                     'probably were carried here by a '
                                     'swallow.',
                         weight=2)


class BlackPit(classes.Location):

    def __init__(self):
        super().__init__(name='A mountain of gold and jewels',
                         items=[],
                         creatures=[],
                         exits={},
                         description='You are in a dank, dirty pit. Yo'
                                     'u don\'t know why you are here i'
                                     'nstead of being on a mountain of'
                                     ' gold and jewels.',
                         show_name_when_exit=True,
                         dark=True)
        self.first_time = True

    def give_info(self, full_info, light):
        if self.first_time:
            print('You run towards the amazing riches...without noticing the giant hole at your feet.')
            print()
            self.name = 'Black Pit'
            self.first_time = False
            super().give_info(True, light)
        else:
            super().give_info(full_info, light)


class DarkTunnel(classes.Location):

    def __init__(self):
        super().__init__(name='Dark Tunnel',
                         items=[],
                         creatures=[Orc(), Orc(), Orc(), Orc()],
                         exits={},
                         description='You are in a featureless dark tunnel.',
                         show_name_when_exit=False,
                         dark=True)


bathroom = classes.Location('Bathroom', [ToiletPaper()], [], show_name_when_exit=True)
bathroom.description = 'There is a toilet and a sink here. They seem'\
                       ' out of place since this is 600 B.C.'
home = classes.Location('Home', [Paper(), classes.Lantern()], [],
                        show_name_when_exit=True)
home.items[0].description = '''NOTICE:
These lands have recently become infested with the servants of evil.
Currently, the main problem is the Legendary Dragon of Nogard (the LDN),
a very powerful lizard that threatens to destroy everything we live for.
It would be greatly appreciated if you would help exterminate the
creatures currently endangering the world. There may be some reward to
anyone who defeats the Legendary Dragon of Nogard that has been ravaging
the nation.
We have left a weapon for you in a nearby chest that might be locked in
a chest. You may have to break it open. We really didn't plan this very well.'''
home.description = 'You are in a familiar cabin made out of logs. '\
                   'There is a pleasantly warm fire in the fireplace '\
                   'and a comfortable-looking armchair beside it.'
start = classes.Location('Start', [classes.Mirror()], [], history=False, start=True)
start.description = 'You are in a small room with concrete walls and '\
                    'no windows.'
closet = classes.Location('Closet', [Stick()], [], show_name_when_exit=True)
closet.description = 'You are in a closet that is full of cobwebs.'
attic = classes.Location('Attic', [Bread(), HealthPot()], [GiantSpider()],
                         show_name_when_exit=True, dark=True)
attic.description = 'The attic has been obviously unused for many year'\
                    's. There are large spiderwebs everywhere.'
backyard = classes.Location('Backyard', [], [Snail()])
backyard.description = 'You are in the back yard of your house.'
frontyard = classes.Location('Front Yard', [classes.Chest([Sword()], True)], [])
frontyard.description = 'You are in your front yard.'
homenorth = classes.Location('North of Home', [], [], show_name_when_exit=False)
homenorth.description = 'You are at the side of your house.'
homesouth = classes.Location('South of Home', [], [], show_name_when_exit=False)
homesouth.description = 'You are at a side of your house with a window visible.'
creepyforest = classes.Location('Creepy forest', [], [Ghost()], show_name_when_exit=True)
creepyforest.description = 'You are in a spooky forest.'
forest = classes.Location('Forest', [], [Bear()], show_name_when_exit=True)
forest.description = 'You are in a forest. There is a sign that says '\
                     '"This is not the spooky forest of the East. Stay'\
                     ' away from there!"'
blackpit = BlackPit()
dtn = DarkTunnel()
dts = DarkTunnel()
deadend = classes.Location(
    'Dead End', [], [], show_name_when_exit=True)
deadend.description = 'You are at a dead end.'
### All this exit stuff is nasty. Need a map.
home.exits = {'north': bathroom, 'south': closet, 'east': backyard,
              'west': frontyard, 'up': attic}
bathroom.exits = {'south': home}
closet.exits = {'north': home}
attic.exits = {'down': home}
backyard.exits = {'west': home, 'east': creepyforest,
                  'northwest': homenorth, 'southwest': homesouth}
creepyforest.exits = {'west': backyard}
frontyard.exits = {'east': home, 'west': forest, 'northeast': homesouth,
                   'southeast': homesouth}
forest.exits = {'east': frontyard}
homenorth.exits = {'southwest': frontyard, 'southeast': backyard}
homesouth.exits = {'northwest': frontyard, 'northeast': backyard,
                   'south': blackpit}
blackpit.exits = {'north': dtn, 'south': dts}
dtn.exits = {'south': blackpit}
dts.exits = {'north': blackpit, 'south': deadend}
deadend.exits = {'north': dts}

cli.play()
