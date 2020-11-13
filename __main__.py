import hideWord
import geneticAlgorithm

import math
import readline

from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
import os
import pyfiglet
import random
import time

MAX_RUN_TIME = 60
SHOW_ANIMATION = True

# FIXED_HIDDEN_WORD = 'hellohello'

if __name__ == "__main__":

    try:
        FIXED_HIDDEN_WORD

        hideWord.hide(FIXED_HIDDEN_WORD)

        geneticAlgorithm.main(math.inf)

    except NameError:

        while True:

            ascii_banner = pyfiglet.figlet_format('Demonstration d' + '\'' +
                                                  'algorithmes genetiques')
            print(ascii_banner)

            # time.sleep(1)

            print(
                'L' + '\'' + 'algorithme décrit sur les pancartes de l' +
                '\'' +
                'exposition va trouver le mot que vous allez soumettre en quelques secondes.'
            )

            # time.sleep(2)

            print()
            FIXED_HIDDEN_WORD = ''
            while len(FIXED_HIDDEN_WORD) < 1:
                FIXED_HIDDEN_WORD = input('Mot à cacher : ')

            bannerWord = geneticAlgorithm.filterSpecials(FIXED_HIDDEN_WORD)

            print(bannerWord)

            ascii_banner = pyfiglet.figlet_format(bannerWord)
            print(ascii_banner)

            print(
                'Nous brouillons maintenant les pistes pour le faire deviner au programme...'
            )

            if SHOW_ANIMATION:

                time.sleep(2)

                def hiding(screen):

                    t0 = time.time()
                    while time.time() - t0 < 3:
                        screen.print_at(
                            random.choice([
                                'Encoder', 'Secret', 'Caché', 'Brouiller',
                                -                                'Mot', 'Inconnu'
                            ]),
                            random.randint(0, screen.width),
                            random.randint(0, screen.height),
                            colour=random.randint(0, screen.colours - 1),
                            bg=random.randint(0, screen.colours - 1))
                        ev = screen.get_key()
                        screen.refresh()

                Screen.wrapper(hiding)
                os.system('cls' if os.name == 'nt' else 'clear')
                ascii_banner = pyfiglet.figlet_format('Le mot est cache')
                print(ascii_banner)
                print('L' + '\'' + 'algorithme n' + '\'' +
                      'en a maintenant plus aucune connaissance.')

                print()
                ascii_banner = pyfiglet.figlet_format(
                    'Appuyez sur Entrer pour demarrer')
                print(ascii_banner)
                input()

            hideWord.hide(FIXED_HIDDEN_WORD)

            geneticAlgorithm.main(MAX_RUN_TIME)

            print()
            input('Appuyez sur Entrer pour relancer le programme')
