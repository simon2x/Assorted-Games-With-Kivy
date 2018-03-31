''' Menu screen '''

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty
from  kivy.uix.label import Label

Builder.load_file('menuscreen.kv')


games = [
    ('Classic Pong', ''),
    ('Future Pong', ''),
    ('Jetman', ''),
    ('The Boxer', ''),
]

# class FitLabel(Label):
    
    # scale_factor = .6
    # factor = dimension = None
    # markup = True
    # font_name = StringProperty('Saniretro')
    
    # def on_texture_size(self, *args):  
        # """ auto resize font to fit texture size """
        # try:
            # if not self.factor:
                # self.factor = [self.font_size/self.texture_size[0],
                               # self.font_size/self.texture_size[1]]

            # self.font_size0 = self.size[0] * self.scale_factor * self.factor[0]
            # self.font_size1 = self.size[1] * self.scale_factor * self.factor[1]

            # if self.font_size0 < self.font_size1:
                # self.font_size = self.font_size0
            # else:
                # self.font_size = self.font_size1
                
        # except ZeroDivisionError:
            # pass

class FitLabel(Widget):
    
    scale_factor = .6
    factor = dimension = None
    markup = True
    font_name = StringProperty('Saniretro')
    label = ''
    font_size = 10
   
    def __init__(self, **kw):
        super(FitLabel, self).__init__(**kw)
        
        # With 
        self._label = Label(markup=True)
        self.add_widget(self._label)
        self._label.markup = True
        self._label.text = self.label        
        self._label.color = 1,1,1,1   
        self._label.font_size = self.font_size

        # self._label.bind(on_size=self.on_texture_size)                
        # self.on_texture_size()
        
    def on_texture_size(self, *args):
        """ fit text inside size """        
        try:
            if not self.factor:
                self.factor = [self._label.font_size/self._label.texture_size[0], 
                               self._label.font_size/self._label.texture_size[1]]

            font_size0 = self.size[0] * self.scale_factor * self.factor[0]
            font_size1 = self.size[1] * self.scale_factor * self.factor[1]
            
            if font_size0 < font_size1:
                self._label.font_size = font_size0
            else:
                self._label.font_size = font_size1
        except ZeroDivisionError:
            pass
        print(self.label,"")    
        
class LabelButton(Widget):
    
    label = StringProperty('testing')
    markup = True
    scale_factor = NumericProperty(2)
    factor = None
    size_hint_y: None
    font_size = NumericProperty(50)
    
    def __init__(self, **kw):
        super(LabelButton, self).__init__(**kw)
        
        self._label = Label(markup=True)
        self.add_widget(self._label)
        self._label.markup = True
        self._label.text = self.label        
        self._label.color = 1,1,1,1   
        self._label.font_size = self.font_size

        self._label.bind(on_size=self.on_texture_size)                
        self.on_texture_size()
        
    def on_texture_size(self, *args):
        """ fit text inside size """
        
        try:
            if not self.factor:
                self.factor = [self._label.font_size/self._label.texture_size[0], 
                               self._label.font_size/self._label.texture_size[1]]

            font_size0 = self.size[0] * self.scale_factor * self.factor[0]
            font_size1 = self.size[1] * self.scale_factor * self.factor[1]
            
            if font_size0 < font_size1:
                self._label.font_size = font_size0
            else:
                self._label.font_size = font_size1
        except ZeroDivisionError:
            pass
        print(self.label,"")    
        
    # def on_touch_up(self, touch):
        # label = self.label.text 
        # name = self.name
        
        # if not self.collide_point(touch.x, touch.y):
            # return
            
        # if label == "Exit Game":
            # root.sm.current = "playscreen"
            # gamescreen.remove_widget(gamescreen.gamewidget)
            
        # elif label == "Resume Game":        
            # gamewidget.resume_game()
            
        # elif label == "Switch D-Pad Placement":        
            # gamesetupscreen.switch_dpad()
        
        # elif name == "Switch D-Pad Placement Back":        
            # gamesetupscreen.close_ask_switch_dpad()
            
        # elif name == "Withdraw Safely":
            # gamesetupscreen.close_ask_switch_dpad()
            
    # def set_pos(self, x, y):    
        # self.x = x
        # self.y = y
        # self.background.pos = self.pos
        # self.label.pos = self.pos
        
    # def set_size(self, w, h):    
        # self.w = w
        # self.h = h
        # self.size = (w, h)
        
        # self.background.size = self.size
        # self.label.texture_size = self.size
        # self.label.size = self.size
        # self.on_texture_size()
        
    # def set_text(self, string):  
        # self.text = string
        
class MenuScreenWidget(Widget):
    ''' Screen class '''

    def __init__(self, **kwargs):
        super(MenuScreenWidget, self).__init__(**kwargs)
              
        
            
class MenuScreen(Screen):
    ''' Screen class '''

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        # self.box = MenuScreenWidget()
        # self.box = self.ids['gamebox']
        # self.box.orientation = 'vertical'
        # self.box.size_hint = (.4, .5)
        # self.box.pos_hint = {'center_x':.5, 'center_y':.5}
        # self.add_widget(self.box)
        # for game, screen in games:
            # but = Button()
            # but.markup = True
            # but.font_size = 70
            # but.text = '[font=Saniretro]{0}[/font]'.format(game)
            # self.add_widget(but)
        # self.add_widget(self.box)
        # self.box.size_hint = (1, 1)
        # self.box.pos_hint = {'center_x':.5, 'center_y':.5}
        # print(self.gamebox)#,self.ids['gamebox'])    
        # print(self.gamebox,self.ids)
    
    def login(self):
        if not self.manager.has_screen('FeedScreen'):
            from screens.feedscreen import FeedScreen
            self.manager.add_widget(FeedScreen())
            
        self.manager.current = 'FeedScreen'
        
    def play(self, *text):
        print(1,text)
        if not self.manager.has_screen('GameScreen'):
            from screens.gamescreen import GameScreen
            self.manager.add_widget(GameScreen())
            
        self.manager.current = 'GameScreen'
