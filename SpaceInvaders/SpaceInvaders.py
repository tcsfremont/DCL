import pgzrun
from random import random
game_over = False
game_start = False
player = Actor("spaceship")
player.x = 400
player.y = 600-player.height * 0.5
speed = 5
cooldown = 0.0000000000000000000001
cooled = True
def cool():
    global cooled
    cooled = True
aliens = []
def add_alien():
    alien = Actor("alien1")
    alien.x = alien.width  * 0.5 + (800 - alien.width) * random()
    alien.y = alien.height * 0.5
    aliens.append(alien)
def add_aliens():
    for a in range(2):
        add_alien()
def on_key_down(key):
    global game_start
    if not game_start:
        game_start = True
        clock.schedule_interval(add_alien, 1)
        clock.schedule_interval(add_alien, 5)
lasers = []
def fire_laser():
    global cooled
    if cooled:
        laser = Rect((player.x, player.y), (1,75))
        lasers.append(laser)
        cooled = False
        clock.schedule_unique(cool, cooldown)
def update():

    global game_over, game_start

    if not game_over:
        if keyboard.left:
            player.x = max(player.width * 0.5, player.x - speed)
        if keyboard.right:
            player.x = min(800 - player.width * 0.5, player.x + speed)
        if keyboard.space:
            fire_laser()
    for alien in aliens:
        alien.y += 3
        if alien.y>600:
            game_over = True
    for laser in lasers:
        laser.y -= 20
        for alien in aliens:
            if laser.x > alien.x-alien.width * 0.5:
                if laser.y > alien.y-alien.height * 0.5:
                    if  laser.x < alien.x + alien.width * 0.5:
                        if laser.y < alien.y + alien.height * 0.5:
                            aliens.remove(alien)
def draw():
    screen.clear()
    player.draw()
    for laser in lasers:
        screen.draw.filled_rect(laser, (0, 255, 0))
    for alien in aliens:
        alien.draw()

    if game_over:
        screen.draw.text("Game Over", (400, 300))

pgzrun.go()
