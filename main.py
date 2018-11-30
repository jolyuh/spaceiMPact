import pyglet
import random
from pyglet.window import key
from pyglet.window import mouse

import player as Player
import enemy as Enemy
import projectile as Projectile
import hud as Hud


window = pyglet.window.Window(width=720, height=500)

img_player = pyglet.image.load('assets/temporary/doge1_50px.png')
img_bullet = pyglet.image.load('assets/temporary/heart.png')
img_enemy = pyglet.image.load('assets/temporary/chocolate_28px.png')

# Set sprites
Player.setImg(img_player)
Enemy.setImg([img_enemy, img_enemy, img_enemy])
# Projectile.set_img(img_bullet)



mouse_position = [0, 0]
step = 0					# 30 steps == 1s
score = 0

player = Player.add(mouse_position)
lives = 3
score = 0


def check_collision():
    global lives
    p1 = player["sprite"].position

    for a in Enemy.Enemies:
        p2 = a["sprite"].position
        d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 
        
        if d < 70**2 and not(player["immune"]):
            Enemy.Enemies.remove(a)   #delete self
            player["immune"] = True
            lives -= 1




def controller():
    global step
    if step % 8 == 0:

        if step < 20*30:
            Enemy.add(0)		# Normal not curve
        elif step < 90*30:
            Enemy.add(random.randint(1, 1))		# Normal curve or not
        elif step == 5*30:
            Enemy.add(2)						# Boss


def update(dt):
    global step, score, lives

    controller()

    Player.update(dt)
    Enemy.update(dt,player)
    #Projectile.update(dt)

    check_collision()

    Hud.update(dt,lives)

    score += 1
    step += 1

'''
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        Projectile.new_projectile()
'''

@window.event
def on_mouse_motion(x, y, dx, dy):
    mouse_position[0] = x
    mouse_position[1] = y


@window.event
def on_draw():

    window.clear()

    Player.draw()
    Enemy.draw()
    #Projectile.draw()

    Hud.draw()

pyglet.clock.schedule_interval(update, 1/60) 			# update every 1/60 s , i.e. run @ 60 fps
pyglet.app.run()
