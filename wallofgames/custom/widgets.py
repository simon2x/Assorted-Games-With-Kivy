from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_file('custom/widgets.kv')

class LabelB(Label):
    bcolor = ListProperty([1,1,0,1])

def register_widgets():
    print("registered custom widgets")
    Factory.register('KivyB', module='LabelB')