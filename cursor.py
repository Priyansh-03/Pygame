import pygame,sys

# Initialize Pygame
pygame.init()

# Set up the window
display=pygame.display.set_mode((300,300))
while True:
    #creating a loop to check events that are occuring
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #checking if keydown event happened?
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_j:#check if key j was pressed
                print("Key j has been pressed")
            if event.key==pygame.K_p:#check if key j was pressed
                print("Key p has been pressed")
        elif event.type==pygame.MOUSEMOTION:
            if event.rel[0]>0:
                print("Mouse moved right")
            if event.rel[1]>0:
                print("Mouse moved down")
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==3:
                print("Rihght mouse button pressed")
        elif event.type==pygame.MOUSEBUTTONUP:
            print("Mouse button released")
            