# Alien Invasion 

### Created an arcade game with a ship, bullets, and aliens using Pygame


1. Used multiple functions in the pygame module to create ship, detect key presses and integrated interaction of various elements on screen

2. Created graphics to move and control the motion of aliens, bullets and the ship

3. Defined functions to draw the ship and the aliens on screen using the `blitme()` method

4. Created the KEYDOWN and KEYUP events using the `pygame.event.get()` method to detect pressing and releasing of the keys

5. Used the `pygame.sprite` module to group the related elements of bullets and aliens

6. The game’s appearance and the ship’s speed are managed with the Settings class

7. Bullet is created by building a rect from scratch using the `pygame.rect()` class and shooting bullets with midtop attribute to match the ship’s midtop attribute

8. Using speed and x-coordinate value to move the fleet of aliens to right and left comparing it with screen rect

9. Detected the collision of the ship and the aliens using the `spritecollideany()` function
