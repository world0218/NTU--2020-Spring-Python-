import pygame
import math

pygame.init()

#視窗大小
win_width = 500   
win_height = 480
win = pygame.display.set_mode((win_width, win_height))

#鼠標
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

#title
pygame.display.set_caption("First Game")

#圖片
bg = pygame.image.load('Game/space.jpg')
aim = pygame.image.load('Game/target.png')

#計時器
clock = pygame.time.Clock()

#音效
bulletSound = pygame.mixer.Sound('Game/bullet.wav')
hitSound = pygame.mixer.Sound('Game/hit.wav')
music = pygame.mixer.music.load('Game/music.mp3')
pygame.mixer.music.play(-1)

#字形
font = pygame.font.SysFont('comicsans', 30, True, True)


#玩家設定
class player(object):
        def draw(self,win):
            x,y = pygame.mouse.get_pos()
            x -= aim.get_width()/2
            y -= aim.get_height()/2
            
            win.blit(aim, (x,y))
           


#物件設定
class projectile(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)



#敵人設定
class enemy(object):
    walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'), pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load('Game/R6E.png'), pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'), pygame.image.load('Game/R9E.png'), pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
    walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'), pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load('Game/L6E.png'), pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'), pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]

    def __init__(self, x, y, width, height,end):
        self.x = x 
        self.y = y
        self.width = width
        self.height= height
        self.end = end
        self.path = [0, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    #走路設定    
    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1


            #血條
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10 ))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5*(10-self.health)), 10 ))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    #移動設定
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    #血量判定
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False

 





def main():
    mouse_x = 0
    mouse_y = 0
    score = 0
    man = player()
    goblin = enemy(100, 300, 64, 64, 450)
    shootLoop = 0
    bullets = []
    run = True
    timer = 0
    play = 0


    #Again
    def play_again(n):
        bigfont = pygame.font.SysFont('comicsans', 80)
        smallfont = pygame.font.SysFont('comicsans', 40)
        if n > 0:
                text = bigfont.render('You Win!', True, (0, 0, 0))
        elif n<0:
                text = bigfont.render('You Lose!', True, (0, 0, 0))
        text2 = smallfont.render('Press SPACE to play again', True, (0, 0, 0))
        textx = 250 - (text2.get_width()/2)
        texty = 200
        textx_size = text2.get_width()
        texty_size = text.get_height()+text2.get_height()
        pygame.draw.rect(win, (255, 255, 255), ((textx - 5, texty - 5), (textx_size + 10, texty_size +10)))

        win.blit(text, (250 - (text.get_width()/2), 200))
        win.blit(text2, (250 - (text2.get_width()/2), 250))

        clock.tick(50)



    

    #畫面刷新
    def redrawGameWindow():
        win.blit(bg, (0,-300))
        
        timer = font.render('Timer: ' + str(ts), 1, (255,255,255))
        win.blit(timer, (180, 10))
        man.draw(win)
        goblin.draw(win)
        if play <0:
            play_again(-1)
        elif play >0 :
            play_again(1)



        for bullet in bullets:
            bullet.draw(win)
        pygame.display.update()


    #mainloop
    while run:
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]

        #timer
        seconds = clock.tick()/1000.0
        if int(timer) >= 30:
            timer = 30
            play = -1
        elif goblin.visible == False:
            play = 1
        else:
            play = 0
            timer += seconds
            displaytimer = math.trunc(timer)
            ts = 30 - displaytimer



        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bulletSound.play()
                if len(bullets) < 5:
                    bullets.append(projectile(mouse_x,mouse_y, 6, (0,0,0)))
               


        #bullet是否擊中
        for bullet in bullets:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play()
                    if goblin.visible == True:
                        goblin.hit()
                        #score += 1
                    bullets.pop(bullets.index(bullet))
                else:
                    bullets.pop(bullets.index(bullet))
            else:
                bullets.pop(bullets.index(bullet))
           


        #鍵盤按鍵判定
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            run = False

            


        
        redrawGameWindow()
repeat = True
while repeat:
    main()


    
pygame.quit()
