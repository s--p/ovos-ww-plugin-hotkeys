## Description

plugin for Keyboard hotkeys, define a key combo to trigger listening

## Install

`pip install ovos_ww_plugin_hotkeys`

Then configure a wake_word with module set to `ovos_ww_hotkeys` in mycroft.conf, add the lines

```json
 "listener": {
      "wake_word": "hotkey" # add this line if you want the keyboard wake word the main listener, otherwise remove the listener part. The default
       listener is then loaded (hey_mycroft)
 },
 "hotwords": {
    "hotkey": {
        "module": "ovos_ww_hotkeys",
        "listen": true, 
        "active": true, # to add the keyboard listener as an extra wake word option, next to the default voice wake word 'Hey Mycroft'
        "hotkey": "space"
      }
   }
 
```


Requirements:
python-evdev (https://python-evdev.readthedocs.io/en/latest/)

 - apt-get install python-dev-is-python3 gcc
 - apt-get install linux-headers-$(uname -r)
 - sudo pip install evdev 

user in ```input``` group

