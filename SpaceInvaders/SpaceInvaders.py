import pgzrun
player = Actor("spaceship")
player.x = 400
player.y = 600-player.height * 0.5
speed = 5
aliens = []
def add_alien():
    alien = Actor("alien1")
    alien.x = 400
    alien.y = alien.height * 0.5
    aliens.append(alien)
clock.schedule_interval(add_alien, 5)
lasers = []
def fire_laser():
    laser = Rect((player.x, player.y), (1,5))
    lasers.append(laser)
def update():
    if keyboard.left:
        player.x = max(player.width * 0.5, player.x - speed)
    if keyboard.right:
        player.x = min(800 - player.width * 0.5, player.x + speed)
    if keyboard.space:
        fire_laser()
    for laser in lasers:
        laser.y -= 20
def draw():
    screen.clear()
    player.draw()
    for laser in lasers:
        screen.draw.filled_rect(laser, (0, 255, 0))
    for alien in aliens:
        alien.draw()

pgzrun.go()
