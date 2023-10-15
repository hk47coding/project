import pygame
import random
from assets import load_assets

# Constants
WIDTH, HEIGHT, FPS = 1350, 800, 20

# Game setup
pygame.init()
pygame.display.set_caption("Frog Hopper")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score, frog, pad, PAD_W, PAD_H, pad_positions, preceding_gap = load_assets()

def main():
    game_running = True
    is_paused = True
    menu_shown = True
    
    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    pause_start_time = 0
    elapsed_time_ms = 0

    while game_running:
        start_scene()
        clock.tick(FPS)
        timer(elapsed_time_ms)
        
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = not is_paused
                    if is_paused:
                        pause_start_time = pygame.time.get_ticks() - start_time
                    else:
                        start_time = pygame.time.get_ticks() - pause_start_time

            if not is_paused:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        frog.jump()
                        move_pads(1)
                        
                    if event.key == pygame.K_RETURN:
                        frog.jump()
                        move_pads(1); move_pads(1)

        if not is_paused:
            frog.draw(screen)
            pygame.display.update()
            elapsed_time_ms = pygame.time.get_ticks() - start_time
        else:
            elapsed_time_ms = pause_start_time
        
        if menu_shown:  
            show_menu()
            menu_shown = False  
            
    pygame.quit()

def start_scene():
    # Screen
    screen.fill((255, 255, 255))
    background = pygame.image.load("img/background.png")
    screen.blit(background, (0, 0))
    
    # Score
    font = pygame.font.Font(None, 46)  
    text = font.render(f"Score: {score}", True, (255, 255, 255)) 
    screen.blit(text, (20, 20)) 
    
    # Pads
    for position in pad_positions:
        screen.blit(pad, position)


def timer(elapsed_time_ms):
    font = pygame.font.Font(None, 46)  
    elapsed_seconds = elapsed_time_ms // 1000
    elapsed_milliseconds = elapsed_time_ms % 1000
    text = font.render(f"Time: {elapsed_seconds:02d}.{elapsed_milliseconds:03d} s", True, (255, 255, 255)) 
    screen.blit(text, (20, 100)) 


def move_pads(n):
    global score, preceding_gap
    
    for i in range(len(pad_positions)):
        x, y = pad_positions[i]
        if frog.rect.colliderect(pygame.Rect(x, y, PAD_W, PAD_H)):
            score += 1  # Increment the score when there's a collision
        else:
            print("No collision")
        pad_positions[i] = (x - PAD_W * n, y)

    # If moved off screen to the left, remove and generate another
    if pad_positions[0][0] + 200 < 0:
        pad_positions.pop(0)
    if preceding_gap:
        pad_positions.append((1400, HEIGHT - PAD_H + 100))
        preceding_gap = False
    else:
        if random.random() < 0.5:
            pad_positions.append((1400, HEIGHT - PAD_H + 100))
        else:
            preceding_gap = True


def show_menu():
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                custom_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_p, 'mod': 0, 'unicode': 'p'})
                pygame.event.post(custom_event)
                menu_running = False
                
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text_lines = [
            "Instructions:",
            "",
            "1. Use SPACEBAR to jump 1 pad.",
            "2. Use ENTER key to jump 2 pads.",
            "3. Avoid falling into the water.",
            "",
            "Press 'P' to pause/unpause the game",
            "",
            "Click to start"
        ]
        y_offset = 200
        for line in text_lines:
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y_offset))
            y_offset += 40
        pygame.display.update()
        
        
if __name__ == "__main__":
    main()