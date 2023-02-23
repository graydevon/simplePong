import pygame
import random

# Initialize Pygame
pygame.init()

# Define the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the font
font = pygame.font.Font(None, 40)

# Define the ball
ball_size = 20
ball_x = screen_width // 2 - ball_size // 2
ball_y = screen_height // 2 - ball_size // 2
ball_speed_x = 5 * random.choice((-1, 1))
ball_speed_y = 5 * random.choice((-1, 1))

# Define the paddles
paddle_width = 15
paddle_height = 100
paddle_speed = 5
left_paddle_x = 50
left_paddle_y = screen_height // 2 - paddle_height // 2
right_paddle_x = screen_width - 50 - paddle_width
right_paddle_y = screen_height // 2 - paddle_height // 2

# Define the score
left_score = 0
right_score = 0

# Define the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    elif keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    elif keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
        right_paddle_y += paddle_speed
    
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Bounce the ball off the top and bottom walls
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y = -ball_speed_y
    
    # Handle collision with the left paddle
    if ball_x <= left_paddle_x + paddle_width and \
        left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x
    
    # Handle collision with the right paddle
    if ball_x + ball_size >= right_paddle_x and \
        right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x
    
    # Handle scoring
    if ball_x <= 0:
        right_score += 1
        ball_x = screen_width // 2 - ball_size // 2
        ball_y = screen_height // 2 - ball_size // 2
        ball_speed_x = 5 * random.choice((-1, 1))
        ball_speed_y = 5 * random.choice((-1, 1))
    elif ball_x + ball_size >= screen_width:
        left_score += 1
        ball_x = screen_width // 2 - ball_size // 2
        ball_y = screen_height // 2 - ball_size // 2
        ball_speed_x = 5 * random.choice(-1,)
