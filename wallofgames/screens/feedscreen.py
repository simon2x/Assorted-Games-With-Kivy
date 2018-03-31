'''Feed screen.'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('feedscreen.kv')

class FeedScreen(Screen):
    '''Screen class.'''

    def show_item(self):
        if not self.manager.has_screen('ItemScreen'):
            from screens.itemscreen import ItemScreen
            self.manager.add_widget(ItemScreen())
        self.manager.current = 'ItemScreen'

    def on_enter(self):
        rv = self.ids.rv
        if not rv.data:
            rv.data = [
                {
                    'text': 'Item {}'.format(str(i))
                }
                for i in range(30)
            ]
