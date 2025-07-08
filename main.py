import pygame
import random

pygame.init()

high_score = 0
color_schemes = {
    'dark': {
        'background': (25, 25, 25), 'text': (255, 255, 255), 'snake': (0, 255, 0),
        'food': (255, 0, 0), 'button': (50, 153, 213), 'button_selected': (100, 200, 255)
    },
    'light': {
        'background': (230, 230, 230), 'text': (20, 20, 20), 'snake': (60, 179, 113),
        'food': (220, 20, 60), 'button': (100, 149, 237), 'button_selected': (30, 100, 200)
    }
}
current_theme = 'dark'
DIFFICULTY_SETTINGS = {'Slow': 10, 'Normal': 15, 'Fast': 25}
BLOCK_SIZE_SETTINGS = {'Small': 10, 'Medium': 20, 'Large': 40}
current_speed = DIFFICULTY_SETTINGS['Normal']
current_block_size = BLOCK_SIZE_SETTINGS['Medium']

info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Python Snake Mini-Game by ZaviQ7')

font_style = pygame.font.SysFont("bahnschrift", 45) 
small_font = pygame.font.SysFont("comicsansms", 25)
ui_font = pygame.font.SysFont("consolas", 20)
credit_font = pygame.font.SysFont("bahnschrift", 22) 

def draw_text(text, font, color, surface, x, y, center=False):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    if center:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect

def start_screen():
    """Displays the main menu and handles user settings."""
    global current_theme, current_speed, current_block_size
    while True:
        colors = color_schemes[current_theme]
        screen.fill(colors['background'])
        
        draw_text('Python Snake Game', font_style, colors['text'], screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, center=True)
        draw_text('by Zavi Q (GitHub: ZaviQ7)', credit_font, colors['text'], screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 + 45, center=True)
        
        draw_text(f"Session High Score: {high_score}", small_font, colors['text'], screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + 20, center=True)
        
        mouse_pos = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        draw_text('Difficulty:', small_font, colors['text'], screen, SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2)
        draw_text('Block Size:', small_font, colors['text'], screen, SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT / 2)
        
        for i, (name, speed) in enumerate(DIFFICULTY_SETTINGS.items()):
            btn_rect = pygame.Rect(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 + 40 + i * 50, 120, 40)
            color = colors['button_selected'] if speed == current_speed else colors['button']
            pygame.draw.rect(screen, color, btn_rect)
            draw_text(name, ui_font, colors['text'], screen, btn_rect.centerx, btn_rect.centery, center=True)
            if btn_rect.collidepoint(mouse_pos) and click: current_speed = speed

        for i, (name, size) in enumerate(BLOCK_SIZE_SETTINGS.items()):
            btn_rect = pygame.Rect(SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT / 2 + 40 + i * 50, 120, 40)
            color = colors['button_selected'] if size == current_block_size else colors['button']
            pygame.draw.rect(screen, color, btn_rect)
            draw_text(name, ui_font, colors['text'], screen, btn_rect.centerx, btn_rect.centery, center=True)
            if btn_rect.collidepoint(mouse_pos) and click: current_block_size = size

        start_button_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT * 0.8, 200, 50)
        theme_button_rect = pygame.Rect(SCREEN_WIDTH - 160, 10, 150, 40)
        pygame.draw.rect(screen, colors['button'], start_button_rect)
        draw_text('START GAME', font_style, colors['text'], screen, start_button_rect.centerx, start_button_rect.centery, center=True)
        pygame.draw.rect(screen, colors['button'], theme_button_rect)
        draw_text('Toggle Theme', small_font, colors['text'], screen, theme_button_rect.centerx, theme_button_rect.centery, center=True)

        if start_button_rect.collidepoint(mouse_pos) and click: return
        if theme_button_rect.collidepoint(mouse_pos) and click:
            current_theme = 'light' if current_theme == 'dark' else 'dark'
            pygame.time.delay(100)

        pygame.display.update()
        pygame.time.Clock().tick(30)

def game_loop(snake_speed, block_size):
    """The main loop for the game, with corrected logic."""
    global high_score
    colors = color_schemes[current_theme]

    start_x = round((SCREEN_WIDTH / 2) / block_size) * block_size
    start_y = round((SCREEN_HEIGHT / 2) / block_size) * block_size
    
    snake_pos = [start_x, start_y]
    snake_body = [[start_x, start_y]]
    length_of_snake = 1
    
    direction = 'RIGHT'
    change_to = direction

    def spawn_food():
        while True:
            food_x = random.randrange(0, SCREEN_WIDTH // block_size) * block_size
            food_y = random.randrange(0, SCREEN_HEIGHT // block_size) * block_size
            if [food_x, food_y] not in snake_body:
                return [food_x, food_y]
    food_pos = spawn_food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
        
        direction = change_to

        if direction == 'UP': snake_pos[1] -= block_size
        if direction == 'DOWN': snake_pos[1] += block_size
        if direction == 'LEFT': snake_pos[0] -= block_size
        if direction == 'RIGHT': snake_pos[0] += block_size

        snake_body.insert(0, list(snake_pos))
        
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            length_of_snake += 1
            food_pos = spawn_food()
        else:
            snake_body.pop()

        screen.fill(colors['background'])
        for pos in snake_body:
            pygame.draw.rect(screen, colors['snake'], pygame.Rect(pos[0], pos[1], block_size, block_size))
        pygame.draw.rect(screen, colors['food'], pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))

        if not (0 <= snake_pos[0] < SCREEN_WIDTH and 0 <= snake_pos[1] < SCREEN_HEIGHT): break
        if snake_pos in snake_body[1:]: break
        
        score = length_of_snake - 1
        draw_text(f"Score: {score} | High Score: {high_score}", font_style, colors['text'], screen, 10, 10)
        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

    final_score = length_of_snake - 1
    if final_score > high_score:
        high_score = final_score
    
    while True:
        screen.fill(colors['background'])
        draw_text("Game Over!", font_style, colors['food'], screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/3, center=True)
        draw_text(f"Your Score: {final_score}", small_font, colors['text'], screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 20, center=True)
        draw_text("Press C to Play Again or Q to Quit", small_font, colors['text'], screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20, center=True)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    return

while True:
    start_screen()
    game_loop(current_speed, current_block_size)
