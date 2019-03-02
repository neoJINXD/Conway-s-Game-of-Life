import pygame
from pgGame import gameOfLife

class Window:
    def __init__(self, width, height):
        self.width, self.height = width, height
        pygame.init()
        self.size = 10
        self.game = gameOfLife(self.width, self.height, self.size)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = False
        self.paused = False
        self.background = None
        self.window_rectangle = pygame.rect.Rect(0,0,self.width,self.height)
        ##self.set_background('background.jpg')
        #Pause menu
        font = pygame.font.SysFont("", 60)
        self.pause_text = font.render("PAUSE", True, (255, 0, 0))

    def draw_cell(self):
        self.game.update()

    def draw_grid(self, screen):
        grid_len = self.width//self.size
        for row in range(grid_len):
            for col in range(grid_len):
                grid = pygame.rect.Rect(col*self.size, row*self.size, self.size, self.size)
                pygame.draw.rect(screen, (200,200,200), grid, 1)


    def draw_background(self,screen):
        screen.fill((0,0,0))
        self.draw_grid(screen)
        self.game.draw(screen)

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        print(pos)
                        self.game.cells[pos[0]//self.size][pos[1]//self.size] = 1
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused

            if not self.paused:
                self.draw_cell()
            self.draw_background(self.screen)

            if self.paused:
                self.screen.blit(self.pause_text, (10,10))

            pygame.display.update()
            self.clock.tick(24)
        pygame.quit()


if __name__ == '__main__':
    win = Window(600, 600)
    win.run()
