import pyglet
import random
import math

Enemies = []
img = [None, None, None]


def set_img(new_img):
    global img
    img = new_img


def add(enemy_type):
    a = {
            "sprite":  pyglet.sprite.Sprite(img[enemy_type]),
            "speed":  100,
            "omega": 0.2*random.uniform(-1, 1),
            "initial_y": 720*random.uniform(-1, 1),
            "boss": False

        }

    if enemy_type == 2:
        a["time"] = 0
        a["sprite"].position = (720, 240)
        a["target"] = (500, 220)
        a["boss"] = True
    else:
        a["sprite"].position = (720, a["initial_y"])
    a["sprite"].anchor = (12, 14)

    def update1(dt, player):
        spr = a["sprite"]
        spr.rotation += a["omega"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"])
    
    def update2(dt, player):
        spr = a["sprite"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"] + 100*math.sin(spr.position[0]/60))

    def goto(pos):
        spr = a["sprite"]

        dx = pos[0] - spr.position[0]
        dy = pos[1] - spr.position[1]

        spr.position = (spr.position[0] + dx/20, spr.position[1] + dy/20)

    def update3(dt, player):
        spr = a["sprite"]
        t = a["time"]

        if t < 30:
            goto((500, 220))
        else:
            m = t % (3*60)
            if m == 0:
                a["target"] = (550, 220)
            elif m == 30:
                a["target"] = (450, 220 + 20*random.uniform(-1, 1))
            elif m == 40:
                a["target"] = (550, 220 + 20*random.uniform(-1, 1))
            elif m == 60:
                if random.uniform(0, 1) > 0.2:
                    a["target"] = player["sprite"].position 
                else:
                    a["target"] = (450, 220)
            elif m == 90:
                if t > 60*60:
                    if random.uniform(0, 1) > 0.5:
                        a["target"] = (player["sprite"].position[0] + 100*random.uniform(-1, 1), player["sprite"].position[1])
                else:
                    if random.uniform(0, 1) > 0.8:
                        a["target"] = player["sprite"].position
            elif m == 150:
                a["target"] = (550, 220)

            if t > 60*60:
                a["sprite"].rotation = 2*random.uniform(-1, 1)

            a["sprite"].color = (255, (255-a["sprite"].color[1])/3 + a["sprite"].color[1], (255-a["sprite"].color[2])/3 + a["sprite"].color[2])

            goto(a["target"])

        a["time"] += 1

    a["update"] = [update1, update2, update3][enemy_type]
    Enemies.append(a)
    return a


def update(dt, player):
    for i in Enemies:
        i["update"](dt, player)


def draw():
    for i in Enemies:
        i["sprite"].draw()
