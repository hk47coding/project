import pygame
import random
from classes import Frog

def load_assets():
    # Variables
    score = 0
    
    # Asset set-up
    frog = Frog()
    pad = pygame.image.load("img/pad.png")
    PAD_W, PAD_H = pad.get_width(), pad.get_height()
    pad_presence = [True, True, False]
    random.shuffle(pad_presence)
    pad_positions = [(200, pygame.display.get_surface().get_height() - PAD_H + 100)]
    pad_positions += [(x, pygame.display.get_surface().get_height() - PAD_H + 100)
                      for (x, include) in zip(range(600, pygame.display.get_surface().get_width(), PAD_W), pad_presence)
                      if include]
    if pad_presence[2] == False:
        preceding_gap = True
    else:
        preceding_gap = False

    return score, frog, pad, PAD_W, PAD_H, pad_positions, preceding_gap
