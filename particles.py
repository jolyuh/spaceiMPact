import pyglet
import random
import math

Particles = []
imgDMG = pyglet.image.load('assets/temporary/heart.png')
imgDOG = pyglet.image.load('assets/temporary/chocolate_28px.png')

def new_particle(theta,position,image,particle_type):
    a = {
        "sprite":  pyglet.sprite.Sprite(image),
        "speed":  200,
        "omega": 0.2*random.uniform(-1, 1),
        "time": 0,
    }
    a["sprite"].rotation = theta
    a["sprite"].position = position
    a["sprite"].scale = 0.5

    if particle_type == 1:
    	a["speed"]= 500
    	a["scale"]= 2

    def update(dt,player):
        spr = a["sprite"]
        spr.rotation += a["omega"]
        dx = a["speed"]*math.cos(spr.rotation)
        dy = a["speed"]*math.sin(spr.rotation)
        spr.position = (spr.position[0] +dx*dt, spr.position[1] +dy*dt)
        if a["time"]>=30:
        	Particles.remove(a)
        a["time"] +=1
       	spr.scale = 1 - a["time"]/30
    
    a["update"] = update

    Particles.append(a)
    return a

def new_particle_system(position):
	for i in range(0,360,40):
		new_particle(i,position,imgDMG,0)

def new_particle_system_dog(position):
	for i in range(0,360,40):
		new_particle(i,position,imgDOG,1)



def update(dt, player):
    for i in Particles:
        i["update"](dt, player)


def draw():
    for i in Particles:
        i["sprite"].draw()
