import pyglet
from pyglet.window import key
from pyglet.window import mouse

label = pyglet.text.Label("",
                          font_name='Times New Roman',
                          font_size=13,
                          x=70, y=480)

def update(dt, lives):
	label.text = "Lives: " + str(lives) 

def draw():
    label.draw()