import pygame , sys
import time
import random
window = pygame.display.set_mode((750,780))

pygame.display.set_caption("CubeWar")


screenplay = pygame.Surface((750,750))

info_string = pygame.Surface((750,30))

speed = 10
speed3 = 10


blue= (0,0,200)

#text = info_font.render('Bomber', True, (210,120,200),(10,5))




pygame.font.init()

"""таймер кадрів"""
#clock  = pygame.time.Clock()
#dt = 0

class Menu:
      def __init__(self,punkts = [600,600, u"namePunkt",(250,250,30),(250,30,250)]):
         self.punkts = punkts
      def render(self,poverhnost,font,num_punkt):
          for i in self.punkts:
              if num_punkt == i[5]:
                  poverhnost.blit(font.render(i[2],1,i[4]),(i[0],i[1]-30))
              else:
                  poverhnost.blit(font.render(i[2],1,i[3]),(i[0],i[1]-30))


      def menu(self):


          done =True
          font_menu = pygame.font.SysFont("comicsansms",70)
          punkt = 0
          while done:
              info_string.fill((10,100,200))
              screenplay.fill((10,100,200))



              mouse = pygame.mouse.get_pos()
              for i in self.punkts:
                  if mouse[0]>i[0] and mouse[0]<i[0]+200 and mouse[1]> i[1] and mouse[1]<i[1]+100:
                        punkt = i[5]

              self.render(screenplay,font_menu,punkt)

              for e in pygame.event.get():
                  if e.type == pygame.QUIT:
                      sys.exit()
                  if e.type == pygame.KEYDOWN:
                      if e.key == pygame.K_ESCAPE:
                          sys.exit()
                      if e.key == pygame.K_UP:
                          if punkt > 0 :
                              punkt -=1
                      if e.key == pygame.K_DOWN:
                          if punkt < len(self.punkts)-1:
                              punkt+=1

                  if e.type ==pygame.MOUSEBUTTONDOWN  and e.button == 1:
                      if punkt == 0:
                           done = False
                      elif punkt == 1:
                          sys.exit()


              window.blit(info_string,(0,0))
              window.blit(screenplay,(0,30))
              pygame.display.flip()


"""создання меню"""
punkts = [(280,280,u"Game",(250,250,30),(250,30,250),0),(292,350,u"Quit",(250,250,30),(250,30,250),1)]
game =Menu(punkts)
game.menu()

class  topclass:
    def __init__(self,xpos,ypos,filename):
        self.x =xpos
        self.y  =ypos
        self.bitmap= pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0 ))



    def render(self) :
        info_string.blit(self.bitmap,(self.x , self.y))




#class Animation():
#    def __init__(self,x,y,sprites= None,time = 100):
#        self.x = x
#        self.y = y
#        self.sprites = sprites
#        self.work_time = 0
#        self.skip_frame = 0
#        self.frame = 0
#    def update(self,dt) :
#        self.work_time += dt
#        self.skip_frame = self.work_time / self.time
#        if self.skip_frame > 0 :
#            self.work_time = self.work_time % self.work_time
    #        self.frame += self.skip_frame
#            if self.frame >= len(self.sprites) :
#                self.frame = 0
#    def get_sprites(self):
#        return self.sprites[self.frame]
#
#sprites = pygame.image.load("D:/pi/blueturtle11.png")



#anim =[]
#anim.append(sprites.subsurface(20,20,40,40))
#anim.append(sprites.subsurface(100,100,100,100))
#anim.append(sprites.subsurface(80,20,40,40))
#anim.append(sprites.subsurface(40,20,40,40))


#time = 180
#target = Animation(anim , time)

walkRight = [pygame.image.load("images/blueturtle11.png"),pygame.image.load("images/blueturtle12.png"),pygame.image.load("images/blueturtle13.png")]
walkLeft = [pygame.image.load("images/redturtle11.png"),pygame.image.load("images/redturtle12.png"),pygame.image.load("images/redturtle13.png")]

playerstandblue = pygame.image.load("images/blueturtle11.png")
playerstandred = pygame.image.load("images/redturtle11.png")

left = False
right =False
animCount = 0

clock = pygame.time.Clock()


"""серця"""
serce1 = topclass(325,5, "images/серцеред.jpg" )


class  justclass:
    def __init__(self,xpos,ypos,filename):
        self.x =xpos
        self.y = ypos
        self.bitmap= pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0 ))



    def render(self) :
        screenplay.blit(self.bitmap,(self.x , self.y))



otbitok = False
otbitok2 =False
test_jump =10
test_jump3 = 10

delay1 = 50
delay2 = 100
#герої
hero1  = justclass( 10,600,"images/blueturtle11.jpg")


hero2 = justclass(350,350, "images/мячик1.jpg" )


strela = justclass(hero1.x + 12, hero1.y , "images/yy2.jpg")
strela.push = False

hero3 = justclass(10, 10, "images/redturtle11.jpg")

strela2 = justclass(hero3.x + 12 , hero3.y , "images/kkk.jpg")
pygame.display.update()
strela2.push = False






a1 = [0]
a2 = [0]



jump =  False
jump_player1 = 20
jump3 = False
jump_player2 = 20
run_hero2 = True

sercered1 = True
sercered2 = True
sercered3 = True

serceblue1 = True
serceblue2 = True
serceblue3 = True


speed2 = 5

hero2_right= True
hero2_down= True
done = True

strela_speed = 5
strela2_speed = 5

"""рахунок"""
raxunok1 = 0
raxunok2 = 0


inf_font = pygame.font.SysFont("images/comicsansms",16)
inf2_font = pygame.font.SysFont("images/comicsansms",16)
inf3_font = pygame.font.SysFont("images/comicsansms",16)
#text = inf_font.render("Швидкість :  "+str(strela_speed),1,(66, 75, 245),(0,255,0))



#pygame.key.set_repeat(1,1)
while done:


    """серця"""
    if a1.count(0) < 4 :
      serce1 = topclass(340,5, "images/серцеред.jpg" )
    if a1.count(0) < 3 :
      serce2 = topclass(365,5, "images/серцеред.jpg" )
    if a1.count(0) < 2 :
      serce3 = topclass(390,5, "images/серцеред.jpg" )



    if a2.count(0) < 4 :
      serce4 = topclass(10,5, "images/серцеблу.jpg" )
    if a2.count(0) < 3 :
      serce5 = topclass(35,5, "images/серцеблу.jpg" )
    if a2.count(0) < 2 :
      serce6 = topclass(60,5, "images/серцеблу.jpg" )


    text = inf_font.render("Speed1 :"+str(strela_speed),1,(0,0,255),(0,255,0))
    text2 = inf2_font.render("Speed2 :"+str(strela2_speed),1,(255,0,0),(0,255,0))
    text3 = inf2_font.render("Score "+str(raxunok1)+":"+str(raxunok2),1,(245, 66, 218),(0,255,0))

    #if (hero2.x < 0 or hero2.x >500 ) or (hero2.y < 0 or hero2.y >500):
    #     hero2.x = 15
    #     hero2_right = random.randint(0,1)
    #     hero2.y = 200
    #     hero2_down = random.randint(0,1)
    """перерва"""
    #права сторона
    #настроювання відбивань 1.1
    def Intersect1(x1, x2,y1,y2):
        if (x1 == x2 - 60 ) and ( y1 - 60 <= y2) and ( y2 <= y1 +60) and (y2 >= y1 +30):

              return 1
        else:
            return 0

    if Intersect1(hero1.x , hero2.x, hero1.y , hero2.y):
              hero2_right = True
              hero2_down =True


    #настроювання відбивань 10.2
    def Intersect11(x1, x2,y1,y2):
        if (x1 == x2 - 60 ) and ( y1 - 60 <= y2) and ( y2 <= y1 +30) :

              return 1
        else:
            return 0

    if Intersect11(hero1.x , hero2.x, hero1.y , hero2.y):
              hero2_right = True
              hero2_down =False




    #ліва сторона
    #настроювання відбивань 20.1
    def Intersect12(x1, x2,y1,y2):
        if (x1 == x2 + 60) and ( y2>= y1 -60) and (y2 <= y1+60) and (y2 >= y1+30) :
            return 1
        else:
            return 0

    if Intersect12(hero1.x , hero2.x, hero1.y , hero2.y):
              hero2_right = False
              hero2_down =True

    #настроювання відбивань 20.2
    def Intersect00(x1, x2,y1,y2):
        if (x1 == x2 + 60) and ( y2>= y1 -60) and (y2 <= y1+30) :
           return 1
        else:
            return 0

    if Intersect00(hero1.x , hero2.x, hero1.y , hero2.y):
              hero2_right = False
              hero2_down =False




    #верхня сторона
    #настроювання відбивань 30.1
    def Intersect13(x1, x2,y1,y2):
        if (y1== y2 +60) and (x1 - 60 <= x2)  and ( x2<= x1 +60) and (x2 >= x1 +30) :
            return 1
        else :
            return 0

    if Intersect13(hero1.x , hero2.x, hero1.y , hero2.y):
              hero2_right = True
              hero2_down =False

    #настроювання відбивань 30.2
    def Intersect14(x1, x2,y1,y2):
         if (y1== y2 +60) and (x1 - 60 <= x2)  and ( x2<= x1 +30) :
             return 1
         else :
             return 0

    if Intersect14(hero1.x , hero2.x, hero1.y , hero2.y):
               hero2_right = False
               hero2_down =False




    #нижня сторона
    #настроювання відбивань 40.1
    def Intersect15(x1, x2,y1,y2):
         if  (y1 + 60 == y2) and (x1 -60 <=x2) and (x2<=x1+60) and x2>= x1+ 30:
             return 1
         else :
             return 0

    if Intersect15(hero1.x , hero2.x, hero1.y , hero2.y):
               hero2_right =True
               hero2_down =True

    #настроювання відбивань 40.2
    def Intersect16(x1, x2,y1,y2):
         if  (y1 + 60 == y2) and (x1 -60 <=x2) and (x2<=x1+30):
             return 1
         else :
             return 0

    if Intersect16(hero1.x , hero2.x, hero1.y , hero2.y):
               hero2_right =False
               hero2_down =True




    # робота цілі
    if hero2_right :
        hero2.x += speed2
        if hero2.x >= 690 :
            hero2_right = False


    if  hero2_right == False :
        hero2.x -= speed2
        if hero2.x <= 10 :
             hero2_right = True

    if hero2_down :
        hero2.y += speed2
        if hero2.y >= 690 :
            hero2_down = False

    if  hero2_down == False:
        hero2.y -= speed2
        if hero2.y <= 10 :
             hero2_down =True

    for najatie in pygame.event.get():
        if najatie.type == pygame.QUIT:
            done = False
        if najatie.type == pygame.K_ESCAPE:
            game.menu()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] :
        game.menu()
    # робота гравця
    if keys[pygame.K_LEFT] and hero1.x > 10:
        hero1.x  -=  speed
        left = True
        right =False
        if strela.push == False :
            strela.x = hero1.x + 12
    if keys[pygame.K_RIGHT] and hero1.x < 675 :
        hero1.x += speed
        left = False
        right =True
        if strela.push == False :
            strela.x = hero1.x + 12
    #стрибки гравця
    if not( jump):

        if keys[pygame.K_UP] and  hero1.y > 375:
            hero1.y -= speed
            left = False
            right =False
            if strela.push == False :
                strela.y = hero1.y + 10
        if keys[pygame.K_DOWN] and hero1.y < 675:
            left = False
            right =False
            hero1.y += speed
            if strela.push == False :
                strela.y = hero1.y + 10
        if keys[pygame.K_SPACE] and hero1.y > 375:
            jump = True
            left = False
            right =True


    else :
          left = False
          right =False
          if test_jump >= -10 :
              if test_jump < 0 :
                  hero1.y += (test_jump ** 2) / 2
              else:
                  hero1.y -= (test_jump ** 2) / 2
              test_jump -= 1
              if strela.push == False :
                  strela.y = hero1.y +10
          else:
             jump = False
             test_jump = 10








    #стріла гравця
    if not(strela.push):


        #pygame.key.set_repeat(100,100)
        if keys[pygame.K_BACKSPACE]  and hero1.y >= 375 :
             strela.push = True

    else:

        #pygame.key.set_repeat(0,0)
        if strela.y > 0 and strela.y <710 :
              strela.y -= strela_speed

        else :
            strela.push = False
            strela.y = hero1.y + 10
            strela.x = hero1.x + 12
        def Intersect0(x1, x2,y1,y2):
               # x1 - мячик x2 - стріла
               if (x1 +60 >= x2) and (y1 + 60 >= y2) and (x1 - 35<= x2) and y2>= y1:
                   return 1

               else :
                   return  0


        #pygame.key.set_repeat(0,0)
        if Intersect0(hero2.x,strela.x,hero2.y,strela.y) :
                  strela.y = hero1.y + 10
                  strela.x = hero1.x + 12
                  if strela_speed >= 100 :


                       strela_speed = 5
                       strela2_speed = 5
                       raxunok1 += 1
                       time.sleep(1)
                  else :

                        strela_speed += 1


                  strela.y = hero1.y + 10
                  strela.x = hero1.x + 12
                  hero2.x = 710


                  hero2_right = random.randint(0,1)

                  hero2.y = 350
                  hero2_down = random.randint(0,1)
                  strela.push=False



        """Попадання в 2 гравця"""
        def Intersect0(x1, x2,y1,y2):
               # x1 - гравець2 x2 - стріла
               if (x1 +60 >= x2) and (y1 + 60 >= y2) and (x1 - 35<= x2) and y2>= y1-90 and y1 <= y2:
                   return 1

               else :
                   return  0


        #pygame.key.set_repeat(0,0)
        if Intersect0(hero3.x,strela.x,hero3.y,strela.y) :
                  strela.y = hero1.y + 10
                  strela.x = hero1.x + 12
                  if strela_speed >= 100 :


                       strela_speed = 5
                       strela2_speed =5
                       raxunok1 += 1
                       time.sleep(1)
                  else :

                        strela_speed += 5


                  strela.y = hero1.y + 10
                  strela.x = hero1.x + 12

                  strela.push=False
                  a1.append(0)
                  if a1.count(0) == 4:
                      raxunok1 += 1
                      strela_speed = 5
                      strela2_speed =5

                      while a1.count(0) > 1 :
                          a1.remove(0)

                          if a2.count(0) > 1:
                              while a2.count(0 ) > 1:
                                  a2.remove(0)
                          time.sleep(1)




    """робота 2 гравця"""
    if keys[pygame.K_a] and hero3.x > 10:
       hero3.x  -=  speed3
       if strela2.push == False :
           strela2.x = hero3.x + 12
    if keys[pygame.K_d] and hero3.x < 675 :
       hero3.x += speed3
       if strela2.push == False :
           strela2.x = hero3.x + 12
    #стрибки гравця
    if not( jump3):
        if keys[pygame.K_w] and  hero3.y > 10:
            hero3.y -= speed3
            if strela2.push == False :
                strela2.y = hero3.y + 10
        if keys[pygame.K_s] and hero3.y < 305:
            hero3.y += speed3
            if strela2.push == False :
                strela2.y = hero3.y + 10
        if keys[pygame.K_e] and hero3.y <305:
            jump3 = True

    else :
          if test_jump3 >= -10 :
              if test_jump3 < 0 :
                  hero3.y -= (test_jump3 ** 2) / 2
              else:
                  hero3.y += (test_jump3 ** 2) / 2
              test_jump3 -= 1
              if strela2.push == False :
                  strela2.y = hero3.y +10
          else:
             jump3 = False
             test_jump3 = 10

    """стріла гравця2"""
    if not(strela2.push):


        #pygame.key.set_repeat(100,100)
        if keys[pygame.K_q]  and hero3.y <=305 :
             strela2.push = True

    else:

        #pygame.key.set_repeat(0,0)
        if strela2.y < 710 and strela2.y > 0:
              strela2.y += strela2_speed

        else :
            strela2.push = False
            strela2.y = hero3.y + 10
            strela2.x = hero3.x + 12
        def Intersect0(x1, x2,y1,y2):
               # x1 - мячик x2 - стріла
               if (x1 +60 >= x2) and (y1 + 60  >= y2) and (x1 - 35<= x2) and (y1 <= y2):
                   return 1

               else :
                   return  0

        #pygame.key.set_repeat(0,0)
        if Intersect0(hero2.x,strela2.x,hero2.y,strela2.y) :
                  strela2.y = hero3.y + 10
                  strela2.x = hero3.x + 12
                  if strela2_speed >= 100 :


                       strela_speed = 5
                       strela2_speed = 5
                       raxunok2 += 1
                       time.sleep(1)
                  else :

                        strela2_speed += 1


                  strela2.y = hero3.y + 10
                  strela2.x = hero3.x + 12
                  hero2.x = 40

                  hero2_right = random.randint(0,1)

                  hero2.y = 350
                  hero2_down = random.randint(0,1)
                  strela2.push=False



        """Попадання в 1 гравця"""

        def Intersect0(x1, x2,y1,y2):
                # x1 - гравець1 x2 - стріла
                if (x1 +60 >= x2) and (y1 + 60  >= y2) and (x1 - 35<= x2) and (y1 -40 <= y2):
                    return 1

                else :
                    return  0
        #pygame.key.set_repeat(0,0)
        if Intersect0(hero1.x,strela2.x,hero1.y,strela2.y) :
                   strela2.y = hero3.y + 10
                   strela2.x = hero3.x + 12
                   if strela2_speed >= 100 :


                        strela2_speed = 5
                        strela_speed = 5
                        raxunok2 += 1
                        time.sleep(1)
                   else :

                         strela2_speed += 5


                   strela2.y = hero3.y + 10
                   strela2.x = hero3.x + 12





                   #hero1.x = random.randint(0,1)
                   strela2.push=False
                   a2.append(0)
                   if a2.count(0) == 4:
                       raxunok2 += 1
                       strela_speed = 5
                       strela2_speed =5
                       while a2.count(0) >1 :
                           a2.remove(0)
                           if a1.count(0) >1 :
                               while a1.count(0 ) > 1:
                                   a1.remove(0)
                           time.sleep(1)
    """настроювання відбивань для 3 гравця"""
    #настроювання відбивань 10.1
    def Intersect101(x1, x2,y1,y2):
        if (x1 == x2 - 60 ) and ( y1 - 60 <= y2) and ( y2 <= y1 +60) and (y2 >= y1 +30):

              return 1
        else:
            return 0

    if Intersect101(hero3.x , hero2.x, hero3.y , hero2.y):
              hero2_right = True
              hero2_down =True


    #настроювання відбивань 10.2
    def Intersect102(x1, x2,y1,y2):
        if (x1 == x2 - 60 ) and ( y1 - 60 <= y2) and ( y2 <= y1 +30) :

              return 1
        else:
            return 0

    if Intersect102(hero3.x , hero2.x, hero3.y , hero2.y):
              hero2_right = True
              hero2_down =False




    #ліва сторона
    #настроювання відбивань 20.1
    def Intersect201(x1, x2,y1,y2):
        if (x1 == x2 + 60) and ( y2>= y1 -60) and (y2 <= y1+60) and (y2 >= y1+30) :
            return 1
        else:
            return 0

    if Intersect201(hero3.x , hero2.x, hero3.y , hero2.y):
              hero2_right = False
              hero2_down =True

    #настроювання відбивань 20.2
    def Intersect202(x1, x2,y1,y2):
        if (x1 == x2 + 60) and ( y2>= y1 -60) and (y2 <= y1+30) :
            return 1
        else:
            return 0

    if Intersect202(hero3.x , hero2.x, hero3.y , hero2.y):
              hero2_right = False
              hero2_down =False




   #верхня сторона
   #настроювання відбивань 30.1
    def Intersect301(x1, x2,y1,y2):
        if (y1== y2 +60) and (x1 - 60 <= x2)  and ( x2<= x1 +60) and (x2 >= x1 +30) :
            return 1
        else :
            return 0

    if Intersect301(hero3.x , hero2.x, hero3.y , hero2.y):
              hero2_right = True
              hero2_down =False

    #настроювання відбивань 30.2
    def Intersect302(x1, x2,y1,y2):
         if (y1== y2 +60) and (x1 - 60 <= x2)  and ( x2<= x1 +30) :
             return 1
         else :
             return 0

    if Intersect302(hero3.x , hero2.x, hero3.y , hero2.y):
               hero2_right = False
               hero2_down =False




    #нижня сторона
    #настроювання відбивань 40.1
    def Intersect401(x1, x2,y1,y2):
         if  (y1 + 60 == y2) and (x1 -60 <=x2) and (x2<=x1+60) and x2>= x1+ 30:
             return 1
         else :
             return 0

    if Intersect401(hero3.x , hero2.x, hero3.y , hero2.y):
               hero2_right =True
               hero2_down =True

    #настроювання відбивань 40.2
    def Intersect402(x1, x2,y1,y2):
         if  (y1 + 60 == y2) and (x1 -60 <=x2) and (x2<=x1+30):
             return 1
         else :
             return 0

    if Intersect402(hero3.x , hero2.x, hero3.y , hero2.y):
               hero2_right =False
               hero2_down =True

    """ попадання стріли в стрілу"""
    # стріла 1 стріла 2
    def Intersect402(x1, x2,y1,y2):
         if  (x2+35>=x1) and (x1 +35 >=x2) and (y2 + 40 >= y1)  :
             return 1
         else :
             return 0

    if Intersect402(strela.x , strela2.x, strela.y , strela2.y):
         strela.push = False
         strela2.push =False

         strela2.y = hero3.y + 10
         strela2.x = hero3.x + 12

         strela.y = hero1.y + 10
         strela.x = hero1.x + 12








    """кількість кадрів"""
    #pygame.time.delay(20)
    clock.tick(60)

    screenplay.fill((50,50,50))
    info_string.fill((245, 158, 66))
    strela.render()
    strela2.render()

    """правильне писання рядка"""
    info_string.blit(text,(85,5))
    #pygame.display.update()
    info_string.blit(text2,(415,5))

    info_string.blit(text3,(670,5))

    hero2.render()
    hero1.render()
    hero3.render()



    #target.update(dt)
    #screenplay.blit(target.get_sprites(), (0,0))

    if a1.count(0) < 4 :
         serce1.render()

    if a1.count(0) < 3 :
         serce2.render()

    if a1.count(0) < 2 :
         serce3.render()


    if a2.count(0) < 4 :
          serce4.render()
    if a2.count(0) < 3 :
          serce5.render()
    if a2.count(0) < 2 :
          serce6.render()
    #window.blit(serce1,(610,5))

    window.blit(screenplay ,(0,30))
    window.blit(info_string ,(0,0))





    #global animCount
    if animCount + 1 >= 15 :
        animCount = 0

    if left :
        screenplay.blit(walkLeft[animCount // 5], (60,80))
        animCount += 1
    elif right:
        screenplay.blit(walkRight[animCount // 5], (60,80))
        animCount += 1
    else :
         screenplay.blit(playerstandblue, (60,80))











    pygame.display.flip()
