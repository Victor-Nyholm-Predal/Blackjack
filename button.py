import pygame

class button_class():
    def __init__(self, color, x, y, width, height, enabled, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.enabled = enabled
        self.text = text

    def draw(self, window, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, True, (255, 255, 255))
            window.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False