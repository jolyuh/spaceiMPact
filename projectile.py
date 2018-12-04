import pyglet

Projectiles = []


def set_img(new_img):
    global img
    img = new_img


# create projectile
def new_projectile(player):
    pr = {
        "sprite": pyglet.sprite.Sprite(img),
        "speed": 400
    }

    # gives bullet to player
    pr["sprite"].position = player["sprite"].position[0]+40, player["sprite"].position[1]+10

    def update_projectile(dt):
        spr = pr["sprite"]
        spr.position = (spr.position[0] + pr["speed"]*dt, spr.position[1])

    pr["update"] = update_projectile
    Projectiles.append(pr)
    return pr


def update(dt):
    for pr in Projectiles:
        pr["update"](dt)


def draw():
    for pr in Projectiles:
        pr["sprite"].draw()
