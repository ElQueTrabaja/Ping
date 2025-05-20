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

WIDTH, HEIGHT = 700, 500
win = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping")
count_1 = 0
count_2 = 0
background = transform.scale(image.load('a.jpg'), (700, 500))




clock = time.Clock()
finish = False
game = True
while game != False:
    win.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        pass
    display.update()
    clock.tick(60)
