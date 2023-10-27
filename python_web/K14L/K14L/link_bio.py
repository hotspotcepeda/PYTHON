"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("Hola Mola!", color='red'):
    return rx.tex

app = rx.App()
app.add_page(index)
app.compile()
