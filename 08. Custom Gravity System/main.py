from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivent_core.managers.resource_managers import texture_manager
from random import randint, choice
import kivent_core
import kivent_cymunk
from math import radians
from assets_ids import ent
from kivent_core.systems.gamesystem import GameSystem
from kivy.factory import Factory

class GravitySystem(GameSystem):
    def __init__(self, **kwargs):
        super(GravitySystem, self).__init__(**kwargs)
        self.objs = []


    def update(self, dt):
        entities = self.gameworld.entities
        for x in range(len(self.objs)):
            entity = entities[ent[self.objs[x]]]
            body = entity.cymunk_physics.body
            force = (0, -80000)
            body.reset_forces()
            body.apply_force(force)


Factory.register('GravitySystem', cls=GravitySystem)

texture_manager.load_atlas('assets/platform.atlas')

class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld(
            ['renderer', 'position', 'rotate', 'color', 'scale',
             'renderer2', 'camera1', 'cymunk_physics', 'cymunk_touch', 'gravity'],
            callback=self.init_game)

    def init_game(self):
        self.setup_states()
        self.set_state()
        self.draw_objects()
        self.custom_gravity()

    def draw_objects(self):
        init_entity = self.gameworld.init_entity

        # Background
        dict = {'renderer': {'texture': 'background', 'render': True},
                  'position': (400, 300),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer']
        background = init_entity(dict, component_order)

        print self.gameworld.entities[background].entity_id

        # Stars
        for x in range(50):
            ran_pos = (randint(0, 800), randint(0, 600))
            ran_scale = choice([.5, .8, 1, 1.2, 1.5])

            dict = {'renderer': {'texture': 'star', 'render': True},
                      'position': ran_pos,
                      'rotate': 0,
                      'scale': ran_scale,
                      'color': (255,255,255,255),
                    }
            component_order = ['position', 'rotate', 'scale', 'color', 'renderer']
            star = init_entity(dict, component_order)

        print self.gameworld.entities[star].entity_id


        # Moon
        col_shape = [{'shape_info': {'inner_radius': 0, 'outer_radius': 30, 'mass': 300, 'offset': (0, 0)},
                      'collision_type': 1, 'group': 0, 'elasticity': 1, 'friction': 1, 'shape_type': 'circle'}]

        object_physics = {'main_shape': 'circle', 'velocity': (0, 0), 'position': (100, 400), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 300,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'moon', 'render': True},
                  'position': (100, 400),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        moon = init_entity(dict, component_order)

        # Ground
        col_shape = [{'shape_info': {'width': 800, 'height': 50, 'mass': 0,},
              'collision_type': 2, 'group': 0, 'elasticity': .5, 'friction': 1, 'shape_type': 'box'}]

        object_physics = {'main_shape': 'box', 'velocity': (0, 0), 'position': (400, 25), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 0,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'ground', 'render': True},
                  'position': (400, 25),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        moon = init_entity(dict, component_order)


        #turn off gravity in the start
        gravity = self.gameworld.system_manager['gravity']
        gravity.paused = True

    def custom_gravity(self):
        gravity = self.gameworld.system_manager['gravity']
        gravity.objs = ['moon']
        gravity.paused = False


    def setup_states(self):
        self.gameworld.add_state(state_name='main',
            systems_added=['renderer', 'position', 'rotate', 'color', 'scale'],
            systems_removed=[], systems_paused=[],
            systems_unpaused=['renderer', 'gravity'],
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
