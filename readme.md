## Description

plugin for Keyboard hotkeys, define a key combo to trigger listening. In this fork I changed from `keyboard` package (that needs root permissions) to `python-evdev`. 


## Install

`pip install ovos_ww_plugin_hotkeys` (for Docker see below)
`python-evdev` (https://python-evdev.readthedocs.io/en/latest/)

 - apt-get install python-dev-is-python3 gcc
 - apt-get install linux-headers-$(uname -r)
 - sudo pip install evdev 


## For OVOS-docker (https://github.com/OpenVoiceOS/ovos-docker/) 
Install evdev in host
Install evedev in container

Add `git+https://github.com/timonvanhasselt/ovos-ww-plugin-hotkeys` to the stt.list file in `ovos/config` or install manually in the `ovos_listener` container.

Add `/dev/input` in the `devices` section of `ovos_listener` in the docker-compose.yml
The section in docker-compose looks like this afterwards:


 `` 
 ovos_listener:
    <<: *podman
    container_name: ovos_listener
    hostname: ovos_listener
    restart: unless-stopped
    image: docker.io/smartgic/ovos-listener-dinkum:${VERSION}
    group_add:
      - "102"
    logging: *default-logging
    pull_policy: always
    environment:
      PULSE_SERVER: unix:${XDG_RUNTIME_DIR}/pulse/native
      PULSE_COOKIE: /home/${OVOS_USER}/.config/pulse/cookie
      TZ: $TZ
    network_mode: host
    devices:
      - /dev/snd
      - /dev/input
    volumes:
      - ~/.config/pulse/cookie:/home/${OVOS_USER}/.config/pulse/cookie:ro
      - ${OVOS_CONFIG_FOLDER}:/home/${OVOS_USER}/.config/mycroft:ro
      - ovos_listener_records:/home/${OVOS_USER}/.local/share/mycroft/listener
      - ovos_models:/home/${OVOS_USER}/.local/share/precise-lite
      - ovos_vosk:/home/${OVOS_USER}/.local/share/vosk
      - ${TMP_FOLDER}:/tmp/mycroft
      - ${XDG_RUNTIME_DIR}/pulse:${XDG_RUNTIME_DIR}/pulse:ro
    depends_on:
      - ovos_messagebus
      - ovos_phal
``


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


