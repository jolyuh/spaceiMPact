import pyglet
import math
from pyglet import font

font.add_file('assets/temporary/8-BIT-WONDER.ttf')
new_font = font.load('8BIT WONDER', 16)

# PHASE 0

label_title_1 = pyglet.text.Label("SPACE DOGGO:", font_name='8BIT WONDER', font_size=30,
                                  anchor_x='center', x=360, y=270)
label_title_2 = pyglet.text.Label("EARTH'S DEFENDER", font_name='8BIT WONDER', font_size=22.5,
                                  anchor_x='center', x=360, y=235)
label_name = pyglet.text.Label("Dizon · Romero · Virtucio ", font_name='8BIT WONDER', font_size=10,
                               anchor_x='center', x=360, y=197)
dog1_image = pyglet.image.load('assets/temporary/DOGE1_MEDIUM.png')
dog2_image = pyglet.image.load('assets/temporary/DOGE2_MEDIUM.png')
doge_sprite = pyglet.sprite.Sprite(dog1_image)
time = [0]

label_button = []
label_button.append(pyglet.text.Label("PLAY", font_name='8BIT WONDER', font_size=17, x=320, y=150))
label_button.append(pyglet.text.Label("QUIT", font_name='8BIT WONDER', font_size=17, x=325, y=120))

mouse_down = False
mouse_prev = False

buttons = [(320, 150), (270, 120), (320, 90)]

doge_sprite.position = (320, 330)
doge_sprite.scale = 0.5

# PHASE 1

label_lives = pyglet.text.Label("", font_name='8BIT WONDER', font_size=13, x=10, y=480)
label_score = pyglet.text.Label("", font_name='8BIT WONDER', font_size=13, x=290, y=480)
label_hiscore = pyglet.text.Label("", font_name='8BIT WONDER', font_size=13, x=500, y=480)

# PHASE 2

label_gameover = pyglet.text.Label("GAME OVER", font_name='8BIT WONDER', font_size=30, x=180, y=280)

label_game_ur_score = pyglet.text.Label("YOUR SCORE", font_name='8BIT WONDER', font_size=10, x=210, y=240)
label_game_score = pyglet.text.Label("32", font_name='8BIT WONDER', font_size=25, x=235, y=190)

label_game_val_hiscore = pyglet.text.Label("HIGH SCORE", font_name='8BIT WONDER', font_size=10, x=370, y=240)
label_game_hiscore = pyglet.text.Label("120", font_name='8BIT WONDER', font_size=25, x=380, y=190)

button_home = pyglet.text.Label("MENU", font_name='8BIT WONDER', font_size=20, x=300, y=120)


def update(phase, dt, lives, score, mouse_position, goto_phase, high_score):
    global mouse_prev, mouse_down

    if phase == 0:

        # check if button hover
        for i in label_button:
            dx = mouse_position[0] - i.x
            dy = mouse_position[1] - i.y

            if 0 <= dx <= i.content_width and 0 <= dy <= i.content_height:
                i.color = (255, 100, 100, 255)
                if mouse_down and i is label_button[0]:
                    goto_phase(1)
                elif mouse_down and i is label_button[1]:
                    goto_phase(4)

            else:
                i.color = (255, 255, 255, 255)

    elif phase == 1:
        label_lives.text = "Lives: " + str(lives)
        label_score.text = "Score: " + str(math.floor(score))
        label_hiscore.text = "HI: " + str(math.floor(high_score))

    elif phase == 2:

        label_game_score.text = str(math.floor(score))
        label_game_hiscore.text = str(math.floor(high_score))
        but = button_home
        dx = mouse_position[0] - but.x
        dy = mouse_position[1] - but.y

        if 0 <= dx <= but.content_width and 0 <= dy <= but.content_height:
            but.color = (255, 100, 100, 255)
            if not mouse_down and mouse_prev:
                goto_phase(0)
        else:
            but.color = (255, 255, 255, 255)
    mouse_prev = mouse_down


def on_mouse_press():
    global mouse_down
    mouse_down = True


def on_mouse_release():
    global mouse_down
    mouse_down = False


def draw(phase):

    if phase == 0:
        label_title_1.draw()
        label_title_2.draw()
        label_name.draw()
        time[0] += 1

        if (time[0] // 30) & 1:
            doge_sprite.rotation = 5
            doge_sprite.position = (320, 330)
            doge_sprite.image = dog1_image
        else:
            doge_sprite.rotation = -2
            doge_sprite.position = (320, 324)
            doge_sprite.image = dog2_image
        doge_sprite.draw()

        for i in label_button:
            i.draw()

    elif phase == 1:
        label_lives.draw()
        label_score.draw()
        label_hiscore.draw()

    elif phase == 2:
        label_gameover.draw()
        label_game_ur_score.draw()
        label_game_score.draw()
        label_game_val_hiscore.draw()
        label_game_hiscore.draw()

        time[0] += 1
        if (time[0] // 30)& 1:
            doge_sprite.rotation = 5
            doge_sprite.position = (320, 330)
            doge_sprite.image = dog1_image
        else:
            doge_sprite.rotation = -2
            doge_sprite.position = (320, 324)
            doge_sprite.image = dog2_image
        doge_sprite.draw()

        button_home.draw()
