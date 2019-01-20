import pygame
import math

maxToGenerate = 94
screenSize = int(math.sqrt(maxToGenerate)*10)

PasswordSize = int(input("Password Size : "))
Password = ""

pygame.init()

screen = pygame.display.set_mode((screenSize,screenSize))
pygame.display.set_caption("")

i = 0
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            tmp = pygame.mouse.get_pos()
            tmp = int(tmp[0]/10)*int(tmp[1]/10)
            if i%10 == 0:
                Password += chr(33+tmp-1)
            if len(Password) >= PasswordSize:
                finish = True
            i += 1

print(Password)