from pygame import *

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    
    def update(self):
        global vel_y, vel_x, count_1, count_2
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 695:
            self.rect.y += self.speed
        wins1 = font.render(
            'Aciertos:'+ str(count_1), True, (255, 255, 255)
        )
        win.blit(wins1, (40, 50))

class Player2(GameSprite):
    def update(self):
        global vel_y, vel_x, count_1, count_2
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 695:
            self.rect.y += self.speed
        wins2 = font.render(
            'Aciertos:'+ str(count_2), True, (255, 255, 255)
        )
        win.blit(wins2, (450, 50))

class bola(GameSprite):
    
    def update(self):
        global vel_y, vel_x, count_1, count_2
        if self.rect.x <= 5:
            count_2 += 1
            self.rect.x = 250
            self.rect.y = 75
            vel_y = 2
            vel_x = 2
        if self.rect.x >= 695:
            count_1 += 1
            self.rect.x = 250
            self.rect.y = 75
            vel_y = 2
            vel_x = 2
    def mov(self):
        self.rect.x += vel_x
        self.rect.y += vel_y          

WIDTH, HEIGHT = 700, 500
win = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping")
count_1 = 0
count_2 = 0
vel_y = 2
vel_x = 2
background = transform.scale(image.load('a.jpg'), (700, 500))
font.init()
font = font.SysFont('Arial', 50)
play1 = Player1('b.jpg', 50, 250, 30, 150, 3)
play2 = Player2('b.jpg', 600, 250, 30, 150, 3)
pelota = bola('p.jpg', 350, 250, 75, 75, 0)

clock = time.Clock()
finish = False
game = True
while game != False:
    win.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        play1.update()
        play1.reset()
        play2.update()
        play2.reset()
        pelota.update()
        pelota.reset()
        pelota.mov()
        if sprite.collide_rect(pelota, play2):

            vel_y += 1
            vel_x += 1
            vel_x *= -1            
        if sprite.collide_rect(pelota, play1):

            vel_y += 1
            vel_x += 1
            vel_x *= -1            
        if pelota.rect.y >= 450:

            vel_y *= -1            
        if pelota.rect.y <= 50:

            vel_y *= -1
    display.update()
    clock.tick(60)

