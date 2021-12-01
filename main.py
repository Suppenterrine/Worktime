from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.picker import MDTimePicker
import datetime


class WorktimeApp(MDApp):
    def set_time(self, args):
        now = datetime.datetime.now()
        time_dialog = MDTimePicker()
        time_dialog.set_time(now)
        time_dialog.bind(time=self.get_time)
        time_dialog.open()


    def get_time(self, instance, time):
        hours = 8.3
        delta = datetime.timedelta(hours = hours)
        resultTime = (datetime.datetime.combine(datetime.date(1,1,1),time) + delta).time()
        self.resultTime.text = str(resultTime) + ' Uhr'
        self.label.text = "Feierabend um:"


    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = MDScreen()

        # Logo
        screen.add_widget(Image(
            size_hint_y=None,
            width= 100,
            allow_stretch= True,
            source="logo.png",
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        ))

        # collect user input
        self.user_label = MDLabel(
            text="Klicken Sie auf den Button\num Ihren Feierabend zu berechnen.",
            halign="center",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            theme_text_color="Primary"
        )

        screen.add_widget(self.user_label)

        # secoundary + primary labes
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.resultTime = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.label)
        screen.add_widget(self.resultTime)

        screen.add_widget(MDFillRoundFlatButton(
            text="BERECHNEN",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.set_time
        ))

        return screen


if __name__ == '__main__':
    WorktimeApp().run()
