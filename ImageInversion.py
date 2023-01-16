import sys
import pygame

#Get the picture
src_img = sys.argv[1]

#Load the image
img = pygame.image.load(src_img)

#Get the size of the image
(w, h) = img.get_size()
win = pygame.display.set_mode((w, h))

#Fill background with white
win.fill((255, 255, 255))

#Blit image
win.blit(img, (0, 0))

#Update the image
pygame.display.update()

exit_flag = False

while not exit_flag:

	left, middle, right = pygame.mouse.get_pressed()
	
	#If left mouse button gets pressed
	if left:
		
		#Get the position of the mouse
		(mouseX, mouseY) = pygame.mouse.get_pos()
		
		tempX = mouseX + 50
		tempY = mouseY + 50
		
		for y in range (1, 51):
			
			for x in range (1, 51):
				
				if mouseX >= tempX or mouseX >= w: 
					mouseX -= 50
				
				#Get colours
				(r, g, b, _) = win.get_at((mouseX, mouseY))
				
				#Invert colours
				win.set_at((mouseX, mouseY), (255 - r, 255 - g, 255 - b, 255 - _))
				
				#+1 pixel
				mouseX += 1
				
			#+1 pixel
			mouseY += 1
				
			if mouseY >= tempY or mouseY >= h:
				mouseY -= 50
			
		pygame.display.update()

	for e in pygame.event.get():
	
		if e.type == pygame.QUIT:

			exit_flag = True
