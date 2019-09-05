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
from cymunk import PivotJoint

texture_manager.load_atlas('assets/platform.atlas')

class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld(
            ['renderer', 'position', 'rotate', 'color', 'scale',
             'renderer2', 'camera1', 'cymunk_physics', 'cymunk_touch'],
            callback=self.init_game)

    def init_game(self):
        self.setup_states()
        self.set_state()
        self.draw_objects()
        self.enable_gravity()
        self.pivot_joint()
        self.collision_callbacks()

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

        print self.gameworld.entities[background].entity_id, 'first entity'

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
              'collision_type': 2, 'group': 1, 'elasticity': .5, 'friction': 1, 'shape_type': 'box'}]

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
        Ground = init_entity(dict, component_order)


        #batholder
        col_shape = [{'shape_info': {'mass': 0, 'vertices': [(0, 36), (-9, 26), (-17, -35), (17, -35), (9, 26)], 'offset': (0, 0)},
               'collision_type': 3, 'group': 1, 'elasticity': 1, 'friction': 1.0, 'shape_type': 'poly'},]


        object_physics = {'main_shape': 'poly', 'velocity': (0, 0), 'position': (400, 85), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 0,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'batholder', 'render': True},
                  'position': (400, 85),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        batholder = init_entity(dict, component_order)

        #bat
        col_shape = [{'shape_info': {'mass': 300, 'vertices': [(-72, 9), (-77, 0), (-72, -9), (45, -5), (45, 5)],
                                     'offset': (0, 0)}, 'collision_type': 4, 'group': 1, 'elasticity': .8, 'friction': 1.0,                                            'shape_type': 'poly'},
                     {'shape_info': {'mass': 380, 'vertices': [(45, 0), (49, -11), (60, -15), (71, -11), (75, 0), (71, 11),
                                                               (60, 15), (49, 11)], 'offset': (0, 0)}, 'collision_type': 4,                                                             'group': 1, 'elasticity': .8, 'friction': 1.0, 'shape_type': 'poly'},]


        object_physics = {'main_shape': 'poly', 'velocity': (0, 0), 'position': (400, 115), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 680,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'bat', 'render': True},
                  'position': (400, 115),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        bat = init_entity(dict, component_order)

        # Goal
        col_shape = [{'shape_info': {'width': 100, 'height': 50, 'mass': 0,},
              'collision_type': 5, 'group': 0, 'elasticity': .5, 'friction': 1, 'shape_type': 'box'}]

        object_physics = {'main_shape': 'box', 'velocity': (0, 0), 'position': (600, 450), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 0,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'goal', 'render': True},
                  'position': (600, 450),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        goal = init_entity(dict, component_order)

        # Youwin
        dict = {'renderer': {'texture': 'youwin', 'render': True},
                  'position': (1000, 300),
                  'rotate': 0,
                  'scale': 1,
                  'color': (255,255,255,255),
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer']
        background = init_entity(dict, component_order)

    def enable_gravity(self):
        physics = self.gameworld.system_manager['cymunk_physics']
        physics.gravity = (0, -100)

    def pivot_joint(self):
        entities = self.gameworld.entities
        physics = self.gameworld.system_manager['cymunk_physics']

        objs = [('batholder', 'bat')]
        for x in range(len(objs)):
            entity = entities[ent[objs[x][0]]]
            batholder = entity.cymunk_physics.body
            entity = entities[ent[objs[x][1]]]
            bat = entity.cymunk_physics.body


            anchr1 = (0, 40)
            anchr2 = (0, 0)


            bat_joint = PivotJoint(batholder, bat,
                                anchr1,
                                anchr2)
            physics.space.add_constraint(bat_joint)

    def show_you_win(self, *args):
        entities = self.gameworld.entities

        entity = entities[ent['youwin']]
        position_ent = entity.position
        position_ent.pos = (400, 500)

    def moon_goal(self, space, arbiter):
        if arbiter.is_first_contact:
            self.show_you_win()

        return True

    def true(self, space, arbiter):
        return True

    def collision_callbacks(self):
        physics_system = self.gameworld.system_manager['cymunk_physics']
    #ranking
        physics_system.add_collision_handler(
            1, 5,
            begin_func= self.moon_goal,
            pre_solve_func= self.true)



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
