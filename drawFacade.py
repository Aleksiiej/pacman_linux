class DrawFacade:
    def __init__(self, screen, pacman, wallGroup, appleGroup, pygame):
        self.screen = screen
        self.pacman = pacman
        self.wallGroup = wallGroup
        self.appleGroup = appleGroup
        self.pygame = pygame

    def drawGame(self):
        self.pacman.draw(self.screen)
        self.wallGroup.draw(self.screen)
        self.appleGroup.draw(self.screen)
        self.pygame.display.flip()
