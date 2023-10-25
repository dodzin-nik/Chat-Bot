import flet as ft
from fuzzywuzzy import fuzz
from questions import q, default_answer

class ChatBot(ft.UserControl):

    def build(self):
        self.heading = ft.Text(value="Техподдержка", size=24)
        self.text_input = ft.TextField(hint_text="Введите ваш вопрос...", expand=True, multiline=True)
        self.output_column = ft.Column()
        self.scroll = True
        return ft.Column(
            width=370,
            controls=[
                self.heading,
                ft.Row(
                    controls=[
                        self.text_input,
                        ft.ElevatedButton("отправить", height=60, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)), on_click=self.button_clicked),
                    ],
                ),
                self.output_column,
            ],
        )
    
    def button_clicked(self, event):
        typization = self.text_input.value
        if fuzz.partial_ratio(typization, q.get(1)[0]) >= 70:
            answer = q.get(1)[1]
        elif fuzz.partial_ratio(typization, q.get(2)[0]) >= 70:
            answer = q.get(2)[1]
        else:
            answer = default_answer
        self.output = answer
        result = Output(self.output, self.text_input.value, self.removing)
        self.output_column.controls.append(result)
        self.text_input.value = ""
        self.update()

    def removing(self, result):
        self.output_column.controls.remove(result)
        self.update()

class Output(ft.UserControl):
    def __init__(self, myoutput, mytext_input, myoutput_delete):
        super().__init__()
        self.myoutput = myoutput 
        self.mytext_input = mytext_input
        self.myoutput_delete = myoutput_delete

    def build(self):
        self.output_display = ft.Text(value=self.myoutput, selectable=True)
        self.delete_button = ft.IconButton(ft.icons.DELETE_OUTLINE_SHARP, on_click=self.delete)
        self.input_display = ft.Container(ft.Text(value=self.mytext_input), bgcolor=ft.colors.BLUE_GREY_100, padding=10)
        self.display_view = ft.Column(controls=[self.input_display, self.output_display, self.delete_button])
        return self.display_view

    def delete(self, event):
        self.myoutput_delete(self)

def main(page):
    page.scroll = True
    page.window_width = 370
    page.window_height = 440
    chat = ChatBot()
    page.add(chat)

ft.app(target=main, port=8080, view=ft.AppView.WEB_BROWSER)