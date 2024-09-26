import pygame, sys, random, math, time
pygame.init() 
pygame.font.init()
  
#Color definitions
BLUE = (10,10,128)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREY=(180, 180, 180)
BEIGE=(255, 228, 168)
DBROWN=(102, 51, 0)


#Screen width
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
  
#Hard points
hpts=[[150,200],[300,200],[450,200],[220,350],[405,350]]
rnum=random.randint(0,3)
  
glist=[]  
  
  
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\Jason_sprite.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.score = 0
  
        self.change_x = 0
        self.change_y = 0
        self.walls = None
  
    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y
  
    def update(self):
        self.rect.x += self.change_x
  
  
        block_hit_list = pygame.sprite.spritecollide(self,self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
  
        self.rect.y += self.change_y
  
        block_hit_list = pygame.sprite.spritecollide(self,self.walls, False)
        for block in block_hit_list:
  
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
  
  
class Guard(pygame.sprite.Sprite):
    def __init__(self,x,y,human):
        super().__init__()
        self.human = human
        self.image = pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\cop.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
  
        self.rect.x = x
        self.rect.y = y
  
    def update(self):
        whit=pygame.sprite.spritecollide(self,wall_group,False)
        if self.human.rect.x > self.rect.x :
            if whit:
                self.rect.x -= 1
                self.rect.y +=1
            else:
                self.rect.x += 1
        if self.human.rect.x < self.rect.x :
            if whit:
                self.rect.x += 1
                self.rect.y +=1
            else:
                self.rect.x -= 1
        if self.human.rect.y > self.rect.y :
            if whit:
                self.rect.y -= 1
                self.rect.x -=1
            else:
                self.rect.y += 1
        if self.human.rect.y < self.rect.y :
            if whit:
                self.rect.y += 1
                self.rect.x -=1
            else:
                self.rect.y -= 1

class Militant(pygame.sprite.Sprite):
    def __init__(self,x,y,human):
        super().__init__()
        self.human = human
        self.image = pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\military_guy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.vel=1
  
        self.rect.x = x
        self.rect.y = y
  
    def update(self):
        self.rect.y+=self.vel
        if self.rect.collidelist(pdlst) >= 0:
            self.vel= -self.vel

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

        
  
  
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
  
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Maze(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(DBROWN)
  
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
class Gem(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\Gem_Sprite.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Base(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\Target.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos

  
def main():
    global rnum
    global wall_group
    global wlist
    global pdlst
      

      
    #Pygame definitions
    pygame_icon = pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\Jason_sprite.png")
    game_over = pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\game_over.png")
    keysimg= pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\keys_wasd.png")
    titleimg= pygame.image.load(r"C:\Users\prmou\Documents\PYGAME TESTS\Pics\Title_pic.png")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption('The Heist')
    pygame.display.set_icon(pygame_icon)
    gem_collect=0
    plc_group = pygame.sprite.Group()
    gc_group = pygame.sprite.Group()
    mc_group = pygame.sprite.Group()
    gem_group = pygame.sprite.Group()
    base_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()
    wlist = pygame.sprite.Group()


    up_pad = pygame.Rect(0,100,600,10)
    bt_pad = pygame.Rect(0,440,1000,300)
    pdlst=[up_pad,bt_pad]
    
      
    #Left wall
    lwall = Wall(0,0,10,600)
    wall_list.add(lwall)
    wall_group.add(lwall)
    #top wall
    twall = Wall(0,100,600,10)
    wall_list.add(twall)
    wall_group.add(twall)
    #Right wall
    rwall = Wall (590,0,10,600)
    wall_list.add(rwall)
    wall_group.add(rwall)
    #Bottom wall
    bwall = Wall (0,440,1000,300)
    wall_list.add(bwall)
    wall_group.add(bwall)

    wlist=[twall, rwall, lwall, bwall]
    
      
    #Player
    player = Player(50,150)
    plc_group.add(player)
    player.walls = wall_list

    #Guards
    guard1 = Guard(350,150, player)
    gc_group.add(guard1)
    guard1.walls = wall_list
    
    #Gem Bases
    b1= Base(hpts[0])
    b2= Base(hpts[1])
    b3= Base(hpts[2])
    b4= Base(hpts[3])
    b5= Base(hpts[4])
    base_group.add(b1)
    base_group.add(b2)
    base_group.add(b3)
    base_group.add(b4)
    base_group.add(b5)

    #Gem
    gem= Gem(hpts[rnum])
    gem_group.add(gem)
      
      
    clock = pygame.time.Clock()

    ADDGUARD =  pygame.USEREVENT + 1
    pygame.time.set_timer(ADDGUARD, 2000)
    
    militcount=0
    ADDMILITANT =  pygame.USEREVENT + 1
    pygame.time.set_timer(ADDMILITANT, 6000)

      
    #Loop
      
    done = False

      
    while not done:
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 48)
        t1 = font2.render("Gems Collected: "+str(gem_collect), True, WHITE)          
        t2 = font1.render("Use            to move", True, WHITE)            
        screen.blit(t1,(275,450))               
        screen.blit(t2,(40,450))            
        screen.blit(keysimg,(20,400))           
        screen.blit(titleimg,(10,0))
        
        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True

            if event.type == ADDGUARD:
                guard1= Guard(10,200,player)
                gc_group.add(guard1)

            if event.type == ADDMILITANT and militcount<3 :
                milit= Militant(550,110,player)
                mc_group.add(milit)
                milit.walls = wall_list
                militcount+=1
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_d:
                    player.changespeed(3,0)
                elif event.key == pygame.K_w:
                    player.changespeed(0,-3)
                elif event.key == pygame.K_s:
                    player.changespeed(0,3)
      
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(3,0)
                elif event.key == pygame.K_d:
                    player.changespeed(-3,0)
                elif event.key == pygame.K_w:
                    player.changespeed(0,3)
                elif event.key == pygame.K_s:
                    player.changespeed(0,-3)


        
        losecm=pygame.sprite.spritecollide(player, gc_group, True) or pygame.sprite.spritecollide(player, mc_group, True)
        if losecm:
            screen.blit(game_over, (-25, 0))
            pygame.display.flip()
            time.sleep(5)
            done = True
        



        gcollect=pygame.sprite.spritecollide(player, gem_group, True)
        if gcollect:
            gem_collect+=1
            rnum=random.choice([0,1,2,3,4])
            gem= Gem(hpts[rnum])
            gem_group.add(gem)




            

        plc_group.update()
        gc_group.update()
        mc_group.update()
        gem_group.update()
        wall_group.update()
        screen.fill(BEIGE)
        base_group.draw(screen)
        plc_group.draw(screen)
        gc_group.draw(screen)
        mc_group.draw(screen)
        wall_group.draw(screen)
        gem_group.draw(screen)

        
        clock.tick(60)


      

  
  
  
    pygame.quit()

main()
