import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
win.fill((255, 255, 255))
pygame.draw.rect(win, (0, 0, 0), (4, 5, 491, 350), 10)
pygame.display.set_caption("Paint-Version Z")

userColour = 0
font = pygame.font.SysFont('freesansbold.ttf', 25)
bigFont = pygame.font.SysFont('freesansbold.ttf', 40)
brushSize = 2
brushSizeDisplay = "0"

class button(object):
    def __init__(self, colour, location1, location2, name = 0, width = 30, height = 30):
        self.colour = colour
        self.location1 = location1
        self.location2 = location2
        self.name = name
        self.width = width
        self.height = height
        #self.draw()

class colourChoice(button):
    def draw(self):
        pygame.draw.rect(win, self.colour, (self.location1, self.location2, self.width, self.height))
        pygame.draw.rect(win, (153, 0, 153), (self.location1, self.location2, 30, 30), 2)

class usefulChoice(button):
    def draw(self):
        text = font.render(self.name, True, (255, 0, 0))
        pygame.draw.rect(win, self.colour, (self.location1, self.location2, text.get_width() + 5, text.get_height() + 5), 3)
        win.blit(text, (self.location1 + 3, self.location2 + 3))

def redrawGameWindow():
    #pygame.draw.rect(win, (0, 0, 0), (4, 5, 491, 350), 10)
    pygame.draw.rect(win, (255, 255, 255), (0, 350 + 5, 600, 600))
    brushSizeDisplay = bigFont.render(str(brushSize), True, (255, 0, 0))
    win.blit(brushSizeDisplay, (360, 460))
    for x in allButtons:
        x.draw()
    pygame.display.update()
    
red = colourChoice((255, 0, 0), 10, 400)
blue = colourChoice((0, 0, 255), 40, 400)
yellow = colourChoice((255, 255, 0), 70, 400)
green = colourChoice((0, 255, 0), 10, 430)
orange = colourChoice((255, 128, 0), 40, 430)
black = colourChoice((0, 0, 0), 70, 430)

colourList = [red, blue, yellow, green, orange, black]

clear = usefulChoice((0, 0, 0), 300, 400, "Clear")
increaseBrush = usefulChoice((0, 0, 0), 300, 460, "^")
decreaseBrush = usefulChoice((0, 0, 0), 330, 460, "v")

usefulList = [clear, increaseBrush, decreaseBrush]

allButtons = colourList + usefulList

keyHeld = False
run = True

while run:

    mousePresses = pygame.mouse.get_pressed()

    #print(mousePresses)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        #if event.type == pygame.MOUSEBUTTONDOWN:
        if mousePresses[0] == 1:
            pos = pygame.mouse.get_pos()

            for c in allButtons:
                if pos[0] > c.location1 and pos[0] < c.location1 + 30:
                    if pos[1] > c.location2 and pos[1] < c.location2 + 30:
                        #print("3")
                        if c in colourList:
                            userColour = c.colour
                        if c == clear:
                            pygame.draw.rect(win, (255, 255, 255), (0, 0, 500, 350))
                            pygame.draw.rect(win, (0, 0, 0), (4, 5, 491, 350), 10)
                        if c == increaseBrush:
                            brushSize = brushSize + 2
                        if c == decreaseBrush:
                            if brushSize > 2:
                                brushSize = brushSize - 2
                        

            
            if userColour != 0:
                #print("a")
                if pos[0] > 4+10 and pos[0] < 491:
                    #print("b")
                    if pos[1] > 5+10 and pos[1] < 350:
                        #print("c")
                        pygame.draw.circle(win, userColour, (pos[0], pos[1]), brushSize)

    redrawGameWindow()

pygame.quit()
