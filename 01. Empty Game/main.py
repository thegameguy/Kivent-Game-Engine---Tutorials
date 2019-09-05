from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty
import kivent_core


class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld(
            ['renderer', 'position', 'rotate', 'color', 'scale'],
            callback=self.init_game)

    def init_game(self):
        self.setup_states()
        self.set_state()


    def setup_states(self):
        self.gameworld.add_state(state_name='main',
            systems_added=['renderer', 'position', 'rotate', 'color', 'scale'],
            systems_removed=[], systems_paused=[],
            systems_unpaused=['renderer'],
            screenmanager_screen='main')

    def set_state(self):
        self.gameworld.state = 'main'

class DebugPanel(Widget):
    fps = StringProperty(None)

    def __init__(self, **kwargs):
        super(DebugPanel, self).__init__(**kwargs)
        Clock.schedule_once(self.update_fps)

    def update_fps(self,dt):
        self.fps = str(int(Clock.get_fps()))
        Clock.schedule_once(self.update_fps, .05)

class YourAppNameApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1.)

if __name__ == '__main__':
    YourAppNameApp().run()
