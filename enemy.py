import pyglet
import random
import math

Enemies = []
img = [None, None, None]


def set_img(new_img):
    global img
    img = new_img


def add(enemy_type):
    e = {
            "sprite":  pyglet.sprite.Sprite(img[enemy_type]),
            "speed":  100,
            "omega": 0.2*random.uniform(-1, 1),
            "initial_y": 720*random.uniform(-1, 1),
            "boss": False

        }

    if enemy_type == 2:
        e["time"] = 0
        e["sprite"].position = (720, 240)
        e["target"] = (500, 220)
        e["boss"] = True
        e["lives"] = 25
    else:
        e["sprite"].position = (720, e["initial_y"])
    e["sprite"].anchor = (12, 14)

    def update1(dt, player):
        spr = e["sprite"]
        spr.rotation += e["omega"]
        spr.position = (spr.position[0] - e["speed"]*dt, e["initial_y"])
    
    def update2(dt, player):
        spr = e["sprite"]
        spr.position = (spr.position[0] - e["speed"]*dt, e["initial_y"] + 100*math.sin(spr.position[0]/60))

    def goto(pos):
        spr = e["sprite"]

        dx = pos[0] - spr.position[0]
        dy = pos[1] - spr.position[1]

        spr.position = (spr.position[0] + dx/20, spr.position[1] + dy/20)

    def update3(dt, player):
        spr = e["sprite"]
        t = e["time"]

        if t < 30:
            goto((500, 220))
        else:
            m = t % (3*60)
            if m == 0:
                e["target"] = (550, 220)
            elif m == 30:
                e["target"] = (450, 220 + 20*random.uniform(-1, 1))
            elif m == 40:
                e["target"] = (550, 220 + 20*random.uniform(-1, 1))
            elif m == 60:
                if random.uniform(0, 1) > 0.2:
                    e["target"] = player["sprite"].position 
                else:
                    e["target"] = (450, 220)
            elif m == 90:
                if t > 60*60:
                    if random.uniform(0, 1) > 0.5:
                        e["target"] = (player["sprite"].position[0] + 100*random.uniform(-1, 1), player["sprite"].position[1])
                else:
                    if random.uniform(0, 1) > 0.8:
                        e["target"] = player["sprite"].position
            elif m == 150:
                e["target"] = (550, 220)

            if t > 60*60:
                e["sprite"].rotation = 2*random.uniform(-1, 1)

            e["sprite"].color = (255, (255-e["sprite"].color[1])/3 + e["sprite"].color[1], (255-e["sprite"].color[2])/3 + e["sprite"].color[2])

            goto(e["target"])

        e["time"] += 1

    e["update"] = [update1, update2, update3][enemy_type]
    Enemies.append(e)
    return e


def update(dt, player):
    for e in Enemies:
        e["update"](dt, player)


def draw():
    for e in Enemies:
        e["sprite"].draw()
