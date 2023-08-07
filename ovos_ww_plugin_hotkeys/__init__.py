from ovos_plugin_manager.templates.hotwords import HotWordEngine
from evdev import InputDevice, ecodes, categorize
from ovos_utils.log import LOG

class HotKeysWakeWordPlugin(HotWordEngine):
    """Spacebar hotkey, trigger listening with the spacebar"""

    def __init__(self, hotword="hotkeys", config=None, lang="en-us"):
        super().__init__(hotword, config or {}, lang)
        self.found_ww = False
        self.hotkey_code = ecodes.KEY_SPACE
        self.device = InputDevice("/dev/input/event6")

    def handle_hotkey_press(self):
        LOG.info("space pressed")
        self.found_ww = True

    def found_wake_word(self, frame_data):
        if self.found_ww:
            self.found_ww = False  # consume keypress
            return True
        return False

    def update(self, chunk):
        # Read input events from the device
        for event in self.device.read():
            if event.type == ecodes.EV_KEY and event.code == self.hotkey_code and event.value == 1:
                self.handle_hotkey_press()

    def stop(self):
        pass 
