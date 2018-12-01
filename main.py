import pyglet
import random
from pyglet.window import key
from pyglet.window import mouse
from time import sleep
from threading import Timer

import player as Player
import projectile as Projectile
import enemy as Enemy
import hud as Hud


window = pyglet.window.Window(width=720, height=500)

img_player = pyglet.image.load_animation('assets/temporary/doge.gif')
doge_bin = pyglet.image.atlas.TextureBin()
img_player.add_to_texture_bin(doge_bin)
img_bullet = pyglet.image.load('assets/temporary/heart.png')
img_enemy = pyglet.image.load('assets/temporary/chocolate_28px.png')
img_background = pyglet.image.load_animation('assets/temporary/plain_space_bg.gif')
bg_bin = pyglet.image.atlas.TextureBin()
img_background.add_to_texture_bin(bg_bin)
img_background_sprite = pyglet.sprite.Sprite(img_background)

# Set sprites
Player.set_img(img_player)
Enemy.set_img([img_enemy, img_enemy, img_enemy])
Projectile.set_img(img_bullet)


# mouse
mouse_position = [0, 0]


step = 0					# 30 steps == 1s

player = Player.add(mouse_position)
lives = 3
score = 0

phase = 0
'''

    0 - Game Menu
    1 - Play
    2 - Game over screen
    3 - High Scores

'''


def check_collision():
    global lives
    p1 = player["sprite"].position

    for a in Enemy.Enemies:
        p2 = a["sprite"].position
        d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 
        
        if d < 70**2:
            Enemy.Enemies.remove(a)   # delete self
            if not(player["immune"]):
                player["immune"] = True
                lives -= 1


def free_memory():

    for a in Enemy.Enemies:
        if a["sprite"].position[0] < 0:
            Enemy.Enemies.remove(a)
    for a in Projectile.Projectiles:
        if a["sprite"].position[0] > window.width:
            Projectile.Projectiles.remove(a)


def spawn_enemy():
    global step
    if step % 8 == 0:

        if step < 20 * 30:
            Enemy.add(0)		                # Normal not curve
        elif step < 90 * 30:
            Enemy.add(random.randint(0, 1))		# Normal curve or not
        elif step == 5 * 30:
            Enemy.add(random.randint(0, 2))						# Boss
        else:
            Enemy.add(random.randint(0, 1))                     # Boss


def update_phase_0(dt):
    ...


def update_phase_1(dt):
    global phase, step, score, lives
    
    spawn_enemy()

    Player.update(dt)
    Enemy.update(dt, player)
    Projectile.update(dt)

    check_collision()
    free_memory()

    if lives <= 0:
        sleep(2)
        phase = 2

    score += 0.1
    step += 1


def update_phase_2(dt):
    ...


def update(dt):

    if phase == 0:
        update_phase_0(dt)
    elif phase == 1:
        update_phase_1(dt)
    else:
        update_phase_2(dt)

    Hud.update(phase, dt, lives, score, mouse_position, goto_phase)


def goto_phase(p):
    global phase

    if p == 4:
        pyglet.clock.unschedule(update)
        pyglet.app.exit()

    sleep(0.1)
    phase = p


@window.event
def on_mouse_motion(x, y, dx, dy):
    mouse_position[0] = x
    mouse_position[1] = y

@window.event
def on_mouse_press(x, y, button, modifiers):

    if button == mouse.LEFT:
        Projectile.new_projectile(player) 
        Hud.on_mouse_press()


@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        Hud.on_mouse_release()



@window.event
def on_draw():
    global phase
    window.clear()

    if phase == 0:
        ...
    elif phase == 1:
        img_background_sprite.draw()
        Projectile.draw()
        Player.draw()
        Enemy.draw()
    else:
        ...

    Hud.draw(phase)


pyglet.clock.schedule_interval(update, 1/60) 			# update every 1/60 s , i.e. run @ 60 fps

pyglet.app.run()
