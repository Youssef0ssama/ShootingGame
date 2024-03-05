import pgzrun
import pygame
from random import randint
import time
background =Actor("background")
bird1=Actor("bird1")
bird2=Actor("bird2")
bird3=Actor("bird3")
ballon=Actor("ballon")
HEIGHT=600
WIDTH=900
score=0
Level=1
timer = 0
Win = 700
start_time = time.time()
game_over=False

def draw ():
    screen.clear()
    background.draw()
    bird1.draw()
    bird2.draw()
    bird3.draw()
    ballon.draw()
    
    screen.draw.text("Score: "+str(score) ,color="yellow", topleft=(420,10))
    screen.draw.text("Level: "+str(int(score/100+1)) ,color="yellow", topleft=(800,10))
    screen.draw.text(str(40-timer) ,color="yellow", topleft=(10,10),fontsize=30)

    if score == 0:
       bird1._surf = pygame.transform.scale(bird1._surf, (50, 50))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (50, 50))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (50, 50))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (45 , 45))
       ballon._update_pos()
       
    if score == 100:
       bird1._surf = pygame.transform.scale(bird1._surf, (45, 45))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (45, 45))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (45, 45))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (40, 40))
       ballon._update_pos()

       
    if score == 200:
       bird1._surf = pygame.transform.scale(bird1._surf, (40, 40))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (40, 40))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (40, 40))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (35, 35))
       ballon._update_pos()

       
    if score == 300:
       bird1._surf = pygame.transform.scale(bird1._surf, (35, 35))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (35, 35))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (35, 35))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (30, 30))
       ballon._update_pos()

       
    if score == 400:
       bird1._surf = pygame.transform.scale(bird1._surf, (30, 30))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (30, 30))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (30, 30))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (25, 25))
       ballon._update_pos()

       
    if score == 500:
       bird1._surf = pygame.transform.scale(bird1._surf, (25, 25))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (25, 25))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (25, 25))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (20, 20))
       ballon._update_pos()

       
    if score == 600:
       bird1._surf = pygame.transform.scale(bird1._surf, (20, 20))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (20, 20))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (20, 20))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (15, 15))
       ballon._update_pos()

       
    if score == 700:
       bird1._surf = pygame.transform.scale(bird1._surf, (15, 15))
       bird1._update_pos()
       bird2._surf = pygame.transform.scale(bird2._surf, (15, 15))
       bird2._update_pos()
       bird3._surf = pygame.transform.scale(bird3._surf, (15, 15))
       bird3._update_pos()
       ballon._surf = pygame.transform.scale(ballon._surf, (10, 10))
       ballon._update_pos()
    

    if game_over==True and score >= Win:
        background.draw()
        screen.draw.text("You Won ^_^ ",color="white", topleft=(325,260),fontsize=60)
        screen.draw.text("Final Score: "+str(score) ,color="white", topleft=(280,320),fontsize=60)
    elif game_over==True and score < Win:
        background.draw()
        screen.draw.text("You Lost -_- ",color="white", topleft=(310,260),fontsize=60)
        screen.draw.text("Final Score: "+str(score) ,color="white", topleft=(280,320),fontsize=60)


def update():
    global timer
    global Level
    # Calculate the elapsed time since the start
    elapsed_time =  time.time() - start_time
    # Update the timer variable as an integer
    timer = int(elapsed_time)

def place_bird1():
    bird1.x=randint(100,700)
    bird1.y=randint(100,400)
    
def place_bird2():
    bird2.x=randint(100,700)
    bird2.y=randint(100,400)
    
def place_bird3():
    bird3.x=randint(100,700)
    bird3.y=randint(100,400)
    
def place_ballon():
    ballon.x=randint(100,700)
    ballon.y=randint(100,400)
    
place_bird1()
place_bird2()
place_bird3()
place_ballon()
def on_mouse_down(pos):
    
    global score
    
    if bird1.collidepoint(pos):
        print("GREAT!!")
        place_bird1()
        score=score+10
        
    elif bird2.collidepoint(pos):
        print("GREAT!!")
        place_bird2()
        score=score+10
        
    elif bird3.collidepoint(pos):
        print("GREAT!!")
        place_bird3()
        score=score+10
        
    elif ballon.collidepoint(pos):
        print("GREAT!!")
        place_ballon()
        score=score+30
        
    else:
        print("CLOSE!")
        score=score-10


def time_up():
    global game_over
    game_over=True
clock.schedule(time_up,40.0)

pgzrun.go()
