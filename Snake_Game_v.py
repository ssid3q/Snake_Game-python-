import random
import time
import pygame

size=42
class Game:
    def __init__(self):
        # initializing pygame
        pygame.init()
        pygame.font.init()

        # DisplaySize
        self.screen=pygame.display.set_mode((1000,700))
        self.background = pygame.image.load(r"C:\Users\Nex\Desktop\grass.jpeg")
        # Title
        self.title = pygame.display.set_caption("Snake Game")
        self.length = 1
        self.score=0


        self.food = Food(self.screen)
        self.food.draw()

        self.snake=Snake(self.screen,2)
        self.snake.draw()

        # Screen Score

    def on_screen_text(self):
            font = pygame.font.SysFont('arial', 18)
            self.screen_text = font.render(f"Score : {self.snake.length*5}", True, 'black')
            self.screen.blit(self.screen_text, [650, 0])


    def run(self):
        # To let the window to be open
        run = True
        while run:
            pygame.time.delay(10)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.snake.move_left()

            if keys[pygame.K_RIGHT]:
                self.snake.move_right()

            if keys[pygame.K_UP] :
                self.snake.move_up()

            if keys[pygame.K_DOWN]:
                self.snake.move_down()


            self.snake.walk()
            self.food.draw()
            self.on_screen_text()

            pygame.display.flip()


            # Snake and body collison
            for i in range(3, self.snake.length):
                if abs(self.snake.x[0]) == self.snake.x[i] and abs(self.snake.y[0]) ==self.snake.y[i]:
                    print("game over")
                    exit(0)



            # Snake and food collision
            if abs(self.snake.x[0] - self.food.x) < 28 and abs(self.snake.y[0] - self.food.y) < 28:
                self.snake.increment()
                self.food.change_pos()


            time.sleep(0.12)






class Food:
    def __init__(self,screen):
        self.food=pygame.image.load("C:\\All\\Programming\\Python\\SnakeGame\Photos\\apple.jpg")
        self.screen=screen
        self.x = size*4
        self.y = size*2
        self.score=0
        self.length=2

    def draw(self):
        self.screen.blit(self.food, (self.x, self.y))
        pygame.display.update()

    def food_pos(self):
        self.screen.blit(self.food, (self.x, self.y))


    def change_pos(self):
            self.x = size * random.randint(1, 22)
            self.y = size * random.randint(1, 16)
            self.screen.blit(self.food, (self.x, self.y))




class Snake:
    def __init__(self,screen,length):
        self.length=length
        self.screen=screen
        self.x = [size]*self.length
        self.y = [size]*self.length
        self.vel = 5
        self.block=pygame.image.load(r"C:\All\Programming\Python\SnakeGame\Photos\body.jpg")
        self.direction="down"



    def draw(self):
        background=pygame.image.load(("C:\All\Programming\Python\SnakeGame\Photos\grass.jpeg"))
        self.screen.blit(background, (0, 0))

        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction="left"
    def move_right(self):
        self.direction="right"
    def move_down(self):
        self.direction="down"
    def move_up(self):
        self.direction="up"

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i] = self.y[i - 1]


        if self.direction=="left":
                if self.x[0]<0:
                    self.x[0]=990-self.vel
                else:
                    self.x[0] -= size

        if self.direction == "right":
            if self.x[0]>1000:
                self.x[0]=0+self.vel
            else:
                self.x[0] += size

        if self.direction == "down":
            if self.y[0]>700:
                self.y[0]=0+self.vel
            else:
                self.y[0] += size

        if self.direction == "up":
            if self.y[0]<0:
                self.y[0]=680+self.vel
            else:
                self.y[0] -= size
        self.draw()

    def increment(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)



start=Game()
start.run()
