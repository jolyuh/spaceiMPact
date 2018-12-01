import pyglet

Projectiles = []


def set_img(new_img):
    global img
    img = new_img


# create projectile
def new_projectile(player):
    a = {
        "sprite": pyglet.sprite.Sprite(img),
        "speed": 400
    }

    # gives bullet to player
    a["sprite"].position = player["sprite"].position[0]+40, player["sprite"].position[1]+10

    def update_projectile(dt):
        spr = a["sprite"]
        spr.position = (spr.position[0] + a["speed"]*dt, spr.position[1])

    a["update"] = update_projectile
    Projectiles.append(a)
    return a


def update(dt):
    for i in Projectiles:
        i["update"](dt)


def draw():
    for i in Projectiles:
        i["sprite"].draw()


# Di na ata to kailangan?
# pyglet.clock.schedule_interval(update, 1/60)
