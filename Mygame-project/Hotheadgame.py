# import os
import random
import pygame, sys
pygame.init()
pygame.display.set_caption("Hot Head Gaming!")
GameWidth = 1100
GameHeight = 700
screen = pygame.display.set_mode((GameWidth, GameHeight))

hothead = pygame.image.load("hothead.png")


def gameloop():
    gameplay = True
    while gameplay:
        BLACK    = (0,     0,   0)
        NAVYBLUE = ( 60,  60, 100)
        WHITE    = (255, 255, 255)
        RED      = (255,   0,   0)
        GREEN    = (  0, 255,   0)
        BLUE     = (  0,   0, 255)
        BROWN    = (204, 102,   0)
        BG       = (179, 218, 255)

        size = 20
        # LEVEL 1
        startpointX = 170
        startpointY = 332
        savepointX = 550
        savepointY = 330
        # LEVEL 2
        startpointX2 = 410
        startpointY2 = 230
        savepointX2 = 670
        savepointY2 = 230
        # LEVEL 3
        startpointX3 = 330
        startpointY3 = 212
        savepointX3 = 330
        savepointY3 = 452

        directioncircle1 = "right"
        directioncircle2 = "left"
        directiondown = 'down'
        directionup = 'up'
        directionleft = 'left'
        directionright = 'right'
        deadcount = 0
        levelcount = 0
        font = pygame.font.SysFont(None,50)

        def deadtext(deadcount):
            text = font.render("DEATHS : " + str(deadcount), True, RED)
            screen.blit(text, [800, 30])
        def leveltext(levelcount):
            text = font.render("LEVELS: " + str(levelcount+1)+ "/?", True, BLACK)
            screen.blit(text, text.get_rect(centerx=(GameWidth / 2),y= 30))
        class Player(object):
            def __init__(self):
                self.rect = pygame.Rect(startpointX, startpointY, 16, 16)

            def move(self, dx, dy):
                if dx != 0:
                    self.move_single_axis(dx, 0)
                if dy != 0:
                    self.move_single_axis(0, dy)

            def move_single_axis(self, dx, dy):
                # Move the rect
                self.rect.x += dx
                self.rect.y += dy

                for wall in walls:
                    if self.rect.colliderect(wall.rect):
                        if dx > 0:  # Moving right; Hit the left side of the wall
                            self.rect.right = wall.rect.left
                        if dx < 0:  # Moving left; Hit the right side of the wall
                            self.rect.left = wall.rect.right
                        if dy > 0:  # Moving down; Hit the top side of the wall
                            self.rect.bottom = wall.rect.top
                        if dy < 0:  # Moving up; Hit the bottom side of the wall
                            self.rect.top = wall.rect.bottom

        class Enemy(object):#enemy pattern
            def Enemylisttwo3(pos):
                self = pygame.Rect(pos[0], pos[1],16,16)
                enemylistwo3store.append(self)
            def Enemylisttwo4(pos):
                self = pygame.Rect(pos[0],pos[1],16,16)
                enemylisttwo4store.append(self)
            def Enemylistthree(pos):
                self = pygame.Rect(pos[0],pos[1],16,16)
                enemylistthreestore.append(self)
            def Enemylistthree2(pos):
                self = pygame.Rect(pos[0],pos[1],16,16)
                enemylistthree2store.append(self)

        class Wall(object):
            def __init__(self, pos):
                self.rect = pygame.Rect(pos[0], pos[1], size, size)
        class enemywall(object):
            def __init__(self, pos):
                self.rect = pygame.Rect(pos[0], pos[1], size, size)
        class Save(object):
            def __init__(self, pos):
                self.rect = pygame.Rect(pos[0], pos[1], size, size)
        class Goal(object):
            def __init__(self, pos):
                self.rect = pygame.Rect(pos[0], pos[1], size, size)
        class clearscreen:
            screen.fill(WHITE)
            pygame.display.update()
        # class

        clock = pygame.time.Clock()
        player = Player()

        # Level 1 enemy
        enemydown = [pygame.Rect(330, 290, 16, 16),pygame.Rect(402, 290, 16, 16)]
        enemyup = [pygame.Rect(366, 370, 16, 16),pygame.Rect(438, 370, 16, 16)]
        enemyright = [pygame.Rect(630,292, 16, 16),pygame.Rect(630,332, 16, 16),pygame.Rect(630,372, 16, 16)]
        enemyleft = [pygame.Rect(770,312, 16, 16),pygame.Rect(770,352, 16, 16)]

        # Level 2 enemy
        enemylisttwo = [pygame.Rect(282, 212, 16, 16), pygame.Rect(538, 212, 16, 16)]
        enemylisttwo2 = pygame.Rect(568, 392, 16, 16)
        enemylisttwo3 = [(772,272),(772,312),(772,352),(772,392),(772,432)]
        enemylistwo3store = []
        enemylisttwo4 = [(852,292),(852,332),(852,372),(852,412)]
        enemylisttwo4store = []
        enemylisttwo5 = [pygame.Rect(390, 454, 25, 25)]
        enemylisttwo6 = [pygame.Rect(730, 480, 25, 25)]

        # Level 3 enemy
        enemylistthree = [(432,192),(472,192),(512,192),(552,192),(592,192),(632,192)]
        enemylistthreestore = []
        enemylistthree2 = [(392,232),(392,272),(392,312),(392,352),(392,392),(392,432)]
        enemylistthree2store = []

        #--- Enemy level 2 store --------------------------
        for i in enemylisttwo3:
            Enemy.Enemylisttwo3(i)
        for i in enemylisttwo4:
            Enemy.Enemylisttwo4(i)
        # --- Enemy level 3 store--------------------------
        for i in enemylistthree:
            Enemy.Enemylistthree(i)
        for i in enemylistthree2:
            Enemy.Enemylistthree2(i)

        levels = [[
            # LEVEL 111111111111111111111111
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #1
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #2
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #3
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #4
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #5
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #6
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #7
            "WWWW              SSSSS          GGGGGWW", #8
            "WWWW              SSSSS          GGGGGWW", #9
            "W                 SSSSS          GGGGGWW", #10
            "WWWW              SSSSS          GGGGGWW", #11
            "WWWW              SSSSS          GGGGGWW", #12
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #13
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #14
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #15
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #16
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #17
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #18
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #19
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #20
            ],
            [
            #  LEVEL 222222222222222222222
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", #1
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", #2
            "EEEEEEEEEWWWWWWWEEEEEEEEWWWWWEEEEEEEEEEE", #3
            "EEEEEE         WEEE     SSSSS       EEEE", #4
            "EEEEEE         WEEE     SSSSS       EEEE", #5
            "EEEEEE         WEEE     SSSSS       EEEE", #6
            "EEEEEE  EWWWWWWWEEE   EEWWWWWEE     EEEE", #7
            "EEEEEE  EEEEEEEEEEE   EEEEEEEEE     EEEE", #8
            "EEEEEE  EEEEEEEEEEE   EEEEEEEEE     EEEE", #9
            "EEEEEE  EEEEEEEEEEE   EEEEEEEEE     EEEE", #10
            "EEEEEE  EEEEEEEEEEE   EEEEEEEEE     EEEE", #11
            "EEEEEE                EEEEEEEEE     EEEE", #12
            "EEEEEE                EEEEEEEEE     EEEE", #13
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     EEEE", #14
            "EEEEEWWWWEEEEEEEEEEEEEEEEEEEEEE     EEEE", #15
            "EEEEEWGGG                           EEEE", #16
            "EEEEEWGGG                           EEEE", #17
            "EEEEEWGGG                           EEEE", #18
            "EEEEEWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", #19
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", #20
            ],
            [
            #   LEVEL 333333333333333333
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #1
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #2
            "WWWWWWWWWWWWEEEEEEEEEEEEEEEWWWWWWWWWWWWW", #3
            "WWWWWWWWW                 EWWWWWWWWWWWWW", #4
            "WWWWWWWWWWWWEEEEEEEEEEEEE EWWWWWWWWWWWWW", #5
            "WWWWWWWWWWWWE           E EWWWWWWWWWWWWW", #6
            "WWWWWWWWWWWWE EEEEEEEEE E EWWWWWWWWWWWWW", #7
            "WWWWWWWWWWWWE E       E E EWWWWWWWWWWWWW", #8
            "WWWWWWWWWWWWE E EEEEE E E EWWWWWWWWWWWWW", #9
            "WWWWWWWWWWWWE E E  GE E E EWWWWWWWWWWWWW", #10
            "WWWWWWWWWWWWE E E EEE E E EWWWWWWWWWWWWW", #11
            "WWWWWWWWWWWWE E E     E E EWWWWWWWWWWWWW", #12
            "WWWWWWWWWWWWE E EEEEEEE E EWWWWWWWWWWWWW", #13
            "WWWWWWWWWWWWE E         E EWWWWWWWWWWWWW", #14
            "WWWWWWWWWWWWE EEEEEEEEEEE EWWWWWWWWWWWWW", #15
            "WWWWWWWWWS                EWWWWWWWWWWWWW", #16
            "WWWWWWWWWWWWEEEEEEEEEEEEEEEWWWWWWWWWWWWW", #17
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #18
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #19
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #20
            ]]


        def load_level(level):
            walls = []
            enemywalls = []
            savepoint = []
            goalpoint = []
            x = y = 150
            for row in levels[level]:
                for col in row:
                    if col == "W":
                        walls.append(Wall((x, y)))
                    if col == "E":
                        enemywalls.append(enemywall((x,y)))
                    if col == "S":
                        savepoint.append(Save((x,y)))
                    if col == "G":
                        goalpoint.append(Goal((x,y)))
                    x += 20
                y += 20
                x = 150
            return walls, enemywalls, savepoint, goalpoint
        walls, enemywalls, savepoint, goalpoint = load_level(levelcount)

        def introgame():
            intro = True
            while intro:
                screen.fill(BG)
                text = font.render("Welcome to Hot Head Gaming", True, RED)
                screen.blit(text, text.get_rect(center=(GameWidth / 2, 200)))
                screen.blit(hothead,[GameWidth / 2 - 53, 230])
                text2 = font.render("Press arrow keys to play", True, NAVYBLUE)
                screen.blit(text2, text2.get_rect(center=(GameWidth / 2, 500)))
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()
                        if e.key == pygame.K_UP or e.key == pygame.K_DOWN or e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                            intro = False
                pygame.display.update()
                clock.tick(15)
        introgame()
        def theend():
            ending = True
            while ending:
                clearscreen()
                screen.fill(BG)
                text = font.render("You have finished this game", True, RED)
                screen.blit(text, text.get_rect(center=(GameWidth / 2 , 250)))
                text2 = font.render("Totals Deaths:  " + str(deadcount), True, NAVYBLUE)
                screen.blit(text2, text2.get_rect(center=(GameWidth / 2, 350)))
                text3 = font.render("Press P to play again, Q to quit", True, BROWN)
                screen.blit(text3, text3.get_rect(center=(GameWidth / 2, 450)))

                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE or e.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        if e.key == pygame.K_p:
                            gameloop()
                pygame.display.update()

        running = True
        while running:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                        clearscreen()
                        if levelcount == 0:
                            levelcount = 1
                            startpointX = startpointX2
                            startpointY = startpointY2
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            savepointX = savepointX2
                            savepointY = savepointY2
                        elif levelcount == 1:
                            levelcount = 2
                            startpointX = startpointX3
                            startpointY = startpointY3
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            savepointX = savepointX3
                            savepointY = savepointY3
                        elif levelcount == 2:
                            theend()
                        walls, enemywalls, savepoint, goalpoint = load_level(levelcount)

                key = pygame.key.get_pressed() #player move
                if key[pygame.K_LEFT]:
                    player.move(-2, 0)
                if key[pygame.K_RIGHT]:
                    player.move(2, 0)
                if key[pygame.K_UP]:
                    player.move(0, -2)
                if key[pygame.K_DOWN]:
                    player.move(0, 2)

                # Draw the scene
                screen.fill(WHITE)
                for wall in walls: #draw wall
                    pygame.draw.rect(screen, BLACK, wall.rect)

                for enemy in enemywalls:
                    pygame.draw.rect(screen, BLUE, enemy.rect)
                    if player.rect.colliderect(enemy.rect):
                        player.rect.x = startpointX
                        player.rect.y = startpointY
                        deadcount += 1

                #   //////////////////  LEVEL 1  //////////////////////////////////////////////////////////
                if levelcount == 0:
                    for enemy in enemydown:
                        pygame.draw.rect(screen, BLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directiondown == 'down':
                            enemy.move_ip(0, 2)
                            if enemy.y >= 372:
                                enemy.y -= 4
                                directiondown = 'up'
                        elif directiondown == 'up':
                            enemy.move_ip(0, -2)
                            if enemy.y <= 292:
                                enemy.y += 4
                                directiondown = 'down'
                    for enemy in enemyup:
                        pygame.draw.rect(screen, BLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directionup == 'up':
                            enemy.move_ip(0, -2)
                            if enemy.y <= 292:
                                enemy.y += 4
                                directionup = 'down'
                        elif directionup == 'down':
                            enemy.move_ip(0, 2)
                            if enemy.y >= 372:
                                enemy.y -= 4
                                directionup = 'up'
                    for enemy in enemyright:

                        pygame.draw.rect(screen, BLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directionright == 'right':
                            enemy.move_ip(2, 0)
                            if enemy.x >= 772:
                                enemy.x -= 4
                                directionright = 'left'
                        elif directionright == 'left':
                            enemy.move_ip(-2, 0)
                            if enemy.x <= 632:
                                enemy.x += 4
                                directionright = 'right'
                    for enemy in enemyleft:
                        pygame.draw.rect(screen, BLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directionleft == 'left':
                            enemy.move_ip(-2, 0)
                            if enemy.x <= 632:
                                enemy.x += 4
                                directionleft = 'right'
                        elif directionleft == 'right':
                            enemy.move_ip(2, 0)
                            if enemy.x >= 772:
                                enemy.x -= 4
                                directionleft = 'left'
                #   //////////////////  LEVEL 2  //////////////////////////////////////////////////////////
                if levelcount == 1:
                    for enemy in enemylisttwo:
                        pygame.draw.rect(screen, BLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directiondown == 'down':
                            enemy.move_ip(0, 2)
                            if enemy.y >= 392:
                                enemy.y -= 4
                                directiondown = 'up'
                        elif directiondown == 'up':
                            enemy.move_ip(0, -2)
                            if enemy.y <= 210:
                                enemy.y += 4
                                directiondown = 'down'
                    pygame.draw.rect(screen, BLUE, enemylisttwo2)
                    if player.rect.colliderect(enemylisttwo2):
                        player.rect.x = startpointX
                        player.rect.y = startpointY
                        deadcount += 1
                    if directionup == 'up':
                        enemylisttwo2.move_ip(0, -2)
                        if enemylisttwo2.y <= 210:
                            enemylisttwo2.y += 4
                            directionup = 'down'
                    elif directionup == 'down':
                        enemylisttwo2.move_ip(0, 2)
                        if enemylisttwo2.y >= 392:
                            enemylisttwo2.y -= 4
                            directionup = 'up'
                    for enemy in enemylistwo3store:
                        pygame.draw.rect(screen, BLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directionright == 'right':
                            enemy.move_ip(2, 0)
                            if enemy.x >= 852:
                                enemy.x -= 4
                                directionright = 'left'
                        elif directionright == 'left':
                            enemy.move_ip(-2, 0)
                            if enemy.x <= 772:
                                enemy.x += 4
                                directionright = 'right'
                    for enemy in enemylisttwo4store:
                        pygame.draw.rect(screen, BLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directionleft == 'left':
                            enemy.move_ip(-2, 0)
                            if enemy.x <= 772:
                                enemy.x += 4
                                directionleft = 'right'
                        elif directionleft == 'right':
                            enemy.move_ip(2, 0)
                            if enemy.x >= 852:
                                enemy.x -= 4
                                directionleft = 'left'

                    for enemy in enemylisttwo5:
                        pygame.draw.rect(screen, NAVYBLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directioncircle1 == 'right':
                            enemy.move_ip(4, 0)
                            if enemy.x >= 730:
                                directioncircle1 = 'down'
                        elif directioncircle1 == 'down':
                            enemy.move_ip(0, 4)
                            if enemy.y >= 480:
                                directioncircle1 = 'left'
                        elif directioncircle1 == 'left':
                            enemy.move_ip(-4, 0)
                            if enemy.x <= 390:
                                directioncircle1 = 'up'
                        elif directioncircle1 == 'up':
                            enemy.move_ip(0, -4)
                            if enemy.y <= 454:
                                directioncircle1 = 'right'

                    for enemy in enemylisttwo6:
                        pygame.draw.rect(screen, NAVYBLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directioncircle2 == 'left':
                            enemy.move_ip(-4, 0)
                            if enemy.x <= 390:
                                directioncircle2 = 'up'
                        elif directioncircle2 == 'up':
                            enemy.move_ip(0, -4)
                            if enemy.y <= 454:
                                directioncircle2 = 'right'
                        elif directioncircle2== 'right':
                            enemy.move_ip(4, 0)
                            if enemy.x >= 730:
                                directioncircle2 = 'down'
                        elif directioncircle2 == 'down':
                            enemy.move_ip(0, 4)
                            if enemy.y >= 480:
                                directioncircle2 = 'left'
                #  ///////////////////  LEVEL 3  //////////////////////////////////////////////////////////
                if levelcount == 2:
                    for enemy in enemylistthreestore:
                        pygame.draw.rect(screen, NAVYBLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directiondown == 'down':
                            enemy.move_ip(0, 4)
                            if enemy.y >= 476:
                                enemy.y -= 8
                                directiondown = 'up'
                        elif directiondown == 'up':
                            enemy.move_ip(0, -4)
                            if enemy.y <= 188:
                                enemy.y += 8
                                directiondown = 'down'
                    for enemy in enemylistthree2store:
                        pygame.draw.rect(screen, NAVYBLUE, enemy)
                        if player.rect.colliderect(enemy):
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            deadcount += 1
                        if directionright == 'right':
                            enemy.move_ip(4, 0)
                            if enemy.x >= 676:
                                enemy.x -= 8
                                directionright = 'left'
                        elif directionright == 'left':
                            enemy.move_ip(-4, 0)
                            if enemy.x <= 388:
                                enemy.x += 8
                                directionright = 'right'

                for save in savepoint:
                    pygame.draw.rect(screen, GREEN, save.rect)
                    if player.rect.colliderect((save.rect)):  # save point
                        startpointX = savepointX  # save point X
                        startpointY = savepointY  # save point Y

                for goal in goalpoint:
                    pygame.draw.rect(screen,RED, goal.rect)
                    if player.rect.colliderect(goal.rect):  # goals , next level
                        clearscreen()
                        if levelcount == 0:
                            levelcount = 1
                            startpointX = startpointX2
                            startpointY = startpointY2
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            savepointX = savepointX2
                            savepointY = savepointY2
                        elif levelcount == 1:
                            levelcount = 2
                            startpointX = startpointX3
                            startpointY = startpointY3
                            player.rect.x = startpointX
                            player.rect.y = startpointY
                            savepointX = savepointX3
                            savepointY = savepointY3
                        elif levelcount == 2:
                            theend()
                        walls, enemywalls, savepoint, goalpoint = load_level(levelcount)

                pygame.draw.rect(screen, RED, player.rect)  # draw player

                clock.tick(60)
                deadtext(deadcount)
                leveltext(levelcount)
                pygame.display.update()
gameloop()