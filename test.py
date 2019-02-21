from asciimatics.effects import Print
from asciimatics.renderers import BarChart, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys
import math
import time
from random import randint


# def fn():
#     return randint(0, 40)


total = 0

def indivFitness():
    functions = []
    for i in range(1, 9):
        def f(i):
            def innerF():
                return i/10
            return innerF
        functions.append(f(i))

    return functions


# print(indivFitness())

# time.sleep(156)


def barChart(screen):
    scenes = []
    effects = [
        Print(
            screen,
            BarChart(
                10,
                70,
                indivFitness(),
                colour=[c for c in range(1, 8)],
                bg=[c for c in range(1, 8)],
                scale=2.0,
                axes=BarChart.X_AXIS,
                intervals=0.5,
                labels=True,
                border=False),
            x=3,
            y=13,
            transparent=False,
            speed=2)
    ]

    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


# def barChart(screen):
#     scenes = []
#     effects = [
#         Print(
#             screen,
#             BarChart(
#                 10,
#                 40, [fn, fn],
#                 char="=",
#                 gradient=[(20, Screen.COLOUR_GREEN), (30,
#                                                       Screen.COLOUR_YELLOW),
#                           (40, Screen.COLOUR_RED)]),
#             x=13,
#             y=1,
#             transparent=False,
#             speed=2),
#         Print(
#             screen,
#             BarChart(
#                 13,
#                 60,
#                 [wv(1), wv(2),
#                  wv(3), wv(4),
#                  wv(5), wv(7),
#                  wv(8), wv(9)],
#                 colour=Screen.COLOUR_GREEN,
#                 axes=BarChart.BOTH,
#                 scale=2.0),
#             x=68,
#             y=1,
#             transparent=False,
#             speed=2),
#         Print(
#             screen,
#             BarChart(
#                 7,
#                 60, [lambda: time.time() * 10 % 101],
#                 gradient=[
#                     (33, Screen.COLOUR_RED, Screen.COLOUR_RED),
#                     (66, Screen.COLOUR_YELLOW, Screen.COLOUR_YELLOW),
#                     (100, Screen.COLOUR_WHITE, Screen.COLOUR_WHITE),
#                 ] if screen.colours < 256 else [(10, 234, 234), (20, 236, 236),
#                                                 (30, 238, 238), (40, 240, 240),
#                                                 (50, 242, 242), (60, 244, 244),
#                                                 (70, 246, 246), (80, 248, 248),
#                                                 (90, 250, 250), (100, 252,
#                                                                  252)],
#                 char=">",
#                 scale=100.0,
#                 labels=True,
#                 axes=BarChart.X_AXIS),
#             x=68,
#             y=16,
#             transparent=False,
#             speed=2),
#         Print(
#             screen,
#             BarChart(
#                 10,
#                 60,
#                 [wv(1), wv(2),
#                  wv(3), wv(4),
#                  wv(5), wv(7),
#                  wv(8), wv(9)],
#                 colour=[c for c in range(1, 8)],
#                 bg=[c for c in range(1, 8)],
#                 scale=2.0,
#                 axes=BarChart.X_AXIS,
#                 intervals=0.5,
#                 labels=True,
#                 border=False),
#             x=3,
#             y=13,
#             transparent=False,
#             speed=2)
#     ]

#     scenes.append(Scene(effects, -1))
#     screen.play(scenes, stop_on_resize=True)


def demo(screen):
    if screen.width != 132 or screen.height != 24:
        effects = [
            Print(
                screen,
                FigletText("Resize to 132x24"),
                y=screen.height // 2 - 3),
        ]
    else:
        barChart(screen)


while True:
    try:
        Screen.wrapper(barChart)
        sys.exit(0)
    except ResizeScreenError:
        pass
