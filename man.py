from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CalcApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, My Calculate", halign="center")


CalcApp().run()