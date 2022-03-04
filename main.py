import pygame
import random
pygame.init()  
pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#platform class

class Platform:
    def __init__ (self, xpos, ypos):#constructor
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (random.randrange(0,250), random.randrange(0,250),random.randrange(0,250)),(self.xpos, self.ypos, 100, 20))
    def collide(self, x, y):
        if x>self.xpos and x<self.xpos+100 and y+40> self.ypos and y+40 < self.ypos + 20:
            return self.ypos
        else:
            return False

#player variables
Px= 500 #xpos of player
Py= 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
controller = pygame.joystick.Joystick(0)
controller.init()
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform


p1=Platform(420, 600)
p2 = Platform(100, 750)
p3 = Platform(200, 650)
p4 = Platform(300, 575)
p5  = Platform(175, 500)
while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    if controller.get_button(0):
        keys[UP] = True
    else:
        keys[UP] = False
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
               
   
        vx = controller.get_axis(0)
        Px += int(vx * 10)
         
    #physics section--------------------------------------------------------------------
   
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT
   
    #turn off velocity
    else:
        vx = 0
       
       
      #JUMPING  
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
   
   

   
    #COLLISION
       
    isOnGround = False
    if p1.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p1.collide(Px, Py) - 40 #need to subtract 40

    elif p2.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p2.collide(Px, Py)  - 40
     
    elif p3.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p3.collide(Px, Py)  - 40
       
    elif p4.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p4.collide(Px, Py)  - 40
       
    elif p5.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p5.collide(Px, Py)  - 40
    print(isOnGround)
    #stop falling if on bottom of game screen
    if Py > 760:
        isOnGround = True
        vy = 0
        Py = 760
   
    #gravity
    if isOnGround == False:
        vy+=.3 #notice this grows over time, aka ACCELERATION
   

    #update player position
    Px+=vx
    Py+=vy
   
 
    # RENDER Section--------------------------------------------------------------------------------
           
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
 
    pygame.draw.rect(screen, (100, 200, 100), (Px, Py, 20, 40))
   
   
    #class platforms
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()
    p5.draw()
   
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()
