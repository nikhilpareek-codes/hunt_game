# A file to store all game functions
import pygame
import sys
from bullet import Bullet
from alien import Alien

def key_up_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    if event.key == pygame.K_UP:
        ship.move_up = False
    if event.key == pygame.K_DOWN:
        ship.move_down = False



def key_down_event(event,ship,screen,gs,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    if event.key == pygame.K_UP:
        ship.move_up = True
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    if event.key == pygame.K_SPACE:
        # create new bullet
        new_bullet = Bullet(screen,gs,ship)
        # add into group which is sprites
        bullets.add(new_bullet)


def chk_events(ship,screen,gs,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_event(event,ship,screen,gs,bullets)
        elif event.type == pygame.KEYUP:
            key_up_events(event,ship)

def get_num_rows(gs,alien_height,ship_height):
    available_space_y = (gs.height - (3*alien_height)-ship_height)
    num_rows = int(available_space_y/(3*alien_height))
    return num_rows




def num_alien_x(gs,alien_width):
    available_space_x = gs.width - 2*alien_width
    no_x = int(available_space_x/(2*alien_width))
    return no_x

def create_alien(screen,gs,alien_number,aliens,row_number):
    alien = Alien(screen,gs)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)



def create_fleet(gs,screen,aliens,ship):
    alien = Alien(screen,gs)
    no_x = num_alien_x(gs,alien.rect.width)
    no_rows = get_num_rows(gs,alien.rect.height,ship.rect.height)
    # to print rows
    for row_number in range(no_rows):
        # coloumns
        for alien_number in range(no_x):
            create_alien(screen,gs,alien_number,aliens,row_number)




def check_fleet_edges(gs,aliens):
    for alien in aliens.sprites():
        # check edge of a single alien
        if alien.check_edges():
            change_fleet_direction(gs,aliens)
            break

def change_fleet_direction(gs,aliens):
    for alien in aliens.sprites():
        # drop the fleet
        alien.rect.y += gs.fleet_drop_speed
    gs.fleet_direction *= (-1)






def update(gs,ship,screen,bullets,aliens):
    screen.fill(gs.color)
    ship.update(gs)
    # Draw bullet behind the Ship
    for bullet in bullets.sprites():
        bullet.blitme()
    # Deleting excess bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

    print(len(bullets))



    #    bullet's position update
    bullets.update()
    ship.blitme()
    aliens.draw(screen)


    pygame.display.flip()

def update_aliens(aliens,gs):
    check_fleet_edges(gs,aliens)
    aliens.update()



