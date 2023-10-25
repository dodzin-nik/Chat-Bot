import flet as ft
# from messages import *

def main(page: ft.Page):
    heading = ft.Text(value="Техподдержка", size=24)
    text_input = ft.TextField()
    submit_button = ft.ElevatedButton("Отправить", height=60)
    page.add(heading)
    page.add(text_input)
    page.add(submit_button)
    print(text_input)

ft.app(target=main)