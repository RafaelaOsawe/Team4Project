from random import randint
from guizero import Box, Text, PushButton

def play(screen):
    container = Box(screen, visible=False)

    number = Text(container, text=randint(1, 1000), size=100)

    def change_number():
        number.value = randint(1, 1000)

    PushButton(container, text="Spin", command=change_number)

    return container