# Import libraries and modules
import pygame
import constants
import sprites

# Make a Game class
class Game:
    def __init__(self):
        # Make the game window
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(constants.SIZE)
        pygame.display.set_caption(constants.TITLE)
        self.is_running = True
        
    def new_game(self):
        self.run()
        
    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.events()
            
    def events(self):
        # Define the game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.is_running = False
                
g = Game()

while g.is_running:
    g.new_game()
    