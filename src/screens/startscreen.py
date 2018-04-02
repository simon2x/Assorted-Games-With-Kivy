""" Start screen """

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('startscreen.kv')

class StartScreen(Screen):
    """ Screen class """

    def on_enter(self): 
        self.start()
        
    def on_leave(self): 
        self.manager.remove_widget(self)
        
    def start(self):
        if not self.manager.has_screen('MenuScreen'):
            from screens.menuscreen import MenuScreen
            self.manager.add_widget(MenuScreen())
                  
        self.manager.current = 'MenuScreen'
