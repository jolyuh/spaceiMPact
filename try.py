import pyglet
import random
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window(width=500,height=500)

#load assets

img_player = pyglet.image.load('assets/temporary/doge1_medium.png')
img_player_sprite = pyglet.sprite.Sprite(img_player)
img_player_sprite.scale = 0.42
img_bullet = pyglet.image.load('assets/temporary/heart.png')
img_enemy  = pyglet.image.load('assets/temporary/chocolate_28px.png')

#create new player
def new_player():
	a = { "sprite" : img_player_sprite }
	a["sprite"].position = (10,0)
	#define update function
	def update(dt):
		spr = a["sprite"]
		#follow mouse
		spr.position = ( 10 , mouse_position[1] )
	#save the function indside the dictinory
	a["update"] = update
	return a


#create enemy
def new_enemey():
	# define 
	a = { 
			"sprite":  pyglet.sprite.Sprite(img_enemy) , 
			"speed" :  200, 
		}
	#ilagay yung enemy sa right ng screen tapos random  yung height
	a["sprite"].position = ( 500 , 500*random.uniform(-1,1)  )
	#update values every frame
	def update(dt):
		spr = a["sprite"]
		#move papuntang left
		spr.position = ( spr.position[0] - a["speed"]*dt  , spr.position[1])
	#save the function indside the dictinory
	a["update"]  = update
	#add to the list of Enemies
	Enemies.append(a);
	#return the new enemy object
	return a;


#create_projectile
def new_projectile():
	a = {
		"sprite": pyglet.sprite.Sprite(img_bullet) ,
		"speed" : 500,
	}
	#ilagay yung bullet sa player
	a["sprite"].position = player["sprite"].position

	def update(dt):
		spr = a["sprite"]
		spr.position = ( spr.position[0] + a["speed"]*dt , spr.position[1] )

	a["update"] = update
	Projectile.append(a)
	return a


#create player
player = new_player()

# Lists ng mga objects
Enemies = []
Projectile = []

#global vars
mouse_position = [0,0]






def update(dt):

	#update all enemies
	for i in Enemies:
		i["update"](dt) #run update function

	for i in Projectile:
		i["update"](dt) #run update function

	player["update"](dt) #run update function


def spawn_enemies(dt):
	new_enemey();


@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		new_projectile();

@window.event
def on_mouse_motion(x, y, dx, dy):
    mouse_position[0] = x
    mouse_position[1] = y

@window.event
def on_draw():

	window.clear()

	for i in Enemies:
		i["sprite"].draw()
	for i in Projectile:
		i["sprite"].draw()

	player["sprite"].draw()


pyglet.clock.schedule_interval(update, 1/60) 			#update every 1/60 s , i.e. run @ 60 fps
pyglet.clock.schedule_interval(spawn_enemies, 1.5)      #spawn enemies every 1.5 s
pyglet.app.run()