import flet as ft
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from questions import q

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

        default_answer = ''

        question = self.text_input.value
        if fuzz.partial_ratio(question, q.get(1)[1]) >= 70:
            self.output = q.get(1)[1]
        elif fuzz.partial_ratio(question, q.get(1)[1]) >= 70:
            self.output = q.get(1)[1]
        else:
            self.output = default_answer
        result = Output(self.output, self.text_input.value, self.outputDelete)
        self.output_column.controls.append(result)
        self.text_input.value = ""
        self.update()
    
    def outputDelete(self, result):
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
        self.input_display = ft.Container(ft.Text(value=self.mytext_input), bgcolor='#EBECE7', padding=10)
        self.display_view = ft.Column(controls=[self.input_display, self.output_display, self.delete_button])
        return self.display_view
    
    def delete(self, e):
        self.myoutput_delete(self)

def main(page):
    page.scroll = True
    page.window_width = 370
    page.window_height = 440
    mychat = Chat()
    page.add(mychat)

ft.app(target=main)