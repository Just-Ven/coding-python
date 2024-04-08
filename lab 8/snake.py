import pygame
import random

# Initialize Pygame
pygame.init()

# Set game window size
width = 640
height = 480

# Create game window
screen = pygame.display.set_mode((width, height))

# Set game title
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set clock for frame rate
clock = pygame.time.Clock()

# Set font for score display
font = pygame.font.SysFont(None, 30)

# Set initial snake position and velocity
snake_pos = [(width // 2, height // 2)]
snake_vel = (0, -10)

# Set initial food position
food_pos = (random.randint(0, width // 10 - 1) * 10, random.randint(0, height // 10 - 1) * 10)
# Set initial score and level
score = 0
level = 1

# Set initial game speed
speed = 10

# Define function to draw snake and food
def draw_game(snake_pos, food_pos):
    # Clear screen
    screen.fill(black)

    # Draw snake
    for pos in snake_pos:
        pygame.draw.rect(screen, green, (pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, red, (food_pos[0], food_pos[1], 10, 10))

    # Update display
    pygame.display.update()

# Define function to check for collision with walls or snake body
def check_collision(snake_pos):
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        return True
    for pos in snake_pos[1:]:
        if snake_pos[0][0] == pos[0] and snake_pos[0][1] == pos[1]:
            return True
    return False

# Define function to generate random food position
def generate_food(snake_pos):
    while True:
        food_pos = (random.randint(0, width // 10 - 1) * 10, random.randint(0, height // 10 - 1) * 10)
        if food_pos not in snake_pos:
            break
    return food_pos

# Game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and snake_vel[1] != 10:
                snake_vel = (0, -10)
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and snake_vel[1] != -10:
                snake_vel = (0, 10)
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and snake_vel[0] != 10:
                snake_vel = (-10, 0)
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and snake_vel[0] != -10:
                snake_vel = (10, 0)

    # Move snake
    snake_pos.insert(0, (snake_pos[0][0] + snake_vel[0], snake_pos[0][1] + snake_vel[1]))

    if check_collision(snake_pos):
        game_over = True

# Check for food collision
    if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
        # Increase score and speed
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2

        # Generate new food position
        food_pos = generate_food(snake_pos)

    # Remove snake tail if not eating food
    else:
        snake_pos.pop()

    # Draw game
    draw_game(snake_pos, food_pos)

    # Display score and level
    score_text = font.render("Score: " + str(score), True, white)
    level_text = font.render("Level: " + str(level), True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(speed)