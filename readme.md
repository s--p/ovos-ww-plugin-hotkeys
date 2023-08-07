## Description

plugin for Keyboard hotkeys, define a key combo to trigger listening

## Install

`pip install ovos_ww_plugin_hotkeys`

Then configure a wake_word with module set to `ovos_ww_hotkeys`

```json
 "listener": {
      "wake_word": "hotkey"
 },
 "hotwords": {
    "hotkey": {
        "module": "ovos_ww_hotkeys",
        "hotkey": "space"
    }
  }
 
```
