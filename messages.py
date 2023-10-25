import flet as ft

class Chat(ft.UserControl):
    
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
                        ft.ElevatedButton("Отправить", heght=60, style=ft.ButtonStyle(ft.RoundedRectangleBorder(radius=1)), on_click=self.btn_clicked)
                            ],
                    ),
                self.output_column,
            ],
        )