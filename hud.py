import pyglet
import math
from pyglet.window import key
from pyglet.window import mouse
from pyglet import font


font.add_file('assets/temporary/8-BIT-WONDER.ttf')
new_font = font.load('8BIT WONDER', 16)

#PHASE 0

label_title       = pyglet.text.Label("GAME NAME",font_name='8BIT WONDER',font_size=30,x=180, y=280)
label_name 		  = pyglet.text.Label("Dizon · Romero · Virtucio ",font_name='8BIT WONDER',font_size=10,x=220, y=250)
dog1_image		  = pyglet.image.load('assets/temporary/DOGE1_MEDIUM.png')
dog2_image		  = pyglet.image.load('assets/temporary/DOGE2_MEDIUM.png')
doge_sprite       = pyglet.sprite.Sprite(dog1_image)
time = [0]

label_button = []
label_button.append( pyglet.text.Label("PLAY",	  font_name='8BIT WONDER',font_size=17,x=320, y=180) )
label_button.append( pyglet.text.Label("HIGHSCORE",font_name='8BIT WONDER',font_size=17,x=270, y=150) )
label_button.append( pyglet.text.Label("QUIT",	  font_name='8BIT WONDER',font_size=17,x=320, y=120) )

mouse_down = False

buttons = [ (320,180) , (270,150) , (320,120) ]

doge_sprite.position = (320,330)
doge_sprite.scale = 0.5

#PHASE 1
label_lives = pyglet.text.Label("",font_name='8BIT WONDER',font_size=13,x=10, y=480)
label_score = pyglet.text.Label("",font_name='8BIT WONDER',font_size=13,x=340, y=480)

def update(phase, dt, lives, score, mouse_position, goto_phase):
	if phase == 0:
		
		#check if button hover
		for i in label_button:
			dx = mouse_position[0] - i.x
			dy = mouse_position[1] - i.y

			if dx >= 0 and dx <= i.content_width and dy >= 0 and dy <= i.content_height:
				i.color = ( 255, 100, 100 , 255)
				if mouse_down and i is label_button[0]:
					goto_phase(1)
				elif mouse_down and i is label_button[2]:
					goto_phase(3)


			else:
				i.color = (255,255,255,255)


	elif phase == 1:
		label_lives.text = "Lives: " + str(lives) 
		label_score.text = "Score: " + str(math.floor(score)) 
	else:
		...

def on_mouse_press():
	global mouse_down
	mouse_down = True

def on_mouse_release():
	global mouse_down
	mouse_down = False

def draw(phase):

	if phase == 0:
		label_title.draw()
		label_name.draw()
		time[0]+=1


		if (time[0] // 30)&1 :
			doge_sprite.image = dog1_image
		else:
			doge_sprite.image = dog2_image
		doge_sprite.draw()

		for i in label_button:
			i.draw()

	elif phase ==1 :
	    label_lives.draw()
	    label_score.draw()
	else:
		...