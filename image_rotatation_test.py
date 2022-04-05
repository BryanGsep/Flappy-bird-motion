import pygame
import cv2
import os

# Make a function allow image rotate around it rotation center
def rotate_image(surface, image, angle, center, center_pos):

    rotated_image = pygame.transform.rotate(image, angle)

    w = image.get_width()
    h = image.get_height()

    # Create a box with four vector that determine conner of the image in compared with the center
    image_box = [pygame.math.Vector2(p) for p in [(-center[0], -center[1]), (w-center[0], -center[1]),
                                                  (-center[0], h-center[1]), (w-center[0], h-center[1])]]


    # Rotate vectors in image_box by certain angle
    rotated_box = [vector.rotate(angle) for vector in image_box]
    new_center_pos = [min(rotated_box, key = lambda p:p[0])[0], max(rotated_box, key = lambda p:p[1])[1]]
    surface.blit(rotated_image, (center_pos[0] + new_center_pos[0], center_pos[1] - new_center_pos[1],
                                 rotated_image.get_width(), rotated_image.get_height()))





def draw_center_point(surface, center_pos):
    pygame.draw.rect(surface, (255, 0, 0), (center_pos[0] - 2, center_pos[1] - 2, 4, 4))




