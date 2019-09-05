from utils import get_asset_path
from jnius import autoclass
from android.runnable import run_on_ui_thread
import kivent_core
import os

os.environ['KIVY_AUDIO'] = 'sdl2'

# sound_manager
sound_manager = self.gameworld.sound_manager

# Load sound
track = 'track1'
address = get_asset_path(track + '.ogg')
track_name = sound_manager.load_sound(track, address, track_count = 1)

# Play sound
sound_manager.play_loop('track1', 1)

# Stop sound
sound_manager.stop('track1')




PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
activity = PythonActivity.mActivity

# Accessing Vibrator_Service through Pyjnius
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

#Vibrate
if vibrator.hasVibrator():
    vibrator.vibrate(500)

# Acessing View through Pyjnius
View = autoclass('android.view.View')
Param = autoclass('android.view.WindowManager$LayoutParams')

@run_on_ui_thread
def android_setflag(self, *args):
    # Point to FLAG_KEEP_SCREEN_ON
    PythonActivity.mActivity.getWindow().addFlags(Param.FLAG_KEEP_SCREEN_ON)

    # set the FLAG_KEEP_SCREEN_ON
    self.android_setflag()



