from random import randint
from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
import numpy as np
import time
import os
import pyfiglet


ascii_banner = pyfiglet.figlet_format('Demonstration d'+'\''+'algorithmes genetiques')
print(ascii_banner)

time.sleep(1)

print('L'+'\''+'aglorithme décrit sur les pancartes de l'+'\''+'exposition va trouver le mot que vous allez soumettre en quelques secondes.')

time.sleep(2)


print("Tapez votre mot ici, puis appuyez sur Enter : ")
hw = input()
ascii_banner = pyfiglet.figlet_format(hw)
print(ascii_banner)

print('Nous brouillons maintenant les pistes pour le faire deviner au programme')

time.sleep(2)

def hiding(screen):
    t0 = time.time()
    while time.time()-t0 < 3:
        screen.print_at(np.random.choice(['Encoder', 'Secret', 'Caché', 'Brouiller', 'Mot', 'Inconnu'], 1),
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

Screen.wrapper(hiding)
os.system('cls' if os.name == 'nt' else 'clear')
ascii_banner = pyfiglet.figlet_format('Le mot est cache')
print(ascii_banner)
print('L'+'\''+'algorithme n'+'\''+'en a maintenant plus aucune connaissance.')
time.sleep(1)
print('Lancement de l'+'\''+'algorithme genetique, à vous Mr Yuste.')
