from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivent_core.managers.resource_managers import texture_manager
from random import randint, choice
from kivy.factory import Factory
from kivent_core.systems.gamesystem import GameSystem

texture_manager.load_atlas('assets/platform.atlas')


class VelocitySystem(GameSystem):

    def update(self, dt):
        entities = self.gameworld.entities
        for component in self.components:
            if component is not None:
                entity_id = component.entity_id
                entity = entities[entity_id]
                position_comp = entity.position
                position_comp.x += component.vx * dt
                position_comp.y += component.vy * dt

Factory.register('VelocitySystem', cls=VelocitySystem)



class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld(
            ['renderer', 'position', 'rotate', 'color', 'scale',
             'velocity'],
            callback=self.init_game)

    def init_game(self):
        self.setup_states()
        self.set_state()
        self.draw_objects()
        self.assign_custom_ID()

    def assign_custom_ID(self):
        objs = ['background',
            'star1', 'star2', 'star3', 'star4', 'star5', 'star6', 'star7', 'star8', 'star9', 'star10', 'star11', 'star12',
            'star13', 'star14', 'star15', 'star16', 'star17', 'star18', 'star19', 'star20', 'star21', 'star22', 'star23',
            'star24', 'star25', 'star26', 'star27', 'star28', 'star29', 'star30', 'star31', 'star32', 'star33', 'star34',
            'star35', 'star36', 'star37', 'star38', 'star39', 'star40', 'star41', 'star42', 'star43', 'star44', 'star45',
            'star46', 'star47', 'star48', 'star49', 'star50']
        num = []
        for x in range(len(objs)):
            new = 0+x
            num.append(new)

        self.ent_list = {}
        for x in range(len(objs)):
            self.ent_list[objs[x]] = num[x]

    def draw_objects(self):
        init_entity = self.gameworld.init_entity

        dict = {'renderer': {'texture': 'background', 'render': True},
                  'position': (400, 300),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer']
        background = init_entity(dict, component_order)

        print self.gameworld.entities[background].entity_id, 'first id'


        for x in range(50):
            ran_pos = (randint(0, 800), randint(0, 600))
            ran_scale = choice([.5, .8, 1, 1.2, 1.5])

            dict = {'renderer': {'texture': 'star', 'render': True},
                      'position': ran_pos,
                      'rotate': 0,
                      'scale': ran_scale,
                      'color': (255,255,255,255),
                    'velocity': {'vx': 0, 'vy': 100},
                    }
            component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'velocity']
            star = init_entity(dict, component_order)

        print self.gameworld.entities[star].entity_id

    def setup_states(self):
        self.gameworld.add_state(state_name='main',
            systems_added=['renderer', 'position', 'rotate', 'color', 'scale',
             'velocity'],
            systems_removed=[], systems_paused=[],
            systems_unpaused=['renderer', 'position', 'rotate', 'color', 'scale',
             'velocity'],
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
