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
from kivy.uix.button import Button
import kivent_particles

texture_manager.load_atlas('assets/platform.atlas')





class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld(
            ['renderer', 'position', 'rotate', 'color', 'scale',
             'renderer2', 'camera1', 'cymunk_physics', 'cymunk_touch',
             'particles', 'emitters', 'particle_renderer',],
            callback=self.init_game)

    def init_game(self):
        self.setup_states()
        self.set_state()
        self.draw_objects()
        self.pivot_joint()
        self.display_button()
        self.collision_callbacks()
        self.load_emitter()

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

            ran_scale = choice([.5, .8, 1, 1.2, 1.5])

            dict = {'renderer': {'texture': 'star', 'render': True},
                      'position': (1000, 400),
                      'rotate': 0,
                      'scale': ran_scale ,
                      'color': (255,255,255,255),
                    }
            component_order = ['position', 'rotate', 'scale', 'color', 'renderer']
            star = init_entity(dict, component_order)




        # Moon
        col_shape = [{'shape_info': {'inner_radius': 0, 'outer_radius': 30, 'mass': 300, 'offset': (0, 0)},
                      'collision_type': 1, 'group': 0, 'elasticity': 1, 'friction': 1, 'shape_type': 'circle'}]

        object_physics = {'main_shape': 'circle', 'velocity': (0, 0), 'position': (1000, 300), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 300,
                           'col_shapes': col_shape}

        dict = {'renderer2': {'texture': 'moon', 'render': True},
                  'position': (1000 , 300 ),
                  'rotate': 0,
                  'scale': 1 ,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                'emitters': []
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer2',
                           'cymunk_physics', 'emitters']
        moon = init_entity(dict, component_order)

        # Ground
        col_shape = [{'shape_info': {'width': 800 , 'height': 50 , 'mass': 0,},
              'collision_type': 2, 'group': 1, 'elasticity': .5, 'friction': 1, 'shape_type': 'box'}]

        object_physics = {'main_shape': 'box', 'velocity': (0, 0), 'position': (400 , 25 ), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 0,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'ground', 'render': True},
                  'position': (400 , 25 ),
                  'rotate': 0,
                  'scale': 1 ,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        Ground = init_entity(dict, component_order)


        #batholder
        col_shape = [{'shape_info': {'mass': 0, 'vertices': [(0, 36), (-9, 26), (-17, -35), (17, -35), (9, 26)], 'offset': (0, 0)},
               'collision_type': 3, 'group': 1, 'elasticity': 1, 'friction': 1.0, 'shape_type': 'poly'},]


        object_physics = {'main_shape': 'poly', 'velocity': (0, 0), 'position': (400 , 75 ), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 0,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'batholder', 'render': True},
                  'position': (400 , 75 ),
                  'rotate': 0,
                  'scale': 1 ,
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
                  'scale': 1 ,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        bat = init_entity(dict, component_order)

        # Goal
        col_shape = [{'shape_info': {'width': 100, 'height': 50, 'mass': 0,},
              'collision_type': 5, 'group': 0, 'elasticity': .5, 'friction': 1, 'shape_type': 'box'}]

        object_physics = {'main_shape': 'box', 'velocity': (0, 0), 'position': (1000, 150), 'angle': 0,
                           'angular_velocity': 0, 'vel_limit': 1000, 'ang_vel_limit': radians(200), 'mass': 0,
                           'col_shapes': col_shape}

        dict = {'renderer': {'texture': 'goal', 'render': True},
                  'position': (1000, 150),
                  'rotate': 0,
                  'scale': 1 ,
                  'color': (255,255,255,255),
                'cymunk_physics': object_physics,
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer', 'cymunk_physics']
        goal = init_entity(dict, component_order)

        # Youwin
        dict = {'renderer': {'texture': 'youwin', 'render': True},
                  'position': (1200, 500),
                  'rotate': 0,
                  'scale': 1 ,
                  'color': (255,255,255,255),
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer']
        background = init_entity(dict, component_order)

        # Start_btn
        dict = {'renderer': {'texture': 'start_btn', 'render': True},
                  'position': (400, 300),
                  'rotate': 0,
                  'scale': 1 ,
                  'color': (255,255,255,255),
                }
        component_order = ['position', 'rotate', 'scale', 'color', 'renderer']
        background = init_entity(dict, component_order)

    def display_button(self):
        self.btn = Button(size_hint=(None, None),
                          text = 'start',
                          size=(200 , 50 ),
                          pos=((400-100), (300-25)),
                          opacity=0)

        self.add_widget(self.btn)

        self.btn.bind(on_press = lambda x:self.pressing('start_btn'))
        self.btn.bind(on_release = self.level)

    def pressing(self, image):
        entities = self.gameworld.entities
        entity = entities[ent[image]]
        renderer = 'renderer'
        imagerender = entity.renderer
        imagerender.texture_key = image+'_pressed'
        Clock.schedule_once(lambda x:self.releasing(image), .2)

    def releasing(self, image):
        entities = self.gameworld.entities
        entity = entities[ent[image]]
        renderer = 'renderer'
        imagerender = entity.renderer
        imagerender.texture_key = image

    def load_emitter(self):
        emitter_system = self.ids.emitter


        data = {'number_of_particles': 300,
                'texture': 'star',
                'paused': False,
                'pos_variance': (30, 30),
                # 'radial_acceleration': 200,
                # 'tangential_acceleration': 15,
                'rotate_per_second': 15,
                'start_scale': 1.5,
                'end_scale': .1,
                'start_color_variance': (255 ,255, 255, 0),
                'end_color_variance': (255 ,255, 255, 0),
               }
        eff_id = emitter_system.load_effect_from_data(data, 'mooneffects')

    def level(self, click):
        entities = self.gameworld.entities
        physics = self.gameworld.system_manager['cymunk_physics']

        # relocate button
        self.btn.pos = (1200, 400)

        #relocate button texture
        entity = entities[ent['start_btn']]
        entity_pos = entity.position
        entity_pos.pos = (1200, 400)


        objs = ['star1', 'star2', 'star3', 'star4', 'star5', 'star6', 'star7', 'star8', 'star9', 'star10', 'star11', 'star12',
    'star13', 'star14', 'star15', 'star16', 'star17', 'star18', 'star19', 'star20', 'star21', 'star22', 'star23',
    'star24', 'star25', 'star26', 'star27', 'star28', 'star29', 'star30', 'star31', 'star32', 'star33', 'star34',
    'star35', 'star36', 'star37', 'star38', 'star39', 'star40', 'star41', 'star42', 'star43', 'star44', 'star45',
    'star46', 'star47', 'star48', 'star49', 'star50',]

        for x in range(len(objs)):
            entity = entities[ent[objs[x]]]
            entity_pos = entity.position
            entity_pos.pos = (randint(0, 800), randint(0, 600))

        objs = ['moon', 'batholder', 'bat', 'goal',]
        pos = [(100, 400), (400, 75), (400, 115), (600, 450)]

        for x in range(len(objs)):
            entity = entities[ent[objs[x]]]
            body = entity.cymunk_physics.body
            shape = entity.cymunk_physics.shapes
            body.position = ((pos[x][0] ), (pos[x][1] ))
            physics.space.reindex_shape(shape[0])

        emitter_system = self.ids.emitter
        emitter_system.add_effect(ent['moon'], 'mooneffects')

        self.enable_gravity()

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
