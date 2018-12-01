import pyglet
import random
import math

Enemies = []
img = [None, None, None]

def setImg(new_img):
    global img
    img = new_img


def add(enemy_type):
    a = {
            "sprite":  pyglet.sprite.Sprite(img[enemy_type]),
            "speed":  100,
            "omega": 0.2*random.uniform(-1, 1),
            "initial_y": 720*random.uniform(-1, 1)
        }

    a["sprite"].position = (720, a["initial_y"])
    a["sprite"].anchor = (12, 14)

    def update1(dt,player):
        spr = a["sprite"]
        spr.rotation += a["omega"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"])
    
    def update2(dt,player):
        spr = a["sprite"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"] + 100*math.sin(spr.position[0]/60))

    def update3(dt,player):
        spr = a["sprite"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"] + math.sin(spr.position[0]))

    a["update"] = [update1, update2, update3][enemy_type]
    Enemies.append(a)
    return a


def update(dt):
    for i in Enemies:
        i["update"](dt)
    a = {
			"sprite":  pyglet.sprite.Sprite(img[enemy_type]),
			"speed":  100,
			"omega": 0.2*random.uniform(-1, 1),
			"initial_y": 720*random.uniform(-1, 1)
		}

    a["sprite"].position = (720, a["initial_y"])
    a["sprite"].anchor = (12, 14)


    def update1(dt,player):
        spr = a["sprite"]
        spr.rotation += a["omega"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"])

    def update2(dt,player):
        spr = a["sprite"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"] + 100*math.sin(spr.position[0]/60))

    def update3(dt,player):
        spr = a["sprite"]
        spr.position = (spr.position[0] - a["speed"]*dt, a["initial_y"] + math.sin(spr.position[0]))

    a["update"] = [update1, update2, update3][enemy_type]
    Enemies.append(a)
    return a


def update(dt,player):
	for i in Enemies:
		i["update"](dt,player)


def draw():
    for i in Enemies:
        i["sprite"].draw()
