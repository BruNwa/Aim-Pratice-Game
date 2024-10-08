import pygame
import random
import math
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Game")

TARGET_INC = 400 #Time it takes to delay the next target from appearing in ms
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30
BG_COLOR = (71, 71, 71)

LIVES = 3
TOP_BAR_HEIGHT = 50
LABEL_FONT = pygame.font.SysFont("family", 24)

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = (102,0,102)
    SECOND_COLOR = (128,0,128)
    THIRD_COLOR = (190,41,236)
    FIRTH_COLOR = (216,150,255)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
            
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.THIRD_COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.FIRTH_COLOR, (self.x, self.y), self.size * 0.4)
        
    def coll(self, x, y):
        dis = math.sqrt((x- self.x)**2 +(y - self.y)**2)
        return dis <= self.size
    
    def no_coll(self, x, y):
        dis = math.sqrt((x- self.x)**4 +(y - self.y)**4)
        return dis > self.size
    

def draw(win, targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)
        
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont("family", 30)
        self.color = (255, 255, 255)
        self.text_color = (0, 0, 0)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        win.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)    

def format_time(secs):
    milli = math.floor(int(secs* 1000%1000)/ 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)
    
    return f"{minutes:02d}:{seconds:02d}.{milli}"
    
    
def draw_top_bar(win, elapsed_time, target_pressed, misses):
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_lebel = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1 , "black")
    speed = round(target_pressed / elapsed_time, 1)
    speed_label= LABEL_FONT.render(f"Speed: {speed} t/s",1, "black")
    hits_label = LABEL_FONT.render(f"Hits: {target_pressed}", 1, "black")
    lives_label = LABEL_FONT.render(f"Lives Left: {LIVES - misses}", 1, "black")
    
    
    
    win.blit(time_lebel, (5,10))
    win.blit(speed_label, (200, 10))
    win.blit(hits_label, (450, 10))
    win.blit(lives_label, (600, 10))
    
    
    
    
    
def end_screen(win, elapsed_time, target_pressed, clicks):
    win.fill(BG_COLOR)   
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1 , "white")
    speed = round(target_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "white")
    hits_label = LABEL_FONT.render(f"Hits: {target_pressed}", 1, "white")
    if clicks > 0:
        accuracy = round(target_pressed / clicks * 100, 1)
    else:
        accuracy = 0.0
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "white")

    win.blit(time_label, (get_mid(time_label), 100))
    win.blit(speed_label, (get_mid(speed_label), 200))
    win.blit(hits_label, (get_mid(hits_label), 300))
    win.blit(accuracy_label, (get_mid(accuracy_label), 400))

    # Create and draw replay button
    replay_button = Button(WIDTH // 2 - 75, HEIGHT // 2 + 100, 150, 50, "Replay")
    replay_button.draw(win)

    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.is_clicked(pygame.mouse.get_pos()):
                    main()  # Restart the game
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()

           
    
    
def get_mid(surface): 
    return WIDTH / 2 - surface.get_width()/2  
    
    
    
    
def main():
    run = True
    targets = [] 
    clock = pygame.time.Clock()
    
    target_pressed= 0
    clicks = 0
    misses = 0
    start_time= time.time()
    
    
    pygame.time.set_timer(TARGET_EVENT, TARGET_INC)                                                                                           
    while run:
        clock.tick(144)
        click = False
        elapsed_time = time.time() - start_time
        mouse_pos= pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False 
                break
            if event.type ==TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1  
                
        for target in targets:
            target.update()
            
            if target.size <= 0:
                targets.remove(target)
                misses += 0.5
                
                
            if click and target.coll(*mouse_pos) :
                  targets.remove(target)
                  target_pressed += 1
            if misses >= LIVES:
                end_screen(win, elapsed_time, target_pressed, clicks)      
                  
        draw(win, targets)
        draw_top_bar(win, elapsed_time, target_pressed, misses)
        pygame.display.update()
    pygame.quit()
    
    



if __name__ == '__main__':
    main()
