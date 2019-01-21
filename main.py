import pygame
import math
import shutil

maxToGenerate = 94
screenSize = int(math.sqrt(maxToGenerate)*10)

passwordSize = int(input("Password Size : "))
password = ""

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
            percentage = len(password)*100/passwordSize
            terminalSize = shutil.get_terminal_size()
            loadBarComponent1 = "■"*int((terminalSize.columns-2)*percentage/100)
            loadBarComponent2 = " "*(terminalSize.columns-2-len(loadBarComponent1))
            print(f"[{loadBarComponent1}{loadBarComponent2}]",end="\r")
            if i%10 == 0:
                password += chr(33+tmp-1)
            if len(password) >= passwordSize:
                finish = True
            i += 1

terminalSize = shutil.get_terminal_size()
print(" "*terminalSize.columns, end="\r")
print(password)