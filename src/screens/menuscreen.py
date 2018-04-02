''' Menu screen '''

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ListProperty
from  kivy.uix.label import Label

Builder.load_file('menuscreen.kv')

from custom.widgets import FittedLabel

games = [
    ('Classic Pong', ''),
    ('Future Pong', ''),
    ('Jetman', ''),
    ('The Boxer', ''),
]

        
class MenuGameButton(FittedLabel):
    color_bg = ListProperty([1,1,1,1])
    color = [0,0,0,0]
    scale_factor = 0.6
    
    def on_release(self, **label):
        print(self.label)
        # label = self.label.text 
        # print(self.)
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
