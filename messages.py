import flet as ft
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Chat(ft.UserControl):

    question = ''
    
    def build(self):
        self.heading = ft.Text(value='Чат-бот техподдержки', size=24)
        self.text_input = ft.TextField(hint_text="Введите ваш запрос...", expand=True, multiline=True)
        self.output_column = ft.Column()
        self.scroll = True
        return ft.Column(
            width=800,
            controls=[
                self.heading,
                ft.Row(
                    controls=[
                        self.text_input,
                        ft.ElevatedButton("Отправить", height=60, style=ft.ButtonStyle(ft.RoundedRectangleBorder(radius=1)), on_click=self.btn_clicked)
                            ],
                    ),
                self.output_column,
            ],
        )
    
    def btn_clicked(self,event):
        typification = ...

def main(page):
    page.scroll = True
    page.window_width = 500
    page.window_height = 700
    mychat = Chat()
    page.add(mychat)

ft.app(target=main, view=ft.WEB_BROWSER)