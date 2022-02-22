#Dev base, which we can then push to the main branch

from channels import random_letter, random_number

from guizero import App, Text, Box, PushButton

WIDTH = 700
HEIGHT = 500

app = App(title="RUPAL",
          bg="lavender blush",
          layout="grid",
          width=WIDTH,
          height=HEIGHT)

taskbar = Box(app, grid=[0, 0], width=round(WIDTH / 3), height=HEIGHT)
screen = Box(app, grid=[1, 0], width=round(2 * WIDTH / 3), height=HEIGHT)

taskbar.bg = "yellow"
screen.bg = "pink"


buttons = Box(taskbar)
active_channel = None

def change_channel(channel):
    global active_channel
    if active_channel:
        active_channel.visible = False
    channel.visible = True
    active_channel = channel



channel1 = Text(screen, text="Snake game", visible=False)
channel2 = random_letter.play(screen)
channel3 = random_number.play(screen)

PushButton(buttons, text="Snake game", command=change_channel, args=[channel1])
PushButton(buttons, text="Random letter", command=change_channel, args=[channel2])
PushButton(buttons, text="RANDOM NUM", command=change_channel, args=[channel3])

app.display()
