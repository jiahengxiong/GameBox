'''如果鼠标移出界面就会出现错误'''
import pygame,random,sys
from pygame.locals import *

pygame.init()

#设置窗口大小
WindowWidth=400        
WindowHeight=710     

#设置黑白颜色
White=(255,255,255)     
TEXTCOLOR = (0, 0, 0)

#设置背景图片background
background=pygame.image.load('back.jpg')

#设置帧速度和字体
FPS=60
fpsclock=pygame.time.Clock()
font = pygame.font.SysFont('等线 Light', 40)

#设置窗口和标题
windowSurface = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('plane')

#加载图片
liferescue=pygame.image.load("prop_type_1.png")         #补给包
kick=pygame.image.load("enemy0.png")                    #敌方飞机
boss1=pygame.image.load('boss.png')                     #敌方boss
player=pygame.image.load("J-20.jpg")                    #玩家飞机
bullet=pygame.image.load("playerbullet.jpg")                #玩家子弹
enemybullet=pygame.image.load('enemybullet.jpg')           #敌方子弹
boss1bullet=pygame.image.load('bossbullet.png')             #boss子弹

#获取位置
playerrect=player.get_rect()
bulletrect=bullet.get_rect()
boss1rect=boss1.get_rect()

#加载音乐
pygame.mixer.music.load('コナミ矩形波倶楽部 - American Patrol.mp3')

#设置等待按键函数
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:               #按esc退出 
                    pygame.quit()
                    sys.exit()
                return

#设置检测小飞机和飞机的碰撞的函数
def playerhashitbaddies(playerrect, baddies):
    for b in baddies:
        if playerrect.colliderect(b['rect']):           
            return True
    return False

#设置输出函数
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#设置最高分数和是否播放音乐
topscore=0
music=True

#设置背景颜色和开始界面
windowSurface.blit(background,(0,0))
drawText("Plane", font, windowSurface, WindowWidth / 3+25, WindowHeight / 3)
drawText("Press a key to play", font, windowSurface, WindowWidth / 3-50, WindowHeight / 3+50)
pygame.display.update()
waitForPlayerToPressKey()                               #等待玩家按键开始

#无限播放音乐
if music:
    pygame.mixer.music.play(-1, 0.0)



#开始主一循环
while True:

    #在初始位置上显示飞机
    windowSurface.blit(player, (200, 700))

    #设置小敌对飞机
    baddies=[]
    baddieAddCounter = 0

    #设置生命包和我方飞机生命
    life=1
    lifes=[]
    lifeaddcounter = 0

    #设置加分金条
    goldaddcounter=0
    golds=[]

    #设置我方子弹
    bulletaddcounter=0
    bulletcounter = 15
    bullets=[]

    #设置敌方小飞机子弹
    enemybullets=[]

    #设置地方大飞机一
    boss1addcounter=0
    bosses1=[]
    boss1counter=0

    #设置地方大飞机一子弹
    boss1bullet9=0
    bosses1totalbullet=[]

    #设置成绩
    score=0



    #开始主二循环
    while True:
        windowSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:

                #设置暂停音乐功能  按s停止bgm
                if event.key == K_s:
                    pygame.mixer.music.stop()
 
                #设置开始音乐功能  按c键开始bgm
                if event.key==K_c:
                    pygame.mixer.music.play(-1,0.0)

                #设置我方子弹限制
                if event.key==K_SPACE:
                    if bulletcounter>0:
                        newbullet={'rect': pygame.Rect(playerrect.centerx,playerrect.centery, 20,20),
                                   'speed': 3,
                                   'surface': pygame.transform.scale(bullet, (20,20))
                                   }            
                        bullets.append(newbullet)
                        bulletcounter-=1

            #设置我方飞机移动
            if event.type == MOUSEMOTION:
                playerrect.centerx = event.pos[0]
                playerrect.centery = event.pos[1]

        #打印我方飞机和更新
        windowSurface.blit(player,playerrect)
        pygame.display.update()

        #打印我方飞机子弹
        for bu in bullets:
            bu['rect'].move_ip(0, -bu['speed'])

        for bu in bullets:
            windowSurface.blit(bu['surface'], bu['rect'])

        #打印敌方小飞机
        bulletaddcounter+=1
        if bulletaddcounter==100:
            bulletaddcounter=0
            bulletcounter=6

        baddieAddCounter += 1
        if baddieAddCounter == 15:
            baddieAddCounter = 0
            baddieSize = random.randint(20, 30)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WindowWidth - baddieSize), 0 - baddieSize, baddieSize,
                                             baddieSize),
                         'speed': random.randint(2,4),
                         'surface': pygame.transform.scale(kick, (baddieSize, baddieSize)),
                         }

            baddies.append(newBaddie)

        for b in baddies:
            b['rect'].move_ip(0, b['speed'])

        for b in baddies:
            if b['rect'].top>WindowHeight:
                baddies.remove(b)

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        #打印敌方小飞机子弹
        for b in baddies:
            ifenemybullet = random.randint(0,66666)
            if ifenemybullet <= 10:
                enemybulletSize=15
                newbullet = {'rect': pygame.Rect(b['rect'].centerx,b['rect'].centery, enemybulletSize, enemybulletSize),
                             'speed': random.randint(2, 4),
                             'surface': pygame.transform.scale(enemybullet, (enemybulletSize, enemybulletSize)),
                             }
                enemybullets.append(newbullet)

        for nb in enemybullets:
            nb['rect'].move_ip(0, nb['speed'])

        for nb in enemybullets:
            if nb['rect'].top>WindowHeight:
                enemybullets.remove(nb)

        for nb in enemybullets:
            windowSurface.blit(nb['surface'],nb['rect'])

        pygame.display.update()

        
        #打印生命包
        lifeaddcounter += 1
        if lifeaddcounter == 1333:
            lifeaddcounter = 0
            lifesize = random.randint(35, 45)
            newlife = {'rect': pygame.Rect(random.randint(0,WindowWidth),0, lifesize, lifesize),
                       'speed': random.randint(2, 4),
                       'surface': pygame.transform.scale(liferescue, (lifesize, lifesize)),
                       }
            lifes.append(newlife)
        for l in lifes:
            l['rect'].move_ip(1, l['speed'])

        for l in lifes[:]:
            if l['rect'].left > WindowWidth or l['rect'].top > WindowHeight:
                lifes.remove(l)

        for l in lifes:
            windowSurface.blit(l['surface'], l['rect'])

        pygame.display.update()

        #打印敌方大飞机一
        boss1addcounter += 1
        if boss1addcounter == 400:
            boss1addcounter = 0
            bosssize = random.randint(35, 45)
            newboss1 = {'rect': pygame.Rect(random.randint(0,WindowWidth), 0, bosssize, bosssize),
                       'speed': 1,
                       'surface': pygame.transform.scale(boss1, (bosssize, bosssize)),
                       'life':random.randint(4,7),
                       }
            bosses1.append(newboss1)

        for bo in bosses1:
            bo['rect'].move_ip(0, bo['speed'])

        for bo in bosses1:
            if bo['rect'].top>WindowHeight:
                bosses1.remove(bo)

        for bo in bosses1:
            windowSurface.blit(bo['surface'], bo['rect'])

        pygame.display.update()

        #打印敌方大飞机一子弹
        for bo in bosses1:
            ifboss1bullet = random.randint(0, 2000)
            if ifboss1bullet<=10:
                boss1rect=bo['rect']
                boss1newbullet={'rect':pygame.Rect(boss1rect.centerx,boss1rect.centery,30,30),
                              'surface':pygame.transform.scale(boss1bullet,(30,30)),
                              'direction':random.randint(-1,1),
                              'speed':2,
                              }
                bosses1totalbullet.append(boss1newbullet)

        for bp in bosses1totalbullet:
            bp['rect'].move_ip(bp['direction'],bp['speed'])

        for bp in bosses1totalbullet:
            if bp['rect'].top>WindowHeight or bp['rect'].left>WindowWidth or bp['rect'].right<0:
                bosses1totalbullet.remove(bp)

        for bp in bosses1totalbullet:
             windowSurface.blit(bp['surface'],bp['rect'])

        pygame.display.update()

        #显示分数
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topscore), font, windowSurface, 10, 50)

        #检测我方飞机与金条的碰撞
        for g in golds:
            if playerrect.colliderect(g['rect']):
                golds.remove(g)
                score+=5

        #检测我方飞机和生命包的碰撞
        for l in lifes:
            if playerrect.colliderect(l['rect']):
                lifes.remove(l)
                if life<7:
                    life+=1

        #检测我方飞机和敌方小飞机的碰撞
        if playerhashitbaddies(playerrect,baddies):
            life-=1
            pygame.time.wait(50)
            if life<=0:
                if score > topscore:
                    topscore = score
                break

        #检测我方子弹与敌方小飞机的碰撞
        for bu in bullets:
            for b in baddies:
                if bu['rect'].colliderect(b['rect']):
                    baddies.remove(b)
                    bullets.remove(bu)
                    score+=1

        #检测我方飞机和敌方小飞机子弹的碰撞
        for nb in enemybullets:
            if playerrect.colliderect(nb['rect']):
                life-=1
                enemybullets.remove(nb)

        #检测我方飞机和敌方大飞机一的碰撞
        for bo in bosses1:
            if playerrect.colliderect(bo['rect']):
                life-=1

        #检测我方飞机和敌方大飞机一子弹的碰撞
        for bu in bosses1totalbullet:
            if bu['rect'].colliderect(playerrect):
                life-=1
                bosses1totalbullet.remove(bu)

        #检测我方子弹和敌方大飞机一的碰撞
        for b in bullets:
            for bo in bosses1:
                if b['rect'].colliderect(bo['rect']):
                    bo['life']-=1
                    bullets.remove(b)

        #检测大飞机一的生命
        for bo in bosses1:
            if bo['life']<=0:
                bosses1.remove(bo)
                score+=3

        #检测我方飞机的生命
        if life<=0:
            if score > topscore:
                topscore = score
            break

        #执行帧速度和更新
        fpsclock.tick(FPS)
        pygame.display.update()

    #输出结束界面
    drawText('GAME OVER', font, windowSurface, (WindowWidth / 3-15), (WindowHeight / 3))
    drawText('Press a key to play again.', font, windowSurface, (WindowWidth / 3-20) - 80, (WindowHeight / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()