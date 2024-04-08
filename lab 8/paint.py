import pygame 
 
WIDTH, HEIGHT = 800, 600   # базовый размер окна 
FPS = 60 
draw = False                # нажатие, зажатие - рисуем, отжали - не рисуем  
lastPos = (0, 0)            # базовая позиция  
radius = 15                 # базовый радиус для инструментов 
color = 'blue'              # базовый цвет 
mode = 'pen'                # базовый режим 
 
BLUE  = (0, 0, 255) 
RED   = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
ORANGE = (255,100,10) 
GREY = (127,127,127) 
YELLOW = (255, 255, 0) 
PURPLE = (153, 0, 153) 
PINK = (255,192,203) 
BROWN = (165,42,42) 
 
pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption('Paint') 
clock = pygame.time.Clock() 
screen.fill(pygame.Color('white')) # закрашиваем в белый цвет, чтобы внутри цикла не обновлялось 
fontRadius = pygame.font.SysFont('Arial', 66, bold = True) 
 
eraser = pygame.transform.scale(pygame.image.load("lab 8\src\eraser.png"), (40, 40))
cleaner = pygame.transform.scale(pygame.image.load("lab 8\src\clean.png"), (40, 40))
pen = pygame.transform.scale(pygame.image.load("lab 8\src\pen.png"), (40, 40))
 
eraser_rect = eraser.get_rect() 
cleaner_rect = cleaner.get_rect() 
pen_rect = pen.get_rect()
 
def drawLine(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
     
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
 
    A = y2 - y1 
    B = x1 - x2 
    C = x2 * y1 - x1 * y2 
 
    if dx > dy: 
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        for x in range(x1, x2): 
            y = (-C - A * x) / B 
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    else: 
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        for y in range(y1, y2): 
            x = (-C - B * y) / A 
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
 
def drawCircle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    x = (x1 + x2) / 2 
    y = (y1 + y2) / 2 
    radius = abs(x1 - x2) / 2 
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width) 
 
 
def drawRectangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    widthr = abs(x1 - x2) 
    height = abs(y1 - y2) 
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width) 
 
while True: 
    # events 
    pygame.draw.rect(screen, pygame.Color('white'), (719, 22, 70, 555)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit()  
        # Нажатия на клавиатуру 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                mode = 'rectangle' 
            if event.key == pygame.K_c: 
                mode = 'circle' 
            if event.key == pygame.K_p: 
                mode = 'pen' 
            if event.key == pygame.K_e: 
                mode = 'erase' 
            if event.key == pygame.K_y: 
                color = 'yellow' 
            if event.key == pygame.K_b: 
                color = 'black' 
            if event.key == pygame.K_g: 
                color = 'gray' 
            if event.key == pygame.K_UP: 
                radius = min(200, radius + 1) # ограничение по максимальному размеру радиуса 
            if event.key == pygame.K_DOWN: 
                radius = max(1, radius - 1) # ограничение по минимальному размеру радиуса 
 
        # Нажатие на мышку 
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True 
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius) 
            prevPos = event.pos 
 
            mx, my = pygame.mouse.get_pos() 
            draw = True 
 
            if 732 <= mx <= 772 and 25 <= my <= 60: 
                mode = 'clean' 
            if 732 <= mx <= 772 and 96 <= my <= 136: 
                mode = 'pen' 
            if 732 <= mx <= 772 and 171 <= my <= 208: 
                mode = 'erase' 
            if 725 <= mx <= 748 and 242 <= my <= 264: 
                color = BLUE 
            if 755 <= mx <= 780 and 242 <= my <= 264: 
                color = RED 
            if 725 <= mx <= 748 and 281 <= my <= 302: 
                color = GREEN 
            if 755 <= mx <= 780 and 281 <= my <= 302: 
                color = BLACK 
            if 725 <= mx <= 748 and 321 <= my <= 343: 
                color = BROWN 
            if 755 <= mx <= 780 and 321 <= my <= 343: 
                color = ORANGE 
            if 725 <= mx <= 748 and 361 <= my <= 384: 
                color = GREY 
            if 755 <= mx <= 780 and 361 <= my <= 384: 
                color = YELLOW 
            if 725 <= mx <= 748 and 401 <= my <= 422: 
                color = PURPLE 
            if 755 <= mx <= 780 and 401 <= my <= 422: 
                color = PINK 
            if 731 <= mx <= 780 and 441 <= my <= 488: 
                mode = 'rectangle' 
            if 731 <= mx <= 780 and 509 <= my <= 567: 
                mode = 'circle' 
 
        # Отпускание мышки 
        if event.type == pygame.MOUSEBUTTONUP:  
            if mode == 'rectangle': 
                drawRectangle(screen, prevPos, event.pos, radius, color) 
            elif mode == 'circle': 
                drawCircle(screen, prevPos, event.pos, radius, color) 
            elif mode == 'clean': 
                screen.fill(WHITE) 
            else: 
                draw = False 
        
        # Перемещение мышки 
        if event.type == pygame.MOUSEMOTION:  
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color) 
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white') 
            lastPos = event.pos 
 
    screen.blit(cleaner, (730, 25))  
    screen.blit(pen, (730, 100)) 
    screen.blit(eraser, (730, 175)) 
    pygame.draw.rect(screen, pygame.Color(color), (730, 440, 50, 50), 10) 
    pygame.draw.circle(screen, pygame.Color(color), (755, 540), 30, 10) 
    pygame.draw.rect(screen, pygame.Color(BLUE), (725, 240, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(RED), (755, 240, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(GREEN), (725, 280, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(BLACK), (755, 280, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(BROWN), (725, 320, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(ORANGE), (755, 320, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(GREY), (725, 360, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(YELLOW), (755, 360, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(PURPLE), (725, 400, 25, 25)) 
    pygame.draw.rect(screen, pygame.Color(PINK), (755, 400, 25, 25)) 
 
    # show radius & color 
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75)) 
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color)) 
    screen.blit(renderRadius, (5, 5)) 
 
    # display 
    pygame.display.flip() 
    clock.tick(FPS)