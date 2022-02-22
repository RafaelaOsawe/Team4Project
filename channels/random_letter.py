from random import choice
from guizero import Box, Text, PushButton


def play(screen):
    container = Box(screen, visible=False)

    letter_display = Text(container,
                              text=choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                              size=100)
    def change_letter():
        letter_display.value = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    PushButton(container, text="New", command=change_letter)

    return container
