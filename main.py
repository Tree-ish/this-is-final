import pygame

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valentine's Adventure")

# Load Character Sprite
character = pygame.image.load("character.jpg")  # Placeholder, replace with actual sprite
character = pygame.transform.scale(character, (50, 80))

# Game Loop
running = True
while running:
    screen.fill(WHITE)  # Background color
    
    # Draw Roads
    pygame.draw.rect(screen, BROWN, (200, 300, 150, 300))  # Left road
    pygame.draw.rect(screen, BROWN, (450, 300, 150, 300))  # Right road
    
    # Draw Character
    screen.blit(character, (375, 220))  # Place character in center
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()
