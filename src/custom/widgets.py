from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file('custom/widgets.kv')

class FittedLabel(ButtonBehavior, Label):
    color_bg = ListProperty([1,1,1,1])    
    factor = None
    font_name = 'Saniretro'
    markup = True  
    scale_factor = 1
    size_hint_y: None
    
    def __init__(self, **kwargs):
        super(FittedLabel, self).__init__(**kwargs)
                
    def on_press(self):
        pass
        
    def on_release(self):
        pass
        
    def on_texture_size(self, *args):
        """ fit text inside size """        
        try:
            if not self.factor:
                self.factor = [self.font_size/self.texture_size[0], 
                               self.font_size/self.texture_size[1]]

            font_size0 = self.size[0] * self.scale_factor * self.factor[0]
            font_size1 = self.size[1] * self.scale_factor * self.factor[1]
            
            if font_size0 < font_size1:
                self.font_size = font_size0
            else:
                self.font_size = font_size1
        except ZeroDivisionError:
            pass
    
def register_widgets():
    print("registered custom widgets")
    Factory.register('KivyB', module='FittedLabel')