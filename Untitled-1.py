#Theodore Perron, 3/30/24 color picker in 
import sys, os, pygame

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

from pygame.locals import *
pygame.init()



dim = 255
dimdiv = dim/255
screen = pygame.display.set_mode((dim, dim), pygame.NOFRAME)
x=2
y=2
z=2
closing = 0
yorz = 'y'
countdown = 0
countdownr = 0

fps=60
FramePerSec = pygame.time.Clock()

pygame.display.set_caption('hello!')

frameimg_url = resource_path('95frame.png')

close_url = resource_path('close.png')
closed_url = resource_path('closed.png')

frameimg = pygame.image.load(frameimg_url)

class frame(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		self.image = (frameimg)
		self.rect = self.image.get_rect()
            
framer = pygame.sprite.Group()

framed = frame(0, 0)

framer.add(framed)

class closewin(pygame.sprite.Sprite):
    def __init__(self, x, y, state):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        if state == 1:
            img = pygame.image.load(close_url)
            self.images.append(img)
        else:
            img = pygame.image.load(closed_url)
            self.images.append(img)
        self.image = self.images[self.index]
       # self.rect = self.image.get_rect()
        self.rect = Rect(240, 4, 250, 11)
        print(self.rect)
		
exitButton = pygame.sprite.Group()

exit = closewin(0, 0, 1)

exitButton.add(exit)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.time.delay(60)

    if yorz == "y":
        x,y = pygame.mouse.get_pos()
    else:
        x,z = pygame.mouse.get_pos()
    
    screen.fill(((x/dimdiv), (y/dimdiv), (z/dimdiv))) 

    pygame.draw.circle(screen, (0, 0, 0), (x,dim), 10)

    if yorz == "y":
        pygame.draw.circle(screen, (20, 20, 20), (dim,y), 10)
    else:
        pygame.draw.circle(screen, (0, 0, 0), (dim,z), 10)

    if pygame.mouse.get_pressed()[0]:
        if countdownr == 0:
            print((x/2), (y/2), (z/2))
            countdownr = 5

    if pygame.mouse.get_pressed()[2]:
        if countdown == 0:
            if yorz == "y":
                yorz="z"
            else:
                yorz="y"
            print(yorz)
            countdown = 5

    framer.draw(screen)
    framer.update()
    exitButton.draw(screen)
    exitButton.update()

    if pygame.mouse.get_pressed()[0]:
        for exit in exitButton:
            if exit.rect.collidepoint(x, y):
                closing = 1
    if not pygame.mouse.get_pressed()[0]:
            if closing == 1 and exit.rect.collidepoint(x, y):
                run = False
                print("bye")
            else:
                closing = 0


    if countdown != 0:
        countdown -= 1

    if countdownr != 0:
        countdownr -= 1

    pygame.display.update()

pygame.quit()