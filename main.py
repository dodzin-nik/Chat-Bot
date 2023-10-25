import flet as ft
from messages import *

def main(page: ft.Page):
    page.title = "Нацпарк куршская коса"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    

ft.app(target=main, view=ft.WEB_BROWSER)