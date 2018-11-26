#create new player
def new_player():
	a = { "sprite" : pyglet.sprite.Sprite(img_player) }
	a["sprite"].position = (10,0)
	#define update function
	def update(dt):
		spr = a["sprite"]

		#follow mouse
		spr.position = ( 10 , spr.position[1] + (mouse_position[1] - spr.position[1])//10 )

		#deform sprite
		spr.scale_y  = 1 - (mouse_position[1] - spr.position[1])/500;

	#save the function indside the dictinory
	a["update"] = update
	return a