import pyglet
import player as Player
import main as Main

Projectiles = []
img = [None]
img_bullet = pyglet.image.load('assets/temporary/heart.png')

def set_img(new_img):
    global img
    img = new_img


# create projectile
def new_projectile():
    a = {
        "sprite": pyglet.sprite.Sprite(img_bullet),
        "speed": 100
    }

    # gives bullet to player
    a["sprite"].position = (Main.window.width//2, Main.window.height//2)

    def update(dt):
        spr = a["sprite"]
        spr.position = (spr.position[0] + a["speed"]*dt, spr.position[1])

    a["update"] = update
    Projectiles.append(a)
    return a
