import kivy
kivy.require('1.1.1')

import custom

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from screens.startscreen import StartScreen



__version__ = "1.0.0"

class AppScreenManager(ScreenManager):
    """ ScreenManager class """
    
    @property
    def app_version(self):
        return __version__
    
class MainApp(App):

    def build(self):
        """ Sets AppScreenManaoneger as root widget """
        sm = AppScreenManager()
        sm.add_widget(StartScreen())
        return sm
        
    def on_pause(self):
        """ Background persistence support for Android/iOS """
        return True
        
    def on_start(self):
        """ Configures app when it starts """
        self.use_kivy_settings = False

    def open_settings(self):
        """ Prevents the settings panel from opening """
        pass

if __name__ == '__main__':
    MainApp().run()