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