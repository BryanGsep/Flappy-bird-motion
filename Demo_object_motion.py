import pygame
import os
import image_rotatation_test

pygame.font.init()

#  Global variables

print("Day la loi vao " + os.path.dirname(__file__))

s_width = 1000
s_height = 1000

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Demo object motion')
image = pygame.image.load(os.path.dirname(__file__) + '/Tho5.jpeg')

class Flappy():
    def __init__(self, x0, y0, width, height):
        self.x = x0
        self.y = y0
        self.vy = 0
        self.vx = 10
        self.angle = 0
        self.width = width
        self.height = height
        self.center = [1/3, 0.5]  # Relative center position of the object

    def move_up(self):
        step_length = 60    # Step length
        step_angle = 20     # Step angle
        if self.y - self.center[1]*self.height - step_length < 0:
            self.y = self.center[1]*self.height
        else:
            self.y -= step_length

        if self.angle + step_angle > 70:
            self.angle = 70
        else:
            self.angle += step_angle

        self.vy -= 10

    def move_down(self):
        step_length = 20    # Step length
        step_angle = 10     # Step angle
        if self.y + (1-self.center[1])*self.height + step_length > s_height:
            self.y = s_height - (1-self.center[1]) * self.height
        else:
            self.y += step_length

        if self.angle < step_angle - 70:
            self.angle = -70
        else:
            self.angle -= step_angle

        self.vy += 10

def motion(surface, flappy):
    """ Running this test motion """
    run = True
    clock = pygame.time.Clock()
    gravity = 2
    game_time = 0
    while run:
        game_time += clock.get_rawtime()
        clock.tick()
        if game_time >= 100:
            game_time = 0
            if flappy.vy < 40:
                flappy.vy += gravity
            if flappy.y > 0 and flappy.y < s_height:
                flappy.y += flappy.vy
            if flappy.angle > -64:
                flappy.angle -= 4

        # Motion based on player reaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    flappy.move_up()
                elif event.key == pygame.K_DOWN:
                    flappy.move_down()

        # Fill image with white color
        surface.fill((255,255,255))
        image_rotatation_test.rotate_image(surface, image, flappy.angle,
                                           [flappy.center[0]*flappy.width,flappy.center[1]*flappy.height],
                                           [flappy.x, flappy.y])
        pygame.display.update()

flappy = Flappy(500, 300, 40, 40)
motion(win, flappy)





