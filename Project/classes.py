import pygame

class Frog:
    def __init__(self):
        self.x = 200
        self.y = 250
        self.sitting_images = [pygame.image.load(f"img/fsit/fsit-{i}.png") for i in range(1, 20)]
        self.jumping_images = [pygame.image.load(f"img/fjump/fjump-{i}.png") for i in range(1, 10)]
        self.width, self.height = self.sitting_images[0].get_width(), self.sitting_images[0].get_height()
        self.sitting = True
        self.sit_frame = 0
        self.jumping = False
        self.jump_frame = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Create a rect for collision detection

    def jump(self):
        if not self.jumping:
            self.jump_frame = 0
            self.jumping = True

    def draw(self, win):
        if self.jumping:
            if self.jump_frame < len(self.jumping_images):
                win.blit(self.jumping_images[self.jump_frame], (self.x, self.y))
                self.jump_frame += 1
                pygame.time.delay(50)
            else:
                self.jumping = False
                self.jump_frame = 0
        else:
            if self.sit_frame < len(self.sitting_images):
                win.blit(self.sitting_images[self.sit_frame], (self.x, self.y))
                self.sit_frame += 1
                pygame.time.delay(50)
            else:
                self.sitting = False
                self.sit_frame = 0
