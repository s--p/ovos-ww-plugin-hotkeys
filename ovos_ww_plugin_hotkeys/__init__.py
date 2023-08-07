from ovos_plugin_manager.templates.hotwords import HotWordEngine
from evdev import InputDevice, ecodes, categorize

class HotKeysWakeWordPlugin(HotWordEngine):
    """Spacebar hotkey, trigger listening with the spacebar"""

    def __init__(self, hotword="hotkeys", config=None, lang="en-us"):
        super().__init__(hotword, config or {}, lang)
        self.found_ww = False
        self.hotkey_code = ecodes.KEY_SPACE
        self.device = InputDevice("/dev/input/event6")

    def handle_hotkey_press(self):
        self.found_ww = True

    def found_wake_word(self, frame_data):
        """ frame data contains audio data that needs to be checked for a wake
        word, you can process audio here or just return a result
        previously handled in update method """
        if self.found_ww:
            self.found_ww = False  # consume keypress
            return True
        return False

    def update(self, chunk):
        """ In here you have access to live audio chunks, allows for
        streaming predictions, result still need to be returned in
        found_wake_word method """
        # Read input events from the device
        for event in self.device.read():
            if event.type == ecodes.EV_KEY and event.code == self.hotkey_code and event.value == 1:
                self.handle_hotkey_press()

    def stop(self):
        """ Perform any actions needed to shut down the hot word engine.

            This may include things such as unload loaded data or shutdown
            external processes.
        """
        pass 
